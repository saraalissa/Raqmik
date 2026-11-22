---
name: amjad-meta-ads
description: Amjad's Meta ads media-buying decision system (Sara's chosen rules). Use for EVERY Meta ads decision on Mëva - when to wait, turn off, raise or lower a budget, and when to move a creative into the scaling campaign. Triggers - "شو نعمل بالإعلانات", kill/keep/scale, budget up/down, scaling campaign, testing campaign, "طبّق قاعدة أمجد".
---

# Amjad's Meta ads rules

Source: Amjad's training video (flowchart "START HERE: Did the ad spend 2x AOV?"), given by Sara on 22 Nov 2026. These rules override generic scaling advice (e.g. the ads skill's +20% / 2-week rules) whenever they conflict.

## Campaign structure
- **Testing campaign: ABO.** Each test has its own ad set budget.
- **Scaling campaign: CBO**, ONE ad set, broad targeting (only who / where / age: women, GB, 45-65), only winning creatives. Budget higher than tests (Amjad: from 500; can start 100-200, i.e. whatever the budget allows).

## Decision flow for every test
1. **Did the ad spend 2-3x AOV?** (Amjad prefers 3x.) It must also have run **at least 2-3 days**.
   - No -> leave it running. No decision yet.
   - Exception: something clearly abnormal (CPC far above the other tests) -> turn off early.
2. **Yes -> did it get a sale?**
   - No -> **turn it off and analyse**: was the CPC good or bad? Was the hook (first second) good or bad? Test new versions.
   - Yes -> **raise the budget +30%** (not double). Leave it 1-2 days.
3. **Did the ad get more profitable sales?**
   - No -> after about 2 days return to the original budget, or turn the test off if the numbers are very bad.
   - Yes -> **+30% again**, every day or every 2 days, as long as it keeps working.
   - The day after a raise is often weaker (ROAS dips). Give the ad 2-3 days to adapt; only react faster if performance is very bad.
4. **After about a week: did it generate at least 10 profitable sales?**
   - Yes -> **duplicate the winning creative into the scaling campaign.** Do NOT turn it off in testing; keep raising it there too (+30%). If both work, keep both.
   - No -> wait until it reaches 10, or lower the budget, or turn it off, depending on ROAS / cost per result.
5. Keep launching new tests in the testing campaign all the time: more winners = more creatives in the scaling CBO = more money.

## Mëva waitlist translation (until paid sales start)
- "sale" = a Shopify waitlist sign-up (customer tag `ad-*`). Shopify is the source of truth; the Meta pixel under-counts.
- "AOV" during the waitlist = target cost per sign-up (£6, Sara 21 Nov). So the spend gate is 3 x £6 = **£18** and 2-3 days. "profitable sale" = sign-up at ≤ £6. Judge on clean days only (from 20 Nov, after the 16-Nov PDP was restored).
- After launch (paid sales): AOV = real average order value (~£40), spend gate 2-3x AOV (£80-120), profitable = cost per purchase below profit per order.

## Guardrails (Sara's standing rules)
- Budget increases and new spend need Sara's OK (Windsor confirmation token). Pauses and decreases follow the rules above.
- Log every change in `meva/ads/changelog.md`.
- Creatives: glossy gummies only, real 250ml jar size, women 40-55 natural, GB-authorised claims only.

## The flowchart (flowchart.png in this folder)
START HERE → **Did the ad spend 2x AOV?**
- NO → Let the ad spend 2x AOV.
- YES → **Did it get a sale?**
  - NO → Turn it off and analyse.
  - YES → Double the budget (in the video Amjad recommends starting with **+30%**, not more — we use +30%).
    → **Did the ad get more profitable sales?**
      - NO → Slow down spend.
      - YES → Scale budget by 30% daily.
        → **Did the ad generate at least 10 profitable sales?**
          - NO → Let it spend until it reaches 10 sales. If not, turn it off or keep it at a low budget based on ROAS.
          - YES → Duplicate it to the scaling campaign.

## Video 2: why scaling breaks, and the 4 questions (Sara, 22 Nov; transcript partly received)
Recap of the test rules:
- Start each test ad set at **$25–50 a day**. Leave it 2–3 days, until it spends 2–3x AOV. Do not touch it.
- Early kill: only if CPC is far above normal (e.g. usual CPC $1, this test $3) → after about 1.5 days, turn it off if it has no sales.
- After 2–3 days, review. Not profitable / no sales → turn off and analyse:
  - low hook rate → fix the hook (stronger first seconds);
  - high CPC → the angle is probably wrong → new angle, new test.
- Profitable → +30% (safe way; doubling is possible but riskier). Wait 2 days. Still profitable → +30% again. Results dipped but still profitable → don't raise, wait 2 more days. Not profitable (e.g. ROAS 0.9) → turn the test off. Continue to about day 7, ask again: profitable → +30% and duplicate into the CBO scaling campaign (keep the test running in the ABO testing campaign).

The scenario that happens to 95% of people: day 1–3 ROAS 2.3 → raise 30% → next day ROAS 1.4–1.7 → raise again → ROAS 0.9 → turn off.
- A ROAS dip the day after a raise is NORMAL. Wait another day before deciding.
- Why it happens: more budget = Meta shows the ad to more, less-ready people and you enter the auction against big competitors → CPA rises. If AOV stays the same, margin disappears.

The 4 questions Amjad asks before any decision (especially in this scenario):
1. **Is the AOV high enough to scale?** Products at $30–40 AOV usually cannot stay profitable when scaling, because CPA rises with spend. Aim for AOV of at least ~$50–70 (bundles, multi-packs, upsells). Example: AOV $35: $25/day → CPA $17, 2 sales, ROAS 2.2; $50/day → CPA $24, ROAS 1.7; $100/day → CPA $40, ROAS 1.4. The one thing that never changed was the AOV.
2–4. (not received yet — add when Sara sends the rest of the video)

### What this means for Mëva
- Prices: 1 jar £24.99, 2 jars £39.98, 3 jars £49.98 → AOV is in Amjad's danger zone if most buyers take 1 jar. Before paid-sales scaling: push the 2- and 3-jar packs (default the selector to 2 jars, free delivery from 2, founders' perks on multi-packs) to lift AOV towards £45–50+.
- Waitlist stage: tests at £10/day are below Amjad's $25–50 start; acceptable because the "AOV" here is the £6 target cost per sign-up, but note it.
