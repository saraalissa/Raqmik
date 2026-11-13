# Mëva: response to the strategic guide (13 Nov 2026)

This responds to "MËVA — التوجيه الاستراتيجي والتنفيذي لكلود" (strategic and execution guidance for Claude).

Sources checked:
- The current theme files in `theme-pending/`, which match the live theme.
- Shopify data from this session.
- The CRO audit of 13 Nov.

Nothing has changed on the site. The product hold is still in force, so this plan touches the theme (copy and layout) only.

---

## أ) Understanding

**Product**
- One product: Mëva Magnesium Gummies, ripe red berry flavour.
- 2 gummies a day, 90mg per gummy (180mg per day, 48% NRV), 60 per jar, so one jar lasts 30 days.
- Vegan.

**Market**
- UK only. Prices in GBP, including VAT.
- Women aged roughly 45–60. This is a marketing choice. The product is not a menopause product, and the site must not say or imply that it is.

**Stage: pre-launch waitlist (the "No Drama Club")**
- Sign-up is a Shopify customer form. It collects an email address plus an optional pack choice and an optional question.
- No payment is taken.
- Black Friday (27–30 Nov) is built and hidden until those dates. It gives first-batch shipping priority only.

**Prices**

| Pack | Price | Per jar | Per day | Delivery |
|---|---|---|---|---|
| 1 jar | £24.99 | £24.99 | £0.83 | £4.99 |
| 2 jars | £39.98 | £19.99 | £0.67 | Free |
| 3 jars | £49.98 | £16.66 | £0.56 | Free |

All orders are one-off. There is no subscription.

**What is working**
- A clear personality.
- Authorised claims, word for word.
- An NDNS statistic with its source.
- The hero is clear on mobile.
- "Nothing to pay today".
- Clarity analytics loads only after consent.
- The sign-up has been proven end to end.

**The real gap**
- The visitor understands the personality before she understands what the product is.
- The trust evidence relies on wording, not documents: GMP, origin and elemental dose are all unproven.
- The word "Reserve" is used for an email-only waitlist.

---

## ب) Conflicts and items to confirm

These only change the promise, price, operations or product accuracy. Everything else can go ahead.

| # | Item | Why it matters | What I need from you |
|---|---|---|---|
| 1 | **Is 180mg elemental magnesium?** The Nutribl spec says "magnesium citrate 90mg per gummy". | If 90mg is the weight of the citrate compound, the elemental dose is much lower, and both the dose and the 48% NRV figure would be wrong everywhere. **This is the most serious item.** | The supplier's spec sheet or label showing "of which magnesium (elemental)". |
| 2 | **Sugar per serving** | Sugar is the first ingredient listed, and there is an FAQ question about sugar. | The nutrition panel: grams of sugar per 2 gummies. |
| 3 | **Manufacturing origin.** `/pages/why-meva` says "Made in Spain… packed in the UK"; the other pages say "packed in the UK". The "GMP standards" wording appears 5 times. | Wording without documents is a trust risk. | A GMP certificate from the manufacturer, or permission to soften the wording. |
| 4 | **The word "Reserve" plus the pack choice.** Nothing is held for the customer: only an email and a preference are saved. | The guide asks for "Reserve" to be avoided unless something is genuinely held. Your Black Friday copy ("reserve by Monday") uses it. | Choose: (a) keep "Reserve" and define it ("we hold your place in the first batch") **only if** first-batch priority will really be honoured in order of sign-up; or (b) change to "Join the waitlist" or "Save my 20%". |
| 5 | **20% for the Founding 500 vs the no-stacking rule** | The code FOUNDING20 is currently set to combine with the multipacks, which contradicts "offers don't stack". | Choose one: 20% off the 1 jar only; or 20% off any order, with the 2- and 3-jar packs at full price instead of their discount. |
| 6 | **How the first 500 are counted** | There is no technical limit in Shopify. | Is it the first 500 with the `founding-500` tag? What happens to sign-up number 501? |
| 7 | **"Ships in the first December batch"** (in the Black Friday copy) | This is an operational promise. | Is there a confirmed date for stock arriving in December? |
| 8 | **Guarantee window.** Currently "30 days from the order arriving", but the jar lasts exactly 30 days, so a customer who finishes the jar may already be out of time. | The window is too tight. This is a business decision. | Choose: (a) extend to 45 days from delivery; or (b) keep 30 days and say "contact us any time in the first 30 days, you don't need to finish the jar". |
| 9 | **Subscription later?** "Never. Every order is a one-off." appears twice. | It contradicts any future subscription plan. | If a subscription is possible, change it to: "Right now every order is a one-off. Nothing renews." |

---

## ج) Change table

The P0 items marked ⏸ wait for the matching answer in ب. Everything else is independent of those answers.

