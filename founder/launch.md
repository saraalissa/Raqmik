# Mëva launch plan (written 22 Nov 2026)

Target launch: **Tuesday 8 December 2026** (earliest realistic; see the critical path). If the label is not approved in writing by **Fri 4 Dec**, move to **Tue 5 Jan 2027**: do not launch into the Christmas post week (Royal Mail last 2nd class ~18 Dec).
Owners: **Sara** (decisions, payments, signatures, publishing the theme), **Muse** (all emails to suppliers and customers, from info@trymeva.co), **Claude** (theme drafts, ads under Amjad's rules, numbers, checks).

## 1. The test before the big spend
The first batch is the test. Nothing bigger is ordered until it reads.
- **What:** 50 labelled jars, offered first to the waitlist only (Founding 20% off any pack, 7 days, with a real end date).
- **Success line (written before):** **≥ 26% of the waitlist buys within 7 days of launch** (the CFO's break-even at £6 per sign-up). With ~26 orders × 1.9 jars ≈ 50 jars, that also means the first batch sells out. The scarcity is real.
- **Kill / rethink line:** < 10% of the list buys in 7 days → stop cold ads, back to `/founder-offer` and `/founder-pricing`, with the buyers' real reasons (reply-to email + 1-question survey).
- Panel comparison: the simulated panel had 0 buyers and 19/20 "waitlist only". Real buyers decide; trust them over the panel.
- Reorder trigger: when 30 of the 50 jars are sold, order the next batch (Nutribl repeat lead time ~5 working days). Sized on the 7-day sell-through, not on hope.

## 2. Countdown (critical path marked ★)

### Week 1: Sun 23 – Sat 28 Nov
- ★ Flex: decision on Addendum No. 1 → Sara signs and pays £395 → onboarding within 48 h → FBO name and address issued. (Muse chases; Sara signs.) Deadline Wed 25 Nov.
- ★ Nutribl: answers to the 20 Nov email (manufacturer, importer, MOQ, pro-forma for 50 jars, label pre-check) and **sugar grams per 2 gummies** from the label file. (Muse.) Deadline Thu 26 Nov.
- ★ Final label artwork with the FBO line → Flex review → Nutribl approval in writing. (Claude prepares the file, Sara approves, Muse sends.) Deadline Sat 28 Nov.
- Lab test: Nutribl's reports or a quote for one test on lot 27627-226103050. If no result before launch, say "test results coming" on the site, never claim one exists. (Muse.)
- Northstar: written answers to the account terms (BT block, site, SKUs for 1/2/3 jars, Shopify integration). (Muse.)
- Site: Sara publishes the DRAFT theme (email typo check + footer fix). Sara gives the Events Manager count (pixel check).
- Ads: Black Friday week, **no new tests and no budget increases**; hold or trim waitlist budgets under Amjad's rules. Waitlist sign-ups keep coming at ≤ £6.
- Email to the list #1 "What's actually in the jar" (dose on the front, sugar grams, made in Spain / packed in the UK, how the first batch works). Muse sends after Sara approves.

### Week 2: Sun 29 Nov – Sat 5 Dec
- ★ Sara pays Nutribl's pro-forma for 50 jars once the label is approved in writing. Deadline Mon 30 Nov.
- ★ Nutribl labels and transfers stock to Organo at Northstar; Northstar confirms booked-in quantity and lot. Deadline Fri 4 Dec.
- Shopify ready to sell (Claude builds in a new DRAFT, Sara publishes on launch day): buy buttons back on the product page, 1/2/3-jar variants mapped to Northstar SKUs, shipping (GB only, £4.99, free over £29), BT postcodes blocked, guarantee and refund pages, receipts with no VAT line until the VAT number arrives.
- Founding code for the list only: one-use or tag-limited code, 20% off any pack, ends Tue 15 Dec 23:59. No countdown timers that reset.
- Test order end to end (a UK friend or a 100%-discount staff order): checkout → Northstar → delivery → refund path. Deadline Sat 5 Dec.
- Purchase tracking: Meta Purchase event (browser + Conversions API through the Shopify Facebook & Instagram app) checked against a test order. Shopify orders remain the truth.
- Emails #2 (Fri 4 Dec) "Doors open Tuesday: the 60-Day Starter, how Founding works, 50 jars in the first batch" and the launch emails scheduled as drafts.
- Product liability insurance: Sara's decision (she chose to wait). Logged as an open risk; revisit when the first batch sells.

### Week 3: launch week, Sun 6 – Sat 12 Dec
- Mon 7 Dec: Claude final check of the DRAFT on mobile and desktop; stock count at Northstar = 50.
- Tue 8 Dec: launch (run sheet below).
- Tell HMRC if the first sale is before the expected VAT effective date (see meva/ops/DECISION-2026-11-21-sell-before-vat-number.md).

Critical path: **Flex signature → FBO line on the label → Nutribl approval → payment → labelling and transfer to Northstar → test order → launch.** Every other task can slip a few days without moving the date.

## 3. Launch day run sheet: Tue 8 Dec (UK time)
| time | what | who |
| --- | --- | --- |
| 07:30 | Northstar confirms stock and that orders will sync | Muse |
| 08:00 | Sara publishes the sell-ready theme; Claude checks the product page, checkout and code on mobile | Sara, Claude |
| 08:30 | One real test order (then refunded); confirm it reaches Northstar | Sara/Claude |
| 10:00 | Email "Doors are open" to the waitlist: Founding 20% off any pack until Tue 15 Dec, 50 jars in the first batch, 2-jar Starter as "our pick" | Muse |
| 10:15 | Instagram post + story (same message, link in bio) | Sara |
| 11:00 | Waitlist ad campaigns stay on at current budgets (no change on launch day) | Claude |
| 12:00, 16:00, 20:00 | Order check: orders, jars left, Northstar sync, payment errors, customer emails | Claude + Muse |
| 21:00 | Day-1 numbers to Sara in Arabic (orders, % of list, jars left, AOV) | Claude |

If something breaks:
- Checkout or payment fails → Claude pauses all ads at once, Muse emails the list "small delay, back within hours"; fix, test, resume.
- Orders not reaching Northstar → export orders CSV twice a day to Northstar until the sync works.
- Code fails → issue a corrected code to the list the same hour.
- Stock sells out → mark "Sold out, the next batch ships in about 7 days" and keep a back-in-stock list. Never take orders we cannot ship.
- Wrong claim or price found → fix in the theme, note it in the changelog.

## 4. After launch: emails and ads
- List emails: Day 0 doors open · Day 2 "how to take it, what to expect in 30/60 days" (honest: works gradually) · Day 5 "jars left: X" (the real number) · Day 7 "Founding ends tonight". Buyers leave the sequence after they buy.
- Post-purchase: dispatch email · Day 7 "how is the taste?" (the 7-day taste promise) · Day 21 review request (honest, buyers only, no incentive for a positive review) · Day 25 reorder reminder (no subscription).
- **Cold ads switch to Purchase** from Day 3 (Thu 10 Dec), once the Purchase event is verified: a new Sales campaign with the proven creatives (1.4, G5, and others ≤ £6 per sign-up), broad GB women 45–65, **£30/day**. Amjad's rules with AOV = £38.98: wait for **£78–£117 spend and 2–3 days** per creative; no sale → off and analyse; sale → +30% (Sara's OK for every increase); 10 profitable sales → duplicate into the scaling CBO. The Founding code is **not** used in cold ads.
- Waitlist campaigns: trim by 30% after launch week, stop when the Sales campaign beats £23 per new buyer.

## 5. The first 30 days: what to track and when to act
Daily (Shopify is the truth): orders, % of the waitlist that bought, AOV and jars per order, jars left, ad spend and cost per new buyer, refund and taste-promise claims.

| number | target | triggers a change if |
| --- | --- | --- |
| Waitlist → buyer (7 days) | ≥ 26% | < 10% → back to offer/pricing |
| Cost per new buyer (cold ads) | ≤ £23 | > £35 after Amjad's gate → that creative off |
| AOV | ≥ £38.98 | < £32 → push the 2-jar Starter harder on the page |
| Refund + taste claims | ≤ 7.5% | > 10% → check taste, delivery, expectations |
| Reorders by day 30–35 | ≥ 25% of first buyers | < 15% → check the day-25 email, ask buyers why |

Reviews:
- **Day 7 (Tue 15 Dec):** Did ≥ 26% of the list buy? Sold out? What did non-buyers say? Next batch size?
- **Day 14 (Tue 22 Dec):** Cost per new buyer from cold ads vs £23. Which creative sells, not only sign-ups? Any first reviews to publish (real, with permission)?
- **Day 30 (Thu 7 Jan):** Contribution per order from real numbers → re-run `/founder-cfo`. First reorders. Decide: scale, fix or stop.

Next: `/founder-plan` compiles everything into the business plan.
