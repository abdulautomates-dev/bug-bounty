import websocket
import json
import time

WS_URL = "wss://ws.pointpay.io/"

def test_no_auth():
    print("=== Test 1: order.query WITHOUT auth ===")
    ws = websocket.create_connection(WS_URL, timeout=10)
    req = {"method": "order.query", "params": ["all", 0, 30], "id": 1}
    ws.send(json.dumps(req))
    try:
        resp = ws.recv()
        print("Response:", resp)
    except Exception as e:
        print("No response / error:", e)
    ws.close()

def test_bad_auth():
    print("\n=== Test 2: order.query with GARBAGE auth token ===")
    ws = websocket.create_connection(WS_URL, timeout=10)
    auth_req = {"method": "server.auth", "params": ["INVALID_TOKEN_12345", "web"], "id": 1}
    ws.send(json.dumps(auth_req))
    auth_resp = ws.recv()
    print("Auth response:", auth_resp)

    order_req = {"method": "order.query", "params": ["all", 0, 30], "id": 2}
    ws.send(json.dumps(order_req))
    try:
        resp = ws.recv()
        print("order.query response:", resp)
    except Exception as e:
        print("No response / error:", e)
    ws.close()

if __name__ == "__main__":
    test_no_auth()
    time.sleep(1)
    test_bad_auth()
