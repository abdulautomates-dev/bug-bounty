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
