# Pre-order sales test (Sara, 23 Nov 2026)

Goal: real paid orders are the only signal. Every order is refunded in full the same day with an honest email (first batch not ready). Contracts (Flex, Nutribl, Northstar) are signed only if the test passes.

## What is built (all waiting for Sara)
- Theme **"Mëva - PRE-ORDER TEST (draft)" 146296930363** (copy of live). Sara publishes it.
  - waitlist_mode OFF on product page, home and header → "Add to basket", real checkout.
  - Under the button: "Pre-order: first batch ships by mid-January 2027". FAQ and sticky bar say the same.
  - Every order line carries the property "Pre-order: Ships by mid-January 2027" (shows in cart, checkout, order).
  - Black Friday reserve banner and Club pop-up switched off in this theme only.
  - Preview: https://trymeva.co/products/meva-magnesium-gummies?preview_theme_id=146296930363
- Shipping (live now, harmless while the live theme is in waitlist mode): renamed to "Pre-order · Royal Mail Tracked · ships by mid-January" (£4.99 under £29) and "Pre-order · Free UK delivery · …" (£29+). Next-day option switched OFF.
  - To restore after the test: names "Royal Mail Tracked (2-3 working days)" / "Free UK delivery · Royal Mail Tracked (2-3 working days)", next-day ON.
- Meta campaign **MEVA | PRE-ORDER TEST | Sales | GB W45-65 | 2026-11-24** (120247508332000424), OUTCOME_SALES, PAUSED:
  - Ad set A 120247508332700424: ad PO_1.4_no-hunting (120247508341820424), £24/day (≈ $30).
  - Ad set B 120247508333090424: ad PO_G5_five-claims (120247508342410424), new image with "Pre-order now →", £24/day.
  - Optimisation: pixel 1647192600272885 PURCHASE. Women 45–65, GB. Advantage audience OFF.
  - Copy: "Pre-order now. Our first batch ships by mid-January. Free UK delivery on 2+ jars, and a first-jar guarantee." CTA Order now. UTM campaign=meva_preorder_test.
  - Spend cap £118 (≈ $150) needs Sara's approval token. Run 2 days, then pause.
  - Exclusion of people who already saw us: not possible through our tool (no custom-audience action). Sara can add in Ads Manager: exclude Website visitors 180d + FB/IG engagers 365d (create them under Audiences), or we run without exclusions.

## Go-live order (same hour)
1. Sara publishes theme 146296930363 and does one test order (then refunds it).
2. Claude checks the order arrives and the Meta Purchase event fires.
3. Claude enables campaign + both ad sets + ads (Sara approves the spend token) and sets the £118 spend cap.
4. After 48 h: Claude pauses the campaign. Sara republishes the waitlist theme (146150785083) and Claude restores shipping names.

## Every order: refund the same day (Sara in Shopify admin; Claude cannot issue refunds)
Shopify → Orders → order → Refund → full amount incl. delivery → Restock off → **untick "Send a notification"** (we send our own email) → Refund.
Then tag the customer `preorder-test`, `waitlist`, `founding-500` (Claude can do the tags) and Muse sends the email below.

### Email for Muse (from info@trymeva.co, personal from Sara, same day as the order)
Subject: Your Mëva pre-order: full refund, and you're first in line

Hi {first name},

Thank you for pre-ordering Mëva. You're one of our very first customers, and that means a lot.

Our first batch isn't ready yet, and I don't want to hold your money while we finish it. So I've refunded your order in full today ({amount}). It should be back on your card within 3–5 working days.

You're now first on our list. When the first batch is ready, I'll email you before anyone else, with your Founding price: 20% off.

Thank you for trusting a brand this new.

Sara
Founder, Mëva

## Decision line (written before the test, ≈ £95–118 spend)
- 5+ paid orders → cost per buyer ≤ £19–24: sign contracts and continue.
- 2–4 → borderline: adjust offer/ad and test again.
- 0–1 → stop before signing anything.
