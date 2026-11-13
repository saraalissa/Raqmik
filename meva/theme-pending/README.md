# Mëva theme: pending upload (13 Nov 2026)

The Shopify connector dropped mid-task, so these files were NOT uploaded.

## What is pending
`sections/meva-pdp.liquid` and `sections/meva-pdpx.liquid` contain two changes that are not on Shopify yet:
1. The 3-stat strip (15% / 83% / 180mg + source line) moved out of the hero into its own section `<section class="pstats">`, cream background #F8EFE6, placed directly above "Notes to self" (`.pnotes`). It appears once.
2. The yellow "Founding 500" box above the pack selector removed in waitlist mode. (The non-waitlist "Free UK delivery" box is kept.)

All other files here match what is already on both themes; they are included so the folder is a complete copy of the custom sections.

## How to finish
1. Find the UNPUBLISHED theme (two copies exist: "Mëva - Draft (Claude)" 145622106171 and "Copy of Mëva - Draft (Claude)" 145862000699; the live one cannot be written).
2. Upload the two pdp files to it: `stagedUploadsCreate` (FILE, POST) → POST the file to the staged target (`upp.py` / `upbatch.py`) → `themeFilesUpsert` with body type URL.
3. Check `/products/meva-magnesium-gummies?preview_theme_id=<id>` on mobile (390px) and desktop: stats appear once, above "Notes to self"; no yellow Founding box; no horizontal scroll.
4. Send the owner the preview link and screenshots. She publishes.
