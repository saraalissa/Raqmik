# Mëva project rules (always apply)

## Product visuals — NON-NEGOTIABLE
- Gummies are GLOSSY, smooth and shiny. NEVER sugar-coated, sugar-dusted, matte, frosted or sandy. (Sara has had to repeat this; do not make her say it again.)
- Shape: cone/pyramid. Colour: deep magenta-purple, translucent. Not round, not red, not bears.
- Every image prompt that shows gummies must say: "glossy, smooth, shiny, wet-look surface, NO sugar coating, no sugar crystals, no dusting".
- Check every generated image at full size for sugar texture before showing Sara. Reject any with sugar.
- Never reuse old sugar-coated assets (e.g. meva6-hand.jpg, meva7-macro.jpg, meva7-hand.jpg, early r1 images).
- Jar: clear glass, SILVER lid, pink-coral label with thin gold borders: "mëva / MAGNESIUM / BERRY GUMMIES / 180mg magnesium · 2 a day / FOOD SUPPLEMENT · 60 GUMMIES".

## Product master image (Sara approved, 18 Nov)
- THE product looks exactly like `meva/assets/product-photos/PRODUCT-MASTER-jar-with-berries.png`: clear glass jar, brushed silver knurled lid, pink-coral label with thin gold lines, 'mëva' in black bold, 'MAGNESIUM / BERRY GUMMIES / 180mg magnesium · 2 a day / FOOD SUPPLEMENT · 60 GUMMIES', full of glossy translucent deep magenta pyramid gummies.
- Higgsfield media id for this master: 46327c51-a76d-4514-8f9e-5758422e4649. Use it as the reference whenever the jar appears. Reject any output whose jar, label or gummies differ.

## Women in imagery — NON-NEGOTIABLE
- Target is women 45–65, so models must look 45–55 mostly: vibrant, stylish, modern. Mix ages from mid-40s upward.
- Do NOT default to elderly / fully silver-haired / grandmother-looking women. Grey streaks are fine; "old lady" is not.
- In every prompt: state an age of 45–52 unless a specific older age is asked for, and describe energetic, fashionable styling.

## Image generation tool — Sara's instruction (updated 24 Nov)
- Do NOT use Soul (`soul_2`) any more (Sara, 24 Nov: "ما تستخدم سول").
- Generate images in Higgsfield with `gpt_image_2_6`. Whenever the jar appears, pass the product master 46327c51-a76d-4514-8f9e-5758422e4649 as a reference; describe the glossy gummies in the prompt.
- Still check label text and gummy gloss at full size before showing Sara.

## Shopify themes workflow (18 Nov)
- LIVE: "Mëva - LIVE" id 146111430715 (published 19 Nov: product page = 16 Nov version, meva-pdp). Writes to live are blocked.
- DRAFT for edits: "Mëva - DRAFT (for edits)" id 146150785083 — exact copy of live. Long PDP archive theme: 146111332411 "ARCHIVE – Long page 18 Nov – DO NOT TOUCH"; long PDP also at ?view=m.
- Theme deletion is blocked for Claude; Sara removes old themes in admin.

## Media buying — Sara's rules (22 Nov)
- Always follow `meva/ads/MEDIA-BUYING-RULES.md` for every test / scale / kill decision: wait for 2–3× AOV spend and 2–3 days; no sale → off and analyse; sale → +30% (not double); 10 profitable sales → duplicate creative into a CBO scaling campaign (1 broad ad set, winners only) and keep it running in testing too.