| Priority | Current | Proposed | Reason | How to verify |
|---|---|---|---|---|
| P0 ⏸1 | "180mg / 48% NRV" everywhere | Keep it if elemental is confirmed; otherwise correct it everywhere at once, including images. | Product accuracy | Compare the spec sheet with the text on all 3 pages and in the images. |
| P0 ⏸4 | Button "Reserve mine" | "Join the waitlist" plus a line under it: "Pick your pack now. Pay nothing today." (or keep "Reserve" with a definition) | Honesty about what the form does | Check the button text on the page and the sticky bar; run a sign-up and confirm the success message. |
| P0 ⏸5 | "20% off your first order" with no conditions shown | One clear sentence of conditions next to the offer | Prevents disputes at launch | Test FOUNDING20 in a test cart on each pack. |
| P0 ⏸8 | Guarantee wording in several places | One identical wording everywhere (see د) | Consistency | Search all pages for "guarantee": only one wording should appear. |
| P0 ⏸3 | "Made to GMP standards" ×5; "Made in Spain" on why-meva | Until the document arrives: "Made by a specialist supplement manufacturer in Spain. Packed in the UK." Remove GMP. | No claim without a document | The text scan finds no GMP without a document. |
| P1 | Hero: eyebrow "For the women who hold everyone together", then "Tired of being tired? Same, babe." | Eyebrow "Magnesium berry gummies" + headline A/B + dose line + one authorised claim (see د) | The product type is clear in the first second | 390px screenshot: eyebrow, H1, dose line and button all in the first screen. |
| P1 | "Six things. No secrets." / "Meet the cast" mixes ingredients and attributes | "What's in the jar": (1) the active ingredient, (2) the full ingredients list, (3) separately: "vegan · gelatine-free · no artificial colours" (only what the label supports) | Separates ingredients from features | Compare against the label word for word. |
| P1 | Comparison table "Mëva vs the usual wellness hype" including "Balances your hormones" | Replace it with "Why Mëva" (4 specific reasons, each with its evidence), or an objective table with no hormone wording | No vague attacks; no hormone wording | Text scan for "hormone" returns 0. |
| P1 | The optional "What's draining you" question in the first step | Email only in the first step; move the question to the success screen | Less friction | Clarity: form starts vs successful sign-ups. |
| P1 | Success message | A clear message: what happens next, when, and how the 20% is received (see د) | Manages expectations | One real sign-up from your phone. |
| P1 | Repeated "No drama", "babe" and "girl" | Keep one or two per page at most, in the headlines; remove them from price, ingredients and FAQ text | Clarity before jokes | Count occurrences per page. |
| P1 | Packs | Show the total, per jar and per day on each card; keep "Best value" on 3 jars (it is mathematically true: £16.66 per jar) | No mental maths for the visitor | Check that the numbers update when switching packs. |
| P2 | Single headline | A/B test A against B with only the headline changing | Learn with evidence | No winner declared before about 300 sign-ups or 2 weeks. |
| P2 | Images | Real video: opening the jar, two gummies in the hand, the back label readable and zoomable | Visual proof | The label is readable at 390px. |
| P2 | Tracking | UTMs on every ad; a "Waitlist sign-up" custom conversion (`customer_posted=true`); no email or answers in URLs or events | Clean measurement | Events Manager shows the conversion from one test. |

---

## د) British English copy (ready to use)

### Hero, version A (emotional + descriptor)
- **Eyebrow:** Magnesium berry gummies
- **H1:** Tired of being tired? Same, babe.
- **Dose line:** Two ripe red berry gummies a day. 180mg magnesium, 48% of your daily reference intake. One jar lasts 30 days.
- **Claim:** Magnesium contributes to the reduction of tiredness and fatigue.
- **Button:** Join the waitlist: 20% off
- **Under the button:** Launching soon · Nothing to pay today · Just your email

### Hero, version B (direct + warm)
- **Eyebrow:** Magnesium berry gummies
- **H1:** Your daily magnesium, in two berry gummies.
- **Subline:** A ten-second habit that actually tastes nice. No pills to swallow, no powders to stir.
- Dose line, claim, button and the line under the button stay the same as version A.

### Pack line (under the cards)
Pick your pack now so we know what to make. It's not an order, and you pay nothing today.

### Offer (once ب5 is answered; option shown: 20% off the single jar only)
Founding 500: 20% off a single jar on your first order, or choose a multipack at its own lower price. One offer per order; they don't stack. One per person.

### Success message
- **Headline:** You're in.
- **Body:** We'll email you the moment Mëva launches, with your Founding 500 code. Nothing to pay today, and you can unsubscribe whenever you like.
- **Optional question:** While you're here: what's draining you most right now? (Optional, and it helps us write emails worth opening.)

### "What's in the jar" section (replaces "Meet the cast")
- **H2:** What's in the jar.
- **Intro:** One active ingredient, a short list of everything else.
- **Active:** Magnesium citrate. 90mg of magnesium per gummy, 180mg in your two a day (48% NRV).
- **Full ingredients:** [copied word for word from the final label]
- **Separate line (features):** Vegan · Gelatine-free · [only what the label supports]

