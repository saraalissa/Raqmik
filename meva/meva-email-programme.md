# Mëva email programme

Platform: Shopify Email + Shopify Messaging automations (free up to 10,000 emails a month).
Sender: Mëva <info@trymeva.co>. Voice: The Best Friend Who Tells It Straight (see meva-messaging.md). British English.
Rules for this voice: warm, cheeky, always on her side. "Girl" and "Babe" where they land, never in every line. No lectures, no guilt, no "don't forget to".

## Lists (Shopify customer tags)

| Tag | Where it comes from |
|---|---|
| `waitlist`, `founding-500` | No Drama Club form (home, product page, /pages/offer) |
| `reserve-1` / `reserve-2` / `reserve-3` | Pack she reserved |
| `q-3pm`, `q-load`, `q-focus`, `q-me`, `q-other` | "What's draining you most?" |
| `newsletter` | Footer form, The No Drama Letter |

## Compliance rules for every email

1. Product claims: only the authorised wording. "Magnesium contributes to the reduction of tiredness and fatigue." "Magnesium contributes to normal psychological function."
2. Menopause and perimenopause can be written about as editorial (information, stories, NHS links). Never place Mëva as the answer to a menopause symptom. Keep product mentions in their own block, with the authorised claim only.
3. No sleep claims, no "hormone balance", no "relief".
4. Reviews: ask every customer, never only happy ones, never pay for positive ones.
5. Every email has an unsubscribe link (Shopify adds it).

---

## Flow 1: No Drama Club welcome (pre-launch)

Trigger: customer created with tag `waitlist`. Exit: launch day (they move to Flow 2).

### Email 1. Immediately (UPDATED 14 Nov 2026: current offer and guarantee wording)
**Setup:** Shopify Email automation "Welcome new subscribers". Trigger: customer subscribes to email marketing.

**Subject:** You're in. Welcome to the No Drama Club.
**Preview:** Your Founding 500 perks, and what happens next.

Hi there,

You're in. Welcome to the No Drama Club.

You're one of the Founding 500, so here's what's saved for you:

- **20% off a single jar** on your first order. Your code arrives by email the day we launch.
- **Free UK delivery** on 2 or more jars.
- **Our 30-day satisfaction guarantee.** Not for you? We'll refund your first jar. You don't need to finish it or send it back. (First order, one per household. Full terms: trymeva.co/pages/refunds)

Black Friday heads-up: reserve 3 jars between 27 and 30 November and your order ships in the first batch.

What Mëva is, in one breath: two ripe red berry gummies a day, 180mg magnesium, printed on the front. Magnesium contributes to the reduction of tiredness and fatigue.

Nothing to pay today. We'll email you the moment we launch, and a couple of short notes before then. Hit reply any time. A real person reads them.

All dose. No drama.
Mëva

**CTA:** Have a look at the jar → https://trymeva.co/products/meva-magnesium-gummies?utm_source=email&utm_medium=welcome&utm_campaign=welcome_1

### Email 2. Day 2
Subject: What's in the jar (and what isn't)
Preview: Three lines. The third one's our favourite.

Real talk, three lines:

What's in it: 180mg magnesium (citrate) in two berry gummies. 60 gummies, 30 days. Vegan.

What it does: magnesium contributes to the reduction of tiredness and fatigue, and to normal psychological function.

What it won't do: fix your inbox, your teenager or your boss. Sorry, babe. We'd tell you if it could.

We write that third line because the supplement aisle never does. If a label won't tell you how much is inside, ask why.

CTA: Read the full label → /pages/ingredients

