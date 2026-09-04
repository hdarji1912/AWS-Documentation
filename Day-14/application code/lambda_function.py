import json
import os
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key


TABLE_NAME = os.environ["TABLE_NAME"]
DEMO_TOKEN = os.environ["DEMO_TOKEN"]
TABLE = boto3.resource("dynamodb").Table(TABLE_NAME)

ALLOWED_STATUSES = {
    "OPEN",
    "PAID",
    "PROCESSING",
    "SHIPPED",
    "DELIVERED",
    "COMPLETED",
}


HTML = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>CloudAdhar Day 14 Order Dashboard</title>
  <style>
    :root { color-scheme: dark; font-family: Inter, system-ui, sans-serif; }
    body { margin: 0; background: #08111f; color: #e5eefb; }
    header { padding: 28px; background: linear-gradient(120deg,#162b55,#5b2a86); }
    h1 { margin: 0 0 8px; }
    header p { margin: 0; color: #cbd5e1; }
    main { max-width: 1050px; margin: auto; padding: 24px; }
    .panel { background: #101c30; border: 1px solid #263957; border-radius: 14px;
             padding: 18px; margin-bottom: 18px; }
    .controls { display: flex; gap: 10px; flex-wrap: wrap; align-items: end; }
    label { display: grid; gap: 6px; color: #b8c7dd; font-size: 14px; }
    input, select, button { border-radius: 8px; border: 1px solid #405575;
                            padding: 10px 12px; font: inherit; }
    input, select { background: #07101d; color: #e5eefb; }
    button { background: #7c3aed; color: white; border: 0; cursor: pointer; }
    button.secondary { background: #2563eb; }
    .orders { display: grid; grid-template-columns: repeat(auto-fit,minmax(260px,1fr)); gap: 14px; }
    .order { border: 1px solid #324764; border-radius: 12px; padding: 15px; background: #0b1627; }
    .status { display: inline-block; padding: 4px 8px; border-radius: 999px;
              background: #164e63; color: #a5f3fc; font-weight: 700; }
    .muted { color: #94a3b8; }
    .message { min-height: 24px; color: #93c5fd; }
    code { color: #f0abfc; }
  </style>
</head>
<body>
  <header>
    <h1>CloudAdhar Day 14 — Order Dashboard</h1>
    <p>Base Query · LSI status filter · GSI order search · Stream-triggered Lambda</p>
  </header>
  <main>
    <section class="panel">
      <div class="controls">
        <label>Customer ID
          <input id="customer" value="C101">
        </label>
        <label>Status filter through LSI1
          <select id="filterStatus">
            <option value="">All orders — base table</option>
            <option>OPEN</option><option>PAID</option><option>PROCESSING</option>
            <option>SHIPPED</option><option>DELIVERED</option><option>COMPLETED</option>
          </select>
        </label>
        <button onclick="loadOrders()">Load orders</button>
      </div>
      <p id="accessPath" class="muted"></p>
    </section>

    <section class="panel">
      <div class="controls">
        <label>Order ID — searched through GSI1
          <input id="orderId" value="O9001">
        </label>
        <button class="secondary" onclick="findOrder()">Find order</button>
        <label>Instructor write token
          <input id="token" type="password" placeholder="Required only for updates">
        </label>
      </div>
      <p id="message" class="message"></p>
    </section>

    <section id="orders" class="orders"></section>
  </main>

  <script>
    const statuses = ["OPEN","PAID","PROCESSING","SHIPPED","DELIVERED","COMPLETED"];

    function escapeHtml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;").replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;").replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    function orderCard(order) {
      const options = statuses.map(status =>
        `<option ${status === order.Status ? "selected" : ""}>${status}</option>`
      ).join("");

      return `<article class="order">
        <h3>${escapeHtml(order.OrderId)}</h3>
        <p><span class="status">${escapeHtml(order.Status)}</span></p>
        <p>Total: ₹${escapeHtml(order.Total)}</p>
        <p class="muted">${escapeHtml(order.CreatedAt)}</p>
        <select id="status-${escapeHtml(order.OrderId)}">${options}</select>
        <button onclick='updateStatus(${JSON.stringify(order.PK)},${JSON.stringify(order.SK)},${JSON.stringify(order.OrderId)})'>Update</button>
      </article>`;
    }

    function showOrders(items) {
      document.getElementById("orders").innerHTML = items.length
        ? items.map(orderCard).join("")
        : `<div class="panel">No matching orders.</div>`;
    }

    async function readJson(url, options = {}) {
      const response = await fetch(url, options);
      const body = await response.json();
      if (!response.ok) throw new Error(body.message || `HTTP ${response.status}`);
      return body;
    }

    async function loadOrders() {
      const customer = document.getElementById("customer").value.trim();
      const status = document.getElementById("filterStatus").value;
      const url = `/api/orders?customerId=${encodeURIComponent(customer)}&status=${encodeURIComponent(status)}`;
      try {
        const result = await readJson(url);
        showOrders(result.items);
        document.getElementById("accessPath").textContent = `Access path: ${result.accessPath}`;
        document.getElementById("message").textContent = `Loaded ${result.count} order(s).`;
      } catch (error) {
        document.getElementById("message").textContent = error.message;
      }
    }

    async function findOrder() {
      const orderId = document.getElementById("orderId").value.trim();
      try {
        const result = await readJson(`/api/order?orderId=${encodeURIComponent(orderId)}`);
        showOrders(result.items);
        document.getElementById("accessPath").textContent = "Access path: GSI1";
        document.getElementById("message").textContent = `GSI1 returned ${result.count} order(s).`;
      } catch (error) {
        document.getElementById("message").textContent = error.message;
      }
    }

    async function updateStatus(pk, sk, orderId) {
      const status = document.getElementById(`status-${orderId}`).value;
      const token = document.getElementById("token").value;
      try {
        await readJson("/api/status", {
          method: "POST",
          headers: {"content-type": "application/json", "x-demo-token": token},
          body: JSON.stringify({pk, sk, status})
        });
        document.getElementById("message").textContent =
          `Updated ${orderId} to ${status}. Check DynamoDB and the Stream Lambda logs.`;
        await loadOrders();
      } catch (error) {
        document.getElementById("message").textContent = error.message;
      }
    }

    loadOrders();
  </script>
</body>
</html>"""


def decimal_default(value):
    if isinstance(value, Decimal):
        if value % 1 == 0:
            return int(value)
        return float(value)
    raise TypeError


def response(status_code, body, content_type="application/json"):
    if not isinstance(body, str):
        body = json.dumps(body, default=decimal_default)

    return {
        "statusCode": status_code,
        "headers": {
            "content-type": content_type,
            "cache-control": "no-store",
            "x-content-type-options": "nosniff",
        },
        "body": body,
    }


def lambda_handler(event, context):
    request_context = event.get("requestContext", {})
    method = request_context.get("http", {}).get("method", "GET")
    path = event.get("rawPath", "/")
    query = event.get("queryStringParameters") or {}

    if method == "GET" and path == "/":
        return response(200, HTML, "text/html; charset=utf-8")

    if method == "GET" and path == "/api/orders":
        customer_id = query.get("customerId", "C101").strip().upper()
        status = query.get("status", "").strip().upper()
        pk = f"CUSTOMER#{customer_id}"

        if status:
            if status not in ALLOWED_STATUSES:
                return response(400, {"message": "Unsupported status"})

            result = TABLE.query(
                IndexName="LSI1",
                KeyConditionExpression=(
                    Key("PK").eq(pk)
                    & Key("LSI1SK").begins_with(f"STATUS#{status}#")
                ),
                ScanIndexForward=False,
            )
            access_path = "LSI1"
        else:
            result = TABLE.query(
                KeyConditionExpression=(
                    Key("PK").eq(pk) & Key("SK").begins_with("ORDER#")
                ),
                ScanIndexForward=False,
            )
            access_path = "Base table PK/SK"

        return response(
            200,
            {
                "accessPath": access_path,
                "count": result.get("Count", 0),
                "items": result.get("Items", []),
            },
        )

    if method == "GET" and path == "/api/order":
        order_id = query.get("orderId", "").strip().upper()
        if not order_id:
            return response(400, {"message": "orderId is required"})

        result = TABLE.query(
            IndexName="GSI1",
            KeyConditionExpression=Key("GSI1PK").eq(f"ORDER#{order_id}"),
        )

        return response(
            200,
            {
                "accessPath": "GSI1",
                "count": result.get("Count", 0),
                "items": result.get("Items", []),
            },
        )

    if method == "POST" and path == "/api/status":
        headers = {
            str(key).lower(): value
            for key, value in (event.get("headers") or {}).items()
        }

        if headers.get("x-demo-token") != DEMO_TOKEN:
            return response(403, {"message": "Invalid instructor token"})

        try:
            payload = json.loads(event.get("body") or "{}")
        except json.JSONDecodeError:
            return response(400, {"message": "Request body must be JSON"})

        pk = str(payload.get("pk", ""))
        sk = str(payload.get("sk", ""))
        status = str(payload.get("status", "")).upper()

        if not pk.startswith("CUSTOMER#") or not sk.startswith("ORDER#"):
            return response(400, {"message": "Only order items can be updated"})

        if status not in ALLOWED_STATUSES:
            return response(400, {"message": "Unsupported status"})

        current = TABLE.get_item(Key={"PK": pk, "SK": sk}).get("Item")
        if not current:
            return response(404, {"message": "Order not found"})

        created_at = current["CreatedAt"]

        updated = TABLE.update_item(
            Key={"PK": pk, "SK": sk},
            UpdateExpression="SET #status = :status, LSI1SK = :lsi",
            ExpressionAttributeNames={"#status": "Status"},
            ExpressionAttributeValues={
                ":status": status,
                ":lsi": f"STATUS#{status}#{created_at}",
            },
            ReturnValues="ALL_NEW",
        )

        return response(200, {"item": updated["Attributes"]})

    return response(404, {"message": "Route not found"})