# Black Friday pre-order launch (Sara, 23 Nov 2026)

Decision: real sales, no refunds. Buyers pre-order at a launch price and wait; we order stock and ship the moment the first batch is ready, by mid-January at the latest. (The first-jar guarantee still applies after delivery.) Because orders are real, Flex, the lab test and the Nutribl order must go ahead regardless of the number of orders.

## Offer (true, with a real end date)
- 20% off every pack, Fri 27 Nov 00:01 – Mon 30 Nov 23:59 UK. Shopify automatic discount "Launch pre-order price: 20% off (27–30 Nov)" (gid://shopify/DiscountAutomaticNode/1467938865211), scheduled.
- 1 jar £19.99 (+£4.99), 2 jars £31.98 (free delivery), 3 jars £39.98 (free delivery). From January: £24.99 / £39.98 / £49.98.
- Never write "was £X": those prices were never charged. Use "from January".
- The old "Black Friday: 3 jars for the price of 2" is removed in the pre-order theme (3 jars is already the price of 2 singles every day).

## Backup of the live site (24 Nov)
- Theme 146303778875 "BACKUP – Live site 24 Nov (before pre-order) – DO NOT TOUCH": exact copy of the live theme 146150785083 as it was before the pre-order launch. To go back: publish 146303778875 (or 146150785083 if it is still unchanged).

## Website: theme "Mëva - PRE-ORDER TEST (draft)" 146296930363, separate from live
- Live theme 146150785083 is untouched. Publish 146296930363 to launch; republish 146150785083 to go back.
- Product page: real checkout, launch-price box (shows only 27–30 Nov), "Pre-order: ships as soon as our first batch is ready, by mid-January 2027 at the latest", order-line property "Pre-order: Ships by mid-January 2027", header bar with the launch offer. Club pop-up and the old Black Friday reserve banner are off in this theme.
- Shipping names: switch at go-live to "Pre-order · Royal Mail Tracked · ships by mid-January" and "Pre-order · Free UK delivery · …", next-day OFF; restore afterwards to "Royal Mail Tracked (2-3 working days)" / "Free UK delivery · Royal Mail Tracked (2-3 working days)", next-day ON. (Claude does both.)

## Ads: campaign 120247508332000424 "MEVA | PRE-ORDER TEST | Sales | GB W45-65 | 2026-11-24" (PAUSED)
- One ad set 120247508332700424 "Launch | 1.4 + G3b | GB W45-65 | Purchase", ends 28 Nov 23:59. Ads: PO_1.4_no-hunting_launch (120247508469240424) and PO_G3b_no-water (120247508466510424). Copy carries the launch price and ship date.
- Paused/unused: ad set B 120247508333090424 (G5) and old ad 120247508341820424.
- At go-live (needs Sara's approval of Meta's spend tokens): ad set budget £24 → £48/day (~$60), campaign spend cap £118 (~$150), enable campaign + ad set + the two ads. Runs Fri 27 – Sat 28 Nov.
- Optional: Sara creates 3 custom audiences in Ads Manager (Visitors 180d, Engagers 365d, Waitlist list); Claude excludes them.

## Waitlist emails (Muse): meva/emails/2026-11-27-launch-preorder-3-emails.md
Fri 27 08:30 "It's open", Sun 29 10:00 "A few questions", Mon 30 18:00 "Tonight at midnight".

## Go-live, Friday 27 Nov morning
1. Sara publishes theme 146296930363. Claude switches the shipping names.
2. Sara places one real test order (and cancels it in Shopify). Claude checks the order, the discount and the Meta Purchase event.
3. Claude enables the campaign with Sara's OK on the spend tokens.
4. Muse sends email 1 at 08:30.
5. Daily: orders, add-to-baskets, spend, cost per order to Sara in Arabic.
6. Tue 1 Dec: Sara republishes the live theme (or keeps pre-orders open at full price); Claude restores shipping names.

## Decision line (written before, ~£95–118 ad spend + waitlist)
- 5+ paid orders from ads → cost per buyer ≤ £24: scale after launch.
- 2–4 → promising; improve offer/page.
- 0–1 from ads → ads don't sell yet; rely on the list, rethink before more ad spend.
Waitlist orders are counted separately (free traffic).

## First batch = 75 jars, shown as a bar (Sara, 23 Nov, replaces the "50 jars, X left" line)
- Product page shows a bar: "51 women on the waitlist · First batch: 75 jars" (bar filled to waitlist ÷ batch). No sold/left numbers.
- The label says WAITLIST, never "sold", "reserved" or "claimed": waitlist sign-ups are not orders.
- Values: shop metafields meva.waitlist_count (51) and meva.first_batch_size (75). Claude updates waitlist_count to the real Shopify count.
- The first batch really is capped at 75 jars; orders beyond it ship with the second batch (~1 week later).

## Go-live log (24 Nov)
- Sara published theme 146296930363 (pre-order) as MAIN.
- Claude renamed checkout delivery methods: "Pre-order · Royal Mail Tracked · ships by mid-January" (£4.99, under £29) and "Pre-order · Free UK delivery · ships by mid-January" (£29+); next-day (Royal Mail Tracked 24) set inactive. Restore after the test: "Royal Mail Tracked (2-3 working days)", "Free UK delivery · Royal Mail Tracked (2-3 working days)", next-day active.
- Active discounts: automatic free UK delivery on every order (24–30 Nov 23:59 UTC); FOUNDING20 code.
- Live check: offer cards, countdown, waitlist bar and guarantee box render; Add to basket adds 3 jars £49.98 with property "Pre-order: Ships by mid-January 2027".
- Waitlist bar stays 51 (Shopify shows 53 tagged "waitlist", including at least one bad address); update when confirmed.
- Next: Sara's test order → check order, discount, Meta Purchase event → ads only with Sara's OK on the spend.
- Checkout delivery fixed by Muse (estimated delivery dates off; "Royal Mail Tracked £3.49 · Mon 30 Nov–Tue 1 Dec" gone). Checkout now shows "Pre-order: ships by mid-January (tracked UK delivery)". Test code MEVATEST100 (100%, 1 use, ends 26 Nov) created for Sara's test order; delete after.
- Live theme is now locked for API writes. Edits go to a copy: "Mëva - PRE-ORDER v2 (edits 24 Nov)" 146306400315 (removed the "Free UK delivery on 2+ jars" and "first-jar guarantee" perk lines). Sara publishes it.

## After Black Friday (Sara, 27 Nov)
- Prices from Tue 1 Dec 00:01 UK: 3 jars £59.98, 5 jars £89.97 (1 jar £24.99 unchanged). Scheduled task "Raise 3/5-jar prices after Black Friday" does the price-list change.
- Theme v8 146455691323 "Mëva - v8 (auto switch after Black Friday)" = live v7 + automatic switch after 30 Nov 23:59 UTC: pack labels Buy 2 Get 1 FREE / Buy 3 Get 2 FREE → Pack of 3 / Pack of 5; announcement → "Free UK delivery on 2+ jars | First-jar guarantee | Vegan & gelatine-free | No subscription"; under-button and cart wording without Black Friday. Sara to publish v8 before 1 Dec. Test copy 146455724091 shows the post-BF state (do not publish).
