# Mëva (trymeva.co) — session handoff

Last updated: 13 Nov 2026, end of session.
Read this first. It replaces the memory of the previous session. Everything here is on branch `meva-email-voice`.

## Start here (in this order)
1. Check the Shopify connector works: `{themes(first:5){nodes{id name role}}}`. It was down (502) for the last part of the previous session, which is why work is pending. If it is still down, tell Sara to reconnect Shopify under Claude settings → Connectors.
2. Finish the pending upload (next section).
3. Black Friday task: read `black-friday-brief.md`. Do NOT build the copy until Sara answers the two open questions in it. If she has answered in her first message, follow her answer.

## Who and how to work
- **Owner:** Sara (Organo LLC). She writes in Levantine Arabic and expects **short Arabic replies**. All site copy is **British English**.
- **Voice:** the honest best friend with no drama. Mature, not cutesy. "Pinky promise" and sticker-style graphics were rejected.
- She gets frustrated by guesses. If an instruction is ambiguous, ask one short question before building.
- **Her vocabulary:** "landing page" / "اللاندينغ" = the **product page** `/products/meva-magnesium-gummies`, NOT `/pages/why-meva`.
- Always show a preview (mobile 390px + desktop) before anything goes live. She publishes.
- Never expose her personal email, phone or address anywhere customer-facing.
- Never activate Meta ads without her explicit confirmation.

