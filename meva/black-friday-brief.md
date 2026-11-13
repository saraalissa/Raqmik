# Mëva Black Friday reservation offer — brief v2 (received 13 Nov 2026, NOT built)

Status: not started. Shopify connector was down (502) in the session that received this. The brief says "if anything is unclear or a step fails, STOP and tell me", so nothing was built. Three points were raised with Sara and need her answer first (see "Open points").

## Owner's brief v2 (verbatim, supersedes v1 below)

TASK: Add a Black Friday reservation offer to the MEVA product page.
Work ONLY on a duplicated theme. Send me the preview link when done. Publish NOTHING.

THE OFFER (explain it to yourself exactly like this):
"Buy 2 jars, the 3rd is on us." The customer reserves 3 jars and pays the 2-jar value: £49.99 total — this is the SAME price as the existing 3-jar pack. Do NOT change any price. Only the framing changes.
Plus: free UK delivery on her first order, whichever pack she picks.
It is a reservation only — nothing to pay today.

WHEN: The offer shows only between 27 Nov 2026 00:01 and 30 Nov 2026 23:59 UK time. Before and after those dates, the site looks exactly as it does now. Use a simple date check; do not build a scheduling system.

MAKE THESE EDITS, ALL OF THEM, NOTHING ELSE:
1. Announcement bar, only during the window: "Black Friday: buy 2 jars, the 3rd is on us — reserve by Monday."
2. On /products/meva-magnesium-gummies, under the pack selector, add one slim module, only during the window: "Black Friday reservation: pick the 3-jar pack and your 3rd jar is on us. Free UK delivery on your first order. Nothing to pay today."
3. In the pack selector, during the window only, the 3-jar option gets a small tag: "3rd jar on us". Prices and all other labels stay identical.
4. Add ONE FAQ item, only during the window: Q: "How does the Black Friday offer work?" A: "Reserve the 3-jar pack during Black Friday and your 3rd jar is on us — you pay £49.99. You also get free UK delivery on your first order. Nothing to pay today; we email you when Mëva launches."
5. Pop-up headline, during the window only: "Black Friday: your 3rd jar is on us." (Body of the pop-up unchanged.)
6. Tagging: sign-ups during the window must save the tags waitlist, founding-500 AND bf-founding, with the chosen pack in the customer note, same as the existing sign-up flow already does for the other tags.
7. Discount rule to state in the module (small line under it): "One best price applies — offers don't stack." Do NOT create any discount code for this. The Founding 500 20% and this offer never combine; the customer simply gets the better single price.

HARD RULES:
- No price changes anywhere. No checkout — it stays closed, "Nothing to pay today" stays true everywhere.
- No health claims in anything you add. Use the copy above word for word.
- Banned words: "you should", "don't forget to", "ladies", "warrior", "journey", "anti-ageing", "hormone balance", "miracle", "game-changer", "menopause relief", and anything about sleep.
- Do not touch any other page, the food-gap section, or the stat strip.
- If anything is unclear or a step fails, STOP and tell me — do not invent a workaround.

WHEN DONE, REPORT BACK:
- The preview link.
- A test sign-up done inside the window dates showing the customer saved with tags waitlist + founding-500 + bf-founding and the pack in the note.
- Confirmation that with a date outside the window, none of the BF elements appear.

## Open points raised with Sara on v2 (awaiting her answer)

1. **Free delivery on any pack contradicts her rule from the same day**: "the 1-jar pack always pays delivery". Which one stands? If 1 jar pays delivery, the module/FAQ line must read "Free UK delivery on 2+ jars" (which is already true for everyone).
2. **"Buy 2 jars, the 3rd is on us" vs the 2-jar pack at £39.98.** On the same selector, 2 jars cost £39.98 and 3 cost £49.99, so the third jar costs £10.01. "2-jar value £49.99" only holds against two single jars (2 × £24.99). And the £49.99 price is the same before, during and after the window, so "reserve by Monday" presents an everyday price as a deadline offer (fake urgency; CAP Code risk; against the brand's own no-fake-scarcity rule). Honest alternatives that cost nothing: "3 jars for the price of 2 single jars" without a deadline on the price, or a real time-limited extra (founders' prize draw, first-dispatch priority).
3. **Pack in the note.** The current flow saves the pack as a tag (`reserve-N`), not in the note. The build will add "Reserved pack: N jars" to the note; say so in the report.

Also note for the build: hCaptcha blocks headless browsers, so the "test sign-up inside the window" must be done from a real browser (Sara's phone) using a preview override, or by temporarily widening the window on the unpublished theme. Shopify shows 0 customers, so the sign-up flow itself has never been proven.

---

# (superseded) Brief v1

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
