# For Muse: fix the delivery option shown at checkout (24 Nov 2026, urgent)

## The problem
Mëva is now taking PRE-ORDERS. Nothing ships before mid-January 2027. But checkout on trymeva.co shows a delivery option that promises delivery next week:

> **Royal Mail Tracked · Mon, 30 Nov–Tue, 1 Dec · 2 to 3 working days** (£3.49, shown as FREE with the Black Friday free-delivery discount)

That date is false and must not be shown to customers.

Our own rates in Settings → Shipping and delivery → General profile → United Kingdom are correct, but checkout does not show them:
- "Pre-order: ships by mid-January (tracked UK delivery)": £4.99, orders up to £28.99
- "Pre-order: ships by mid-January (free tracked UK delivery)": £0, orders £29+
- "Next working day · Royal Mail Tracked 24": switched OFF

So the "Royal Mail Tracked £3.49" option and the date come from somewhere else.

## Please do, in this order, and check checkout after each step
How to check: open trymeva.co on a phone in a private tab, add "Buy 2 Get 1 FREE", go to checkout, and enter a UK address (e.g. Vicar Street, Kidderminster, DY10 1DB). Look at "Shipping method". Do NOT complete the order.

1. **Turn off estimated delivery dates.** Settings → Shipping and delivery → look for "Delivery dates", "Estimated delivery dates" or "Delivery promise" (it is currently ON, processing time 1 day). Turn it OFF and save.
2. **Find the "Royal Mail Tracked £3.49" rate.** Check, and screenshot anything you find:
   - Settings → Shipping and delivery: any other shipping profile, "Shopify Shipping", "carrier-calculated rates", or a Royal Mail account.
   - Settings → Markets → United Kingdom → anything about shipping or delivery for this market.
   - Settings → Shipping and delivery → "Delivery customizations" (an app can rename or hide rates).
   If you find a "Royal Mail Tracked" £3.49 rate, delete it or switch it off. Do not change the two "Pre-order" rates above.
3. **If it is still there:** the **Collective** app (Shopify Collective) has its own active delivery service. Mëva does not sell other brands' products. Ask Sara before uninstalling it.
4. **Do not touch 17TRACK.** It only tracks parcels after shipping.

## Done when
Checkout for a UK address shows only:
- "Pre-order: ships by mid-January (free tracked UK delivery)" for £29+ baskets (or the £4.99 one under £29),
- no delivery date range.

## Report back to Sara
- What you turned off or deleted, and where.
- A screenshot of the checkout "Shipping method" section after the fix.

Do not change prices, discounts, the theme, or the Meta ads.