## FIRST JOB: finish the pending upload
See `meva/theme-pending/README.md`. Two changes are saved in `theme-pending/sections/meva-pdp.liquid` and `meva-pdpx.liquid` but are NOT on Shopify (the connector dropped):
1. The 3-stat strip is now its own section `<section class="pstats">` (cream #F8EFE6), directly above "Notes to self".
2. The yellow "Founding 500" box above the pack selector is removed in waitlist mode.

Upload to the unpublished theme, verify, send her screenshots + the preview link.

## Store facts
- Shopify store trymeva.co. Pre-launch **waitlist mode**: "No Drama Club", Founding 500 = 20% off first order (code FOUNDING20), free UK delivery on 2+ jars, first-jar refund guarantee. Nothing is paid today.
- Product: Mëva Magnesium Gummies. 2 a day = 180mg magnesium (48% NRV), 60 per jar, vegan, flavour wording "ripe red berry".
- Prices: 1 jar £24.99 · 2 jars £39.98 · 3 jars £49.99. One-off, no subscription. Do not change prices.
- Delivery: free from £29 (2+ jars), otherwise £4.99.

## Themes (important)
- Two copies exist: **"Mëva - Draft (Claude)"** `145622106171` and **"Copy of Mëva - Draft (Claude)"** `145862000699`. Check which is MAIN with `{themes(first:5){nodes{id name role}}}`.
- The **live (MAIN) theme cannot be written** through the API. Edit the unpublished copy, verify, she clicks Publish. Then sync the other copy so both match.
- At the end of the last session MAIN was "Mëva - Draft (Claude)". The unpublished "Copy of…" already had the cream stats band inside the hero (superseded by the pending files).
- Do not click or suggest the theme "Version 4.5.0 available" update.
- Upload flow: `stagedUploadsCreate` (FILE, POST) → POST file to the staged target (`theme-pending/upp.py`, `upbatch.py`) → `themeFilesUpsert` with body type URL. Upload snippets before the sections that render them.

## Locked structure (her final decisions)
- The product page is the **single conversion page** and the destination for ALL ads.
- `/pages/offer` is unpublished and redirects (301) to the product page. Do not recreate it.
- No new funnels, listicles or landing pages. `/pages/why-meva` and the homepage stay as they are.

## Product page order (after the pending upload)
hero (gallery + buy box) → pban → pfacts → **pstats (new)** → pnotes "Notes to self" → plabel → pjar → pmonth (30 days) → ogap "The food gap" → vs comparison → ppromise → pnote → offer → reviews (hidden until real reviews) → faq → sticky bar.

## Done and live (verify, do not redo)
- Redirect `/pages/offer` → product page.
- Ticker: "30-day first-jar guarantee".
- Main button "Reserve mine" (no price) + "Nothing to pay today"; sticky bar shows pack name + "Nothing to pay today" (no price).
- Header: "Join the club" (→ product page `#club`), basket hidden in waitlist mode (header setting `waitlist_mode`).
- Pop-up: opens after 18s or 50% scroll, never on 404, hidden 3 days after closing, never after joining.
- Mobile hero: full square jar image sized to screen height so H1 + Reserve button are in the first screen.
- "The food gap" section on the product page (her locked copy).
- Microsoft Clarity (project `zcqqw28kt2`) loads only after analytics consent (`snippets/meva-clarity.liquid`). Meta Pixel 1647192600272885 is installed.
- Favicon: salmon circle with "ë".
- "Most popular" replaced by "Our pick" (no customers yet).

## Locked copy
Stats strip, word for word:
- 15% — of UK women aged 19–64 don't reach the minimum magnesium intake from food
- 83% — of the recommended daily intake is the average UK woman's magnesium intake from food
- 180mg — of magnesium in your two gummies — 48% of your daily reference intake
- Source: National Diet and Nutrition Survey 2019–2023, Office for Health Improvement and Disparities & Food Standards Agency (2025).
The source line is mandatory. Figures verified against NDNS 2019–2023 Table 5.41 (15% below LRNI; mean 83% of RNI). "~80%" is superseded.

## Compliance (hard rules)
- Only the 5 GB-authorised magnesium claims, word for word: reduction of tiredness and fatigue; normal psychological function; normal functioning of the nervous system; normal muscle function; maintenance of normal bones.
- No menopause, hormone, sleep, cure/treat language. No timed-result promises.
- No invented reviews, ratings, customer counts, "most popular", fake scarcity.
- Guarantee is first jar of first order only, one per household.

## Open items
1. Pending upload (above).
2. Her real test sign-up from a UK phone: confirm "You're in" message, email arrives, customer appears in Shopify tagged `waitlist, founding-500`. Shopify showed 0 customers; the flow has never been proven end to end.
3. Meta custom conversion "Waitlist sign-up": URL contains `customer_posted=true`.
4. Privacy policy line naming Meta Pixel and Microsoft Clarity (she pastes policies herself; no API permission).
5. Zoho Mail for info@trymeva.co (EU data centre, new account, DNS in Shopify Domains), then set as Shopify sender email.
6. Later: business address, VAT/NETP, GDPR rep, reviews and tracking after first sales.
7. Possible: yellow Founding box also removed outside waitlist mode (ask her).
8. Black Friday upgrade (see section above).

## Black Friday task (not started)
Full brief and build notes: `black-friday-brief.md`. Window: 27 Nov 2026 00:01 to 30 Nov 2026 23:59 UK time.
Two questions were put to Sara and were unanswered when the session ended:
1. The brief says "your 3rd jar is on us… after Monday the third jar is full price", but the 3-jar pack is £49.99 before, during and after, and prices must not change. That deadline claim is untrue and is fake urgency. Recommended: lead with the real new benefit (free UK delivery on any pack, incl. 1 jar) and tie the deadline to that only.
2. "Discounts never stack" means the Founding 20% only helps 1-jar buyers, while the live site says "20% off your first order" next to pack prices. If she confirms no stacking, the Founding copy and the FOUNDING20 discount need changing before launch.
Tracking required by the brief: tags `waitlist, founding-500, bf-founding` inside the window (no `bf-founding` outside), and "Reserved pack: N jars" in the customer note. Prove it with a real sign-up; hCaptcha blocks headless browsers.

## Other files in this folder
- `black-friday-brief.md`: Black Friday brief (verbatim), open questions, build notes.
- `theme-pending/`: theme files waiting to be uploaded, plus the upload helper scripts.
- `cro-audit-2026-11-13.md`: full CRO audit.
- `muse-social-prompt.md`, `meva-email-programme.md`, policy `.txt` files, `TODO-legal-details.md`.