### Email 3. Day 5
Subject: Girl, we know you're tired.
Preview: Why we made Mëva (it's not "just your age").

Every woman we spoke to said the same thing in different words. She looks after everyone. Work, kids, parents, the dog. And somewhere along the way, nobody asks how she is.

Then she walks into a pharmacy and forty boxes shout at her. Fear on one shelf, miracles on the next.

We wanted to be the friend in that aisle. The one who grabs your arm and says "not that one". One mineral at a clear dose. Only claims we can prove. A berry gummy you'll actually look forward to.

You hold everyone together. Let someone be straight with you for once.

CTA: Read our story → /pages/our-story

### Email 4. Day 9
Subject: Can we ask you something?
Preview: One line is plenty. We read every reply.

What's draining you most right now?

Hit reply and tell us in your own words. No form, no survey, just you and us. We read every one, and it shapes what we make and what we write about in The No Drama Letter.

(Not in the mood? Totally fine, babe. You'll still hear from us on launch day.)

CTA: none, reply only

---

## Flow 2: Launch (one-off campaigns to `waitlist`)

### Launch day
Subject: It's here, girl. Your 20% is waiting.
Preview: Founding price, free UK delivery on 2+ jars, and our no-drama guarantee on your first jar.

It's launch day and you're first in line, exactly where you should be.

Use code FOUNDING20 for 20% off your first order (use the same email you signed up with). Delivery is free on 2+ jars. Finish your first jar. Not for you? We'll refund it. No forms, no fuss.

The founding price ends Sunday at midnight.

CTA: Claim my founding price → /products/meva-magnesium-gummies?reserve={{ pack }}
Segment tip: send `reserve-3` a version that opens the 3-jar pack.

### Two days later (only to people who haven't ordered)
Subject: Babe, Sunday.
Preview: That's when the founding price ends. That's the whole email.

Quick one, because we know your inbox is a lot. The founding price (20% off, plus free delivery on 2+ jars) ends Sunday at midnight. After that it's the normal price. That's it. Go on.

CTA: Use my 20% → product page

---

## Flow 3: The No Drama Letter (newsletter)

Audience: `newsletter` + `waitlist` + customers who accepted marketing.
Cadence: every other Sunday, 8am UK.
Length: 300 to 450 words, reads in two minutes on a phone.

### Format (same every issue)

1. **Straight talk** (editorial): one midlife topic explained plainly, linking to the NHS or the British Menopause Society. Menopause and perimenopause live here, as information only.
2. **Supplement speak, translated**: one industry phrase in plain English. "Proprietary blend" = "We'd rather not tell you how much."
3. **One small thing**: a four-second habit, a recipe, a walk route, a book.
4. **Her words**: an anonymous reader reply (with permission).
5. **From us** (own block): product news or offer, authorised claim only.

### First four issues

| Issue | Straight talk | Translated | Small thing |
|---|---|---|---|
| 1 | "Perimenopause: what the NHS actually says" | "Clinically inspired" | The 3pm kettle reset |
| 2 | "Talking to your GP: a one-page checklist" | "Hormonal harmony" | A 10-minute walk that counts |
| 3 | "Brain fog at work: what women told us" (no product link) | "Proprietary blend" | Phone-free first ten minutes |
| 4 | "HRT: questions to ask, from people who know" (link to BMS) | "Doctor formulated" | Saying no without a reason |

Subject line examples: "What the NHS actually says about perimenopause (no fluff)" · "Supplement speak, translated: part 2" · "The 3pm kettle reset, babe".
Opening line of every issue: "Hi gorgeous," then straight into it. Sign-off: "Your honest friends at Mëva".

---

## Flow 4: Retention (after launch)

Build in Shopify Messaging: "Thank customers after purchase", "Upsell after first purchase" (set the delay), "Win back customers".

| When | Email | Subject | Job |
|---|---|---|---|
| Day 1 after delivery | How to start | "Babe, put the jar by the kettle" | Put the jar where she'll see it. Habit before results. |
| Day 10 | Check-in | "Real talk: how's it going?" | Reply-based. Catch problems early. |
| Day 21 | Review request | "Would you tell your friends the truth?" | Ask every customer for an honest review. No incentive tied to a good one. |
| Day 24 (1 jar) / 54 (2) / 84 (3) | Refill | "Psst. About six days left in your jar" | Reorder before she runs out. Offer the 2-jar pack (free delivery). |
| Day 28 | Referral | "Know a girl who needs this?" | Give £5, get £5 (needs a referral app later). |
| 45 days after expected run-out | Win-back | "We miss you, babe. Here's 15%, no drama." | One offer, then stop. |

Refill email body:

Psst. You've got about six days left in your jar. If two gummies by the kettle has become your thing, here's the easy way to keep it going.

The 2-jar pack ships free and works out cheaper per day. And the guarantee stands: finish your first jar, and if it's not for you, we'll refund it. No awkward questions.

CTA: Restock in one click → product page (2 jars preselected)

---

## What to measure

| Metric | Target |
|---|---|
| Welcome email open rate | 50%+ |
| Email 4 reply rate | 5%+ (this is research gold) |
| Launch email: waitlist to buyer | 10 to 15% |
| Newsletter open rate | 35%+ |
| Refill email: reorder rate | 25%+ |
| Unsubscribe per send | under 0.5% |
