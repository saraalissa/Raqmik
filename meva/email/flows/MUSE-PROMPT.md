# Muse prompt: build 6 Mëva email automations (all paused) + switch on Judge.me on the live theme

Store: trymeva.co. Work in Shopify admin only. Do NOT touch the existing Welcome automation. Do NOT activate anything. Leave every new automation turned OFF / paused. Do NOT change shipping rates, products, prices or discounts. Do NOT publish any theme.

Design reference for every email: the existing Welcome email (same header "mëva" on burgundy #3d0f27, peach #f4c9b4 hero band, plum #8e2a5a buttons, cream #F8EFE6 footer). The exact copy for each email is in the attached HTML files (open them in a browser to see the layout). Copy the text exactly, word for word.

Sender on every email: Mëva <info@trymeva.co>.
Footer on every email: "Food supplements should not replace a varied, balanced diet and healthy lifestyle." plus Shopify's standard unsubscribe link.
No discount codes in any of these emails.

## Part A: Shopify Messaging automations (Marketing → Automations → Create automation)

1. **Abandoned checkout.** Use Shopify's "Abandoned checkout" template. Wait time: 4 hours. 1 email. Subject: "You left your jar behind". Copy: 1-abandoned-checkout.html. Button text "Back to your jar". Button link: https://trymeva.co/products/meva-magnesium-gummies?utm_source=email&utm_medium=flow&utm_campaign=abandoned_checkout
2. **Abandoned cart.** Use the "Abandoned cart" template. Wait: 3 hours. 1 email. Subject: "Still thinking it over?" Copy: 2-abandoned-cart.html.
3. **Browse abandonment.** Use the "Abandoned product browse" template. Wait: 24 hours. 1 email. Subject: "The number most labels hide". Copy: 3-browse-abandonment.html.
4. **Post-purchase.** Use the "Thank customers after purchase" / "First purchase" template, or a custom automation with trigger "Order fulfilled".
   - Step (a): send immediately on fulfilment. Subject: "It's on its way". Copy: 4a-post-purchase-thanks.html.
   - Step (b): wait 10 days after fulfilment (about 7 days after delivery). Subject: "How are the gummies going?" Copy: 4b-post-purchase-review.html. Button "Write a review" → https://trymeva.co/products/meva-magnesium-gummies#judgeme_product_reviews
5. **Refill reminder.** Custom automation. Trigger: "Order fulfilled". Wait: 25 days. Condition: the customer has not placed another order since. Subject: "About 5 days left in the jar". Copy: 5-refill-reminder.html. Button "Reorder".
6. **Winback.** Use the "Win back customers" template, or custom: trigger "Order fulfilled" → wait 60 days → condition: no order in the last 60 days. Subject: "Still no drama here". Copy: 6-winback.html. Button "Reorder".

After each one is saved, confirm it shows **Off / Paused / Not active**. Take a screenshot of the Automations list showing all 6 with that status, and one screenshot of each automation's workflow screen.

## Part B: Judge.me on the LIVE theme ("Mëva - Draft (Claude)", the one marked Current/Live)

1. Online Store → Themes → the live theme → Customize.
2. Left sidebar → App embeds (the puzzle-piece icon) → switch ON "Judge.me Reviews" (core). Save.
3. Do not add any app blocks. The star badge and review widget are already in the product page code. Note: on the live theme the code still hides both until the first review exists. The version that shows them in the empty state is on the theme "Copy of Mëva - Draft (Claude)". Sara decides whether to publish that copy.
4. Screenshot the App embeds panel showing Judge.me ON.

## Part C: Judge.me settings (Judge.me app → Settings)

- Reviews: allow reviews from **verified buyers only**. This stops anonymous or fake reviews while we're pre-launch.
- Review request emails: Judge.me sends its own by default. Because our Shopify post-purchase step (b) also asks for a review, turn Judge.me's own request email OFF. Otherwise customers get two requests. Screenshot the setting.

Report back with all screenshots.