### "Why Mëva" (replaces the hype table)
1. **The dose is on the front.** 180mg magnesium per day, printed where you can see it.
2. **Two gummies, done.** No pills to swallow, no powder, no water.
3. **It tastes like ripe red berries.** You'll look forward to it.
4. **Your first jar is on us if it's not for you.** [the agreed guarantee wording]

### Guarantee (one wording, option 8b)
**Try your first jar risk-free.** If Mëva isn't for you, email us within 30 days of your first order arriving. You don't need to finish the jar or send it back. We'll refund the jar you opened. First order only, one per household.

### Origin (until the GMP document arrives)
Made by a specialist supplement manufacturer in Spain. Packed in the UK.

### Subscription (if a subscription is possible later)
Right now every order is a one-off. Nothing renews, nothing to cancel.

---

## هـ) Layout plan

### Product page (the single conversion page for ads)

**1. Hero.** The jar image, then:
- eyebrow, H1, dose line and claim
- pack selector showing total, per jar and per day
- button, with "Nothing to pay today" next to it
- on mobile: everything up to the button sits in the first screen, with the sticky bar below

**2. pfacts.** Four quick facts: dose, 2 a day, 30 days, taste.

**3. pstats** (locked).

**4. Why Mëva** (new, replaces vs).

**5. What's in the jar.** Active ingredient, full ingredients, then the features. Back-label image, zoomable.

**6. The 30 days.** The routine, not results.

**7. The food gap** (locked).

**8. Guarantee** (one wording).

**9. The offer.** Its conditions sit next to it.

**10. FAQ.** Order: sugar, medication, allergens, guarantee, delivery.

**11. Final CTA.**

Removed from this page: the vs table and the pnote section, if it repeats content. "Notes to self" stays only if it adds something new; otherwise merge it into Why Mëva.

### Homepage

1. Hero (same pattern as above).
2. Three different points: the authorised claim, ease of use, taste.
3. Real video.
4. Why Mëva.
5. Ingredients and label.
6. Packs.
7. Guarantee and FAQ.
8. One final CTA.

The homepage should be shorter than today: about 17,000px tall on mobile, which repeats the product page.

### Mobile rules
- No headline cut off.
- The sticky bar must not cover the form.
- The email keyboard opens (`type=email`, `autocomplete=email`).
- Text on images is at least 14px.
- Test at 390px and 360px before publishing.

---

## و) Implementation

Not done yet. Once you approve:

**Without waiting for your answers** (on the unpublished theme `145622106171`, with a preview):
- the hero eyebrow and dose line
- "What's in the jar"
- "Why Mëva" in place of the table
- removing "hormones"
- the success message
- reducing "No drama" and "babe"

**After your answers in ب:** dose, button wording, offer conditions, guarantee and origin.

No product edits. The product hold still applies.

---

## ز) Decision log

| Date | Decision | Reason / evidence | Assumptions |
|---|---|---|---|
| 13 Nov 2026 | The product page is the single page for ads | CRO audit; /pages/offer redirected | — |
| 13 Nov 2026 | 3 jars at £49.98 | "3 for the price of 2" is literally true | — |
| 13 Nov 2026 | No discount stacking; 1 jar always pays delivery | Profit: about £16 per 1-jar order before ads | Cost estimates (£4.16 per jar, fulfilment £4.84–£5.65) |
| 13 Nov 2026 | Black Friday = first-batch shipping priority only | No fake urgency | December stock date not confirmed (ب7) |
| 13 Nov 2026 | "Our pick" instead of "Most popular"; "Best value" for 3 jars | No sales data; per-jar price is the lowest | — |
| 13 Nov 2026 | Clarity only after consent; no personal data in events | UK GDPR | — |
| 13 Nov 2026 | Proposed: eyebrow "Magnesium berry gummies" + A/B headline test | Guide §7; the product type is not clear in the first second | Needs enough traffic before judging |
| 13 Nov 2026 | Proposed: replace the vs table with "Why Mëva" | Guide §14; hormone wording | — |
| Pending | 180mg elemental, sugar, GMP, Reserve, 20%, guarantee, subscription | See ب | — |

## Update (13 Nov, evening): items confirmed from the Nutribl certificate of conformity

Source: `CoC-PL-541-27627-226103050`, attached to Nutribl's email of 6 Nov in Gmail.

- **Item 1, dose: confirmed.** "Magnesium (Magnesium citrate) 90 mg per gummy, 24% NRV". That is elemental magnesium. 2 gummies = 180mg = 48% NRV, so the site's figures are correct.
- **Item 3, origin and GMP: confirmed.**
  - Country of manufacture: Spain. Country of packing: United Kingdom.
  - "Manufactured under Good Manufacturing Practice by an approved manufacturing partner", audited under Nutribl's BRCGS-certificated supplier approval system.
  - The site now says this accurately.
- **Allergens:** "None of the 14 major allergens are used as ingredients". Vegan: yes.
- **Item 2, sugar: still open.** The certificate has no nutrition panel. Ask Nutribl for sugar and kcal per 2 gummies. Unit weight is 3g.
