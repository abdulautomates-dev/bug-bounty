## Marketing site bundles (ofza.com, Next.js App Router)
- Reviewed: webpack, main-app, 16678, 1dd3208c, app/[locale] page + layouts
- Result: no first-party API paths; fetch() calls are Next.js internals only
- In-scope hosts referenced: auth, orders, wallet, spot, profile, features, media (.ofza.com)
- Next: capture authenticated traffic from my own account
