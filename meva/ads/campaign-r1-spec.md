# Meta campaign R1: ready to build (on hold, waiting for Sara's go-ahead)

## IDs
- Ad account: 1007509492392852 (MEVA UK)
- Pixel: 1647192600272885
- Custom conversion "Waitlist sign-up": 1385882766748326
- Facebook page: MEVA (61596592942162)
- Instagram: @trymeva.co (business account, linked to the page)

## Campaign
- Name: "MEVA | Waitlist R1 | UK W45+ | <launch date YYYY-MM-DD>" (date = the day Sara switches it on; set before first publish because utm_campaign takes the name at publish)
- Objective: OUTCOME_LEADS
- Budget: campaign level (CBO), £25/day
- Status: PAUSED

## Ad sets (3, one per angle)
- Ad sets: A Transparency · B Tiredness · C Offer
- Optimisation: OFFSITE_CONVERSIONS
- Promoted object: pixel 1647192600272885 + custom conversion 1385882766748326
- Targeting: GB, women, age 45–65+
- Advantage+ audience: off

## Ads (15)
- Images: feed JPGs. Their public URLs are in `2026-11-13/_image-urls.json`.
- Link: `https://trymeva.co/products/meva-magnesium-gummies`
- URL parameters (url_tags on every ad): `utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&placement={{placement}}`
- Ad names: `A1_search-dose`, `A2_check-bottle`, `A3_simplified`, `A4_circled-dose`, `A5_whole-routine`, `B1_3pm-empty`, `B2_15pct`, `B3_stuck-at-83`, `B4_todo-4sec`, `B5_tired-same`, `C1_056-a-day`, `C2_breakup`, `C3_meva-maths`, `C4_receipt`, `C5_founding-member`
- Headline: "Join free: 20% off your first jar"
- Description: "Nothing to pay today"
- CTA: SIGN_UP
- Primary text: the hook line from `2026-11-13-angles.md`, then this body:

  > Mëva is two ripe red berry gummies a day with 180mg magnesium. Magnesium contributes to the reduction of tiredness and fatigue.
  > Join the No Drama Club for free. The first 500 get 20% off a single jar. Nothing to pay today.

## Before going live
- Sara publishes the theme.
- She approves the campaign build.

## No Advantage+ anything (Sara, 13 Nov)
- **Budget:** no Advantage campaign budget (CBO). Use ad set budgets (ABO), £10/day each × 3 = £30/day.
- **Audience:** Advantage+ audience off. Original audience options only (GB, women, 45–65+).
- **Placements:** manual, not Advantage+ placements:
  - Facebook Feed
  - Instagram Feed
  - Instagram Stories
  - Facebook Stories
  - Instagram Reels
  - Facebook Reels
- **Creative:** every Advantage+ creative enhancement OPT_OUT via `degrees_of_freedom_spec` on each ad. That covers:
  - text improvements
  - image touch-ups, image brightness and contrast, image templates and expansion
  - music
  - 3D animation
  - adding site links and catalogue items
  - comments
- **Targeting expansion:** off. No detailed-targeting expansion and no lookalike expansion.

## Temporary images (Sara, 13 Nov)
These are approved for now. Swap them for real product photography when the official photos/samples arrive from the source (Nutribl).

| Ad | Image source | When the real photos arrive |
|---|---|---|
| A2 | AI-generated (plain bottle next to the jar) | Replace |
| A4 | AI-generated (hand holding the jar) | Replace |
| B1 | AI-generated (tired woman) | Replace the jar in shot |
| A1, A3, B3, C3, C5 | Existing jar render or cut-out | Replace |
| A5, C1 | Sara's / site product images | Keep unless the label changes |

## Build status (13 Nov)
- **Campaign** 120247371770060424, PAUSED.
- **Ad sets**, all PAUSED, £10/day each:
  - A 120247371770800424
  - B 120247371772150424
  - C 120247371772570424
- **Promoted object:** `{"custom_conversion_id":"1385882766748326"}`. Passing the pixel_id together with it was rejected as an invalid combination.
- **Ads:** not created yet. Meta returned "Facebook Page is Missing": the Windsor token has no access to Page 61596592942162. Sara needs to reconnect Windsor and select the MEVA Page and @trymeva.co.
- **Ad payloads:** asset_feed_spec with 3 bodies and 3 titles, built in the scratchpad.
- **Tracking:** `utm_campaign` is static (`meva_waitlist_r1`), so the campaign name, with its date, can be changed at launch.

## BUILT (13 Nov, night). Everything PAUSED, nothing spending
- **Page:** 1368462283024523. The old ID, 61596592942162, was wrong.
- **Instagram:** 17841479804583743
- **Images:** hosted on Shopify Files (`cdn.shopify.com/.../files/meva-ad-<ID>-feed.jpg` and `-story.jpg`). Meta could not fetch the earlier image URLs.
- **Each ad has:**
  - 4:5 for FB/IG feed, 9:16 for stories and reels (placement asset customisation)
  - every Advantage+ creative enhancement OPT_OUT
  - URL tags on
- **Multiple text options are not allowed together with placement customisation.** So each ad has one primary text and one headline, and the 3 texts are spread across the 5 ads in each ad set.

### Ad IDs
| Ad set | Ad | ID |
|---|---|---|
| A | A1 | 120247372197020424 |
| A | A2 | 120247372202020424 |
| A | A3 | 120247372203030424 |
| A | A4 | 120247372204620424 |
| A | A5 | 120247372205770424 |
| B | B1 | 120247372209760424 |
| B | B2 | 120247372210970424 |
| B | B3 | 120247372212290424 |
| B | B4 | 120247372217040424 |
| B | B5 | 120247372219100424 |
| C | C1 | 120247372229340424 |
| C | C2 | 120247372233750424 |
| C | C3 | 120247372237970424 |
| C | C4 | 120247372246730424 |
| C | C5 | 120247372256370424 |

### To launch
1. Rename the campaign with the launch date.
2. Enable the campaign, the 3 ad sets and the 15 ads, only on Sara's explicit go-ahead.

## LIVE (13 Nov 2026, late evening): Sara approved "شغلها هلأ" ("switch it on now") with £25/day split equally
- **Ad set budgets:** £8.33/day each (833 pence × 3 = £24.99/day).
- **Status:** the campaign, all 3 ad sets and all 15 ads are ENABLED.
- **Campaign name:** "MEVA | Waitlist R1 | UK W45+ | 2026-11-13".
- **Review plan:**
  - Meta ad review usually takes from a few hours up to 24h.
  - Judge after ≥1,000 impressions per ad.
  - First proper read at day 5–7.
