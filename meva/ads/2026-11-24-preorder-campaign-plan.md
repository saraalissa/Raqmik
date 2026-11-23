# Pre-order SALES test: campaign plan (for Sara's OK, 23 Nov 2026)

## What the past data says (Meta spend ÷ Shopify sign-ups, 14–23 Nov)
| Ad | Spend | Impr. | Link clicks | CTR | CPC | Sign-ups | £ per sign-up | Click → sign-up |
|---|---|---|---|---|---|---|---|---|
| 1.4 no-hunting (test + scale) | £190.31 | 4,230 | 136 | 3.2% | £1.40 | 23 | £8.27 | 17% |
| G3b gummy vs capsule | £96.56 | 1,766 | 55 | 3.1% | £1.76 | 8 | £12.07 | 15% |
| G5 five claims | £15.02 | 174 | 10 | 5.7% | £1.50 | 2 | £7.51 | 20% (tiny sample) |
| 1.1 circled dose | £35.46 | 890 | 23 | 2.6% | £1.54 | 3 | £11.82 | 13% |

Selling is not the same as a free sign-up. A free sign-up converted ~17% of clicks; a paid order from cold traffic usually converts 1–3% of clicks, and a pre-order a bit less. At ~£1.40 a click, £118 buys ~80 clicks → realistic result 1–3 orders. 5+ orders (break-even, ≤ £24 per buyer) would be a strong result.

## Creatives for selling
- **Keep 1.4 (real jar in hand, dose circled).** Best data by far, shows the product. Copy rewritten for buying: price, free delivery, guarantee, no subscription, ship date.
- **Drop G5 for this test.** Text-only claims, no product, only £15 of data. Good for curiosity, weak for paying.
- **Add G3b (gummy vs capsule).** Second-best volume, shows the gummies in a hand, sells the reason to switch. Image button changed to "Pre-order now →". The old first-person copy ("I stopped taking the big capsules") is dropped: with no customers yet it reads like a testimonial.

### Ad 1: PO_1.4_no-hunting
Primary text:
No hunting for the number on Mëva:
✅ 180mg magnesium in 2 berry gummies a day, printed on the front
✅ Magnesium contributes to the reduction of tiredness and fatigue
✅ Vegan, gelatine-free, no subscription

2 jars £39.98 (£19.99 a jar) with free UK delivery. Finish your first jar: if it's not for you, we refund it.

Pre-order now. Our first batch ships by mid-January.
Headline: 180mg, on the front. 2 jars £39.98
Description: Pre-order · free UK delivery on 2 jars
CTA: Order now → product page

### Ad 2: PO_G3b_no-water
Primary text:
Swap the big capsule for two berry gummies. No glass of water, just chew.

180mg magnesium a day, printed on the front. Magnesium contributes to the reduction of tiredness and fatigue.

2 jars £39.98 with free UK delivery · first-jar guarantee · no subscription.

Pre-order now. Our first batch ships by mid-January.
Headline: No water needed. Just chew
Description: Pre-order · free UK delivery on 2 jars
CTA: Order now → product page

## Structure (recommended, Amjad's rule)
Amjad's gate is 2–3× order value per creative (£78–117) and 2–3 days. With £118 in total, only one place can reach that gate. So:
- **1 campaign, 1 ad set, 2 ads (1.4 + G3b), £48/day (~$60), 2 days, spend cap £118.** Meta puts more money behind the ad that sells. We judge the campaign on cost per paid order; per-ad numbers are only a hint.
- Sara's version (2 ad sets × ~$30) also works, but each gets ~£48, half the gate, so neither can be judged alone.

## Audience
- UK, women 45–65, Advantage+ audience OFF, automatic placements (1.4 got sign-ups from Reels and Feed).
- **Exclude people who already know us** (needs 5 minutes in Ads Manager, our tool can't create audiences):
  1. Audiences → Create → Custom audience → Website → all visitors, 180 days → name "Visitors 180d".
  2. Create → Custom audience → Instagram account + Facebook Page → everyone who engaged, 365 days → "Engagers 365d".
  3. Create → Custom audience → Customer list → upload the waitlist CSV from Shopify → "Waitlist".
  Then Claude adds all three as exclusions on the ad set.

## Optimisation and tracking
- Objective Sales, optimise for Purchase (pixel 1647192600272885), 7-day click / 1-day view.
- Before launch: one test order on the pre-order theme to confirm the Purchase event fires. Shopify orders are the truth (UTM campaign = meva_preorder_test).
- Check after ~£50 spend: if there are no add-to-baskets at all, the problem is the page or the price, not the ad. Add-to-baskets but no paid orders → price/pre-order hesitation at checkout.

## Decision line (≈ £95–118 spend)
- 5+ paid orders → sign contracts and continue.
- 2–4 → promising; improve the offer/page and test again.
- 0–1 → stop before signing.

## Status
- Live theme 146150785083 unchanged. Pre-order theme 146296930363 is separate; publish it to start, republish 146150785083 to go back.
- Shipping names reverted to the original (2–3 working days, next-day ON). They are switched to "Pre-order · ships by mid-January" only at go-live, and back after the test.
- Campaign 120247508332000424 built PAUSED with 1.4 and G5. Once Sara approves this plan, Claude swaps G5 → G3b, rewrites the copy as above and moves both into one ad set.
