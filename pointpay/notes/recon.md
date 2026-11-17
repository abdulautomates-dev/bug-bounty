## Marketing site bundles (ofza.com, Next.js App Router)
- Reviewed: webpack, main-app, 16678, 1dd3208c, app/[locale] page + layouts
- Result: no first-party API paths; fetch() calls are Next.js internals only
- In-scope hosts referenced: auth, orders, wallet, spot, profile, features, media (.ofza.com)
- Next: capture authenticated traffic from my own account
## Mobile TLS capture setup (PCAPdroid) - 2026-11-17
- Installed PCAPdroid + PCAPdroid-mitm addon (v2.6, arm64)
- CA cert installed, TLS decryption enabled, Full payload enabled
- Created separate/clean Chrome profile (no saved passwords) for testing, target app = Chrome
- Setup complete but not yet used to capture real PointPay traffic
- Next: start capture, log into PointPay in the clean profile, browse dashboard/buy-crypto/spot,
  stop capture, check Connections tab (look for green lock = decrypted), use HTTP view (⇄ icon)
  to see method/path/response per request

## ws.pointpay.io - WebSocket JSON-RPC API (decrypted via PCAPdroid)
Auth: {"method":"server.auth","params":["<bcrypt-shaped token>","web"],"id":N}
  - NOTE: token has $2y$10$... format (bcrypt). Worth checking: is this a static
    per-client-type token (not sensitive) or something session-specific that
    shouldn't be client-visible in this shape? Needs manual verification, not
    yet a finding.

Observed methods (all via wss://ws.pointpay.io):
  - server.ping / server.auth
  - market.subscribe, market.update (public ticker feed, all pairs)
  - today.subscribe / today.update (24h stats per market)
  - deals.subscribe / deals.update (public trade tape)
  - depth.subscribe / depth.update (order book, full + diff)
  - kline.subscribe / kline.query / kline.unsubscribe (candles)
  - asset.subscribe (seen once, params ["BTC","USDT"])
  - order.query  <-- params ["all", offset, limit] -> {market_name,offset,limit,total,records}
    This is the one to test for IDOR / access control once real orders exist:
    does it only return MY orders (session-scoped), or can offset/limit/market_name
    be manipulated to see another user's orders? Could not test today (0 orders,
    no second account).

Next steps:
  1. Place a small real or test order (if balance allows) so order.query returns
     non-empty data, then check whether the response ever includes another user's
     order/user identifiers.
  2. Try calling order.query BEFORE server.auth succeeds, or with a tampered/empty
     auth token, to see if it still returns data (auth bypass check).
  3. Ask HackenProof whether synthetic/test funds are available, since real-money
     testing isn't comfortable to do just to generate order history.
