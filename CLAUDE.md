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

## Image generation tool — Sara's instruction
- Generate ALL images in Higgsfield with model `soul_2` (Higgsfield Soul 2.0), quality 2k.
- soul_2 accepts ONE reference image: use the real jar (media 32c23d56-d26d-4e03-b5d4-e8b77bb7008f) whenever the jar appears; describe the glossy gummies in the prompt.
- Still check label text and gummy gloss at full size before showing Sara.
- Soul 2.0 cannot draw the jar correctly. Proven workflow (18 Nov): 1) make the scene/woman in soul_2; 2) swap in the real jar with gpt_image_2_6 using [scene, product master 46327c51-a76d-4514-8f9e-5758422e4649] as references, keeping the woman and pose identical.

## Shopify themes workflow (18 Nov)
- LIVE: "Mëva - LIVE" id 146111332411. Writes to live are blocked. (Old themes DELETE ME 1–3 were deleted 19 Nov; no rollback theme exists.)
- DRAFT for edits: "Mëva - DRAFT (for edits)" id 146111430715 — an exact copy of live. Make all changes here, show Sara, she publishes. After she publishes, duplicate the new live as the next DRAFT so live and draft stay identical.
- Theme deletion is blocked for Claude; Sara removes old themes in admin.
