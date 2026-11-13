# Mëva Black Friday reservation upgrade — brief (received 13 Nov 2026, NOT built yet)

Status: not started. The Shopify connector was down in the session that received this, so nothing was built, uploaded or tested.
Three points below need the owner's answer before the copy goes live (see "Open questions").

## Owner's brief (verbatim)

TASK: Build the MEVA Black Friday reservation upgrade on the PRODUCT page. Duplicate the live theme first, build there, and send me the preview link. Do NOT publish without my approval. Do not change any price, product copy, or section outside this task. No new apps.

CONTEXT
- Mëva is in waitlist mode: reservations only, "Nothing to pay today", checkout stays closed. This task changes nothing about that.
- The product page /products/meva-magnesium-gummies is the only page to touch, plus the waitlist pop-up headline.
- Current offer: Founding 500 = 20% off first order + free UK delivery on 2+ jars + first-jar guarantee ("Finish your first jar. Not for you? We'll refund it."). Pack prices: 1 jar £24.99 · 2 jars £39.98 · 3 jars £49.99.

THE BLACK FRIDAY UPGRADE (live window: 27 Nov 2026 00:01 – 30 Nov 2026 23:59 UK time)
Anyone who reserves during the window gets the "BF Founding" upgrade on their first order at launch:
1. The 3-jar reservation is presented as "2 jars + your 3rd on us" at the same £49.99 total — a gift frame, not a deeper discount.
2. Free UK delivery on their first order, whichever pack they choose (removes the 2+ jars condition for this group only).
3. Discounts never stack: the 20% Founding discount and pack prices never combine on one order — the customer automatically gets whichever single price is better for her. State this in the small print, worded positively.

BUILD
1. Announcement bar during the window only (date-gate it in the theme; outside the window the current bar returns): "Black Friday · Reserve 2 jars, your 3rd is on us · Ends Monday · Nothing to pay today"
2. A slim module directly under the pack selector, same window-gating: Headline: "Black Friday, the no-drama way." Body: "Reserve the 3-jar pack this weekend and the third jar is on us — £49.99 for three, nothing to pay today. Plus free UK delivery on your first order, whichever pack you pick. Ends Monday night. After that, the third jar is full price." Button: "Reserve mine" (same action as the existing reserve buttons).
3. Small print under the module: "One offer per first order — discounts don't stack, you always get the better price. First-jar guarantee applies: finish it, and if it's not for you, we refund it."
4. Add one FAQ item: "How does the Black Friday upgrade work?" — "Reserve any pack between Friday 27 and Monday 30 November and your reservation carries the upgrade: the 3-jar pack is priced as 2 jars plus one on us, and your first order ships free in the UK whichever pack you choose. Nothing is charged today — we email you when Mëva launches."
5. Pop-up headline during the window: "Black Friday: your 3rd jar is on us" — subline: "Join the No Drama Club this weekend to lock it in."
6. TRACKING (must work, prove it with a test sign-up): a reservation made during the window must save customer tags waitlist + founding-500 + bf-founding, and the chosen pack saved in the customer note (e.g. "Reserved pack: 3 jars"). A reservation outside the window must NOT get the bf-founding tag.

COMPLIANCE — hard rules
- Use ONLY these authorised claims, word-for-word, if any claim appears at all: "Magnesium contributes to the reduction of tiredness and fatigue" / "Magnesium contributes to normal psychological function" / "Magnesium contributes to normal muscle function" / "Magnesium contributes to the maintenance of normal bones" / "Magnesium contributes to normal energy-yielding metabolism". The BF module needs no claim — prefer none.
- Never use: ladies, warrior, journey, anti-ageing, hormone balance, miracle, game-changer, menopause relief, "you should", "don't forget to", or anything about sleep.
- Prices and the guarantee wording stay exactly as they are everywhere else on the page.

REPORT BACK
Preview link, a screenshot of the module on mobile, and proof from a test sign-up that the tags + pack note saved correctly. List anything you could not date-gate automatically.

## Open questions raised with the owner (awaiting her answer)

1. **"Your 3rd is on us" / "After that, the third jar is full price."**
   The 3-jar pack is £49.99 before, during and after the window, and the brief says no price changes. So nothing about the 3-jar price is new during Black Friday, and "after that, the third jar is full price" is not true. Presenting an everyday price as a time-limited gift is the fake-urgency pattern the brand's own rules ban, and it is the kind of claim the UK CAP Code / CMA treat as misleading. Also 2 jars are £39.98, so the third costs £10.01 inside the pack; it is not free.
   What IS new in the window: free UK delivery on a 1-jar first order (worth £4.99).
   Options: (a) lead with the true benefit (free delivery whichever pack) and describe 3 jars honestly ("three for £49.99"); (b) make the 3-jar deal really better in the window (needs a price change, which the brief forbids); (c) keep the gift frame but drop "Ends Monday… after that full price" for the jar and tie the deadline only to free delivery.

2. **"Discounts never stack."**
   The live site says "Founding 500: 20% off your first order" next to pack prices. With no stacking, the 20% only helps 1-jar buyers (£19.99); on 2 jars 20% off £49.98 equals the pack price, on 3 jars the pack price wins. Visitors will expect 20% off £39.98 / £49.99. If non-stacking is the rule, the Founding copy across the site needs to say so, and the FOUNDING20 discount (currently 20% off the order, combinable with shipping) must be reconfigured before launch.

3. **Pack note.** Today the form saves the pack as a tag (`reserve-2`), and the note field only for "something else" answers. The build will write "Reserved pack: N jars" into the note as asked.

## Build notes for whoever implements
- Date-gate in JavaScript using Europe/London time (27 Nov 2026 00:01 to 30 Nov 2026 23:59), not only Liquid: Shopify caches rendered pages, so a Liquid-only gate can switch late. Add a `?bf=1` preview override that works only on unpublished-theme previews so the owner can see it before the 27th.
- The `bf-founding` tag is added client-side in the sign-up form's submit handler (`snippets/meva-club-form.liquid`), inside the same window check.
- Ticker text comes from `sections/header-group.json` → `announcement`; swap it in JS during the window.
- Pop-up headline lives in `snippets/meva-club-form.liquid` (rendered with `fid: 'pop'`); the pop-up wrapper is `snippets/meva-club-pop.liquid`.
- FAQ is in `sections/meva-pdp.liquid` (`.pfaq`).
- Prove tracking with a real sign-up from a normal browser (hCaptcha blocks headless browsers), inside and outside the window.
