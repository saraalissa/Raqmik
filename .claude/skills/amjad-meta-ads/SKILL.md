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
