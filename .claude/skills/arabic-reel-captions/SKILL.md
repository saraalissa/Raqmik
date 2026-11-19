---
name: arabic-reel-captions
description: Add premium animated Arabic captions to a vertical talking-head video - words bent around the head, a big calligraphy word behind the head, neon, liquid glass, words painted on the wall, highlighted word boxes, UI chips and a warm cinematic grade. Use when someone wants eye-catching or trending-reel captions, «كابشن ملفت», «كلام ورا راسي», «كلام بيلف حواليا», or sends a talking video and asks for creative captions.
---

# Arabic reel captions

Turns a vertical video of one person talking into a reel whose words interact with the speaker, in a premium look:
a modern sans font (Alexandria) for the small words, cream/gold calligraphy (Aref Ruqaa) for the key word, an elegant italic (Amiri) for English words. Every word blurs in, rises and settles; key words pop with a soft glow. Reply to the user in their own language and dialect.

## What you need from the user

1. The video: vertical (9:16), one person talking, with some empty wall above or beside the head.
2. The exact words spoken. If they can't give them, transcribe the audio and ask them to confirm before rendering.
3. Optional: which words matter most. If they don't say, pick them yourself (the punchline, the brand, numbers, the call to action).

For a video made of several scenes, run every step per scene and join the results at the end (`ffmpeg -f concat`).

## Setup (once per session)

```bash
pip install --break-system-packages onnxruntime opencv-python-headless pillow soundfile numpy
python3 -c "from PIL import features; print('raqm', features.check('raqm'))"   # must print True
which ffmpeg
```
If raqm is False, Arabic letters won't join: `apt-get install -y libraqm0 libfribidi0` (or `pip install -U pillow`) and check again.
`S` = this skill's `scripts` folder.

## Steps

1. **Cut out the speaker** (only used to put words *behind* her, never to replace the background):
   `python3 $S/matte.py in.mp4 matte.mp4` — downloads a 15 MB model once; about 4 frames a second at 1080p.
2. **Time the words**: `python3 $S/timing.py in.mp4 "<exact line>" words.json` prints every word with its time.
   Check the times against the speech pauses; fix by hand if a word is clearly early or late.
3. **Write `plan.json`** (format below). Pick each style from what the word *means*.
4. **Preview**: `python3 $S/render.py --video in.mp4 --matte matte.mp4 --plan plan.json --preview 0.6,1.8,3.2`
   writes `preview_<t>.jpg`. Look at every event. Fix and preview again until every rule below passes.
5. **Render**: same command with `--out captioned.mp4`. The original sound is kept.
6. **Check** a contact sheet (`ffmpeg -i captioned.mp4 -vf "fps=4,scale=270:-1,tile=8x4" sheet.jpg`), then deliver.

## plan.json

```json
{"grade": true, "face": [540, 620],
 "events": [
  {"style": "hero", "text": "استنى", "t0": 0.44, "t1": 1.75, "x": 540, "y": 1340, "size": 260},
  {"style": "arc", "which": "bottom", "cx": 540, "cy": 620, "rx": 470, "ry": 520, "size": 118, "t1": 3.3,
   "words": [{"w": "الكابشن", "t": 0.92}, {"w": "ده", "t": 1.62}, {"w": "كله", "t": 1.80}]},
  {"style": "arc", "which": "top", "cx": 540, "cy": 620, "rx": 470, "ry": 520, "size": 160, "off0": -120, "off1": 120, "t1": 3.3,
   "words": [{"w": "جه", "t": 2.0}, {"w": "منين؟", "t": 2.1}]},
  {"style": "line", "x": 540, "y": 1270, "size": 100, "t1": 4.2,
   "words": [{"w": "كل", "t": 2.58}, {"w": "ما", "t": 2.75}, {"w": "أتحرك", "t": 2.9}]},
  {"style": "hero", "text": "بتتغير", "t0": 3.25, "t1": 4.2, "x": 540, "y": 1490, "size": 330}
 ]}
```
`grade`: warm cinematic look on the whole frame with a soft spotlight on `face` (x, y of the face centre). Positions are pixels of the video (1080x1920).

| style | looks like | fields | best for |
|---|---|---|---|
| `line` | small words that blur in one by one | `words` [{w, t, font?, fill?, size?, box?, glow?}], `t1`, `x`, `y`, `size` | most of the sentence |
| `hero` | one big calligraphy word that pops with a glow | `text`, `t0`, `t1`, `x`, `y`, `size`, `fill` (creamgrad/goldgrad), `behind` | the key word |
| `hero` + `"behind": true` | the big word stands on the wall and her head covers part of it | same | «ورا راسي», a word that should feel huge |
| `arc` | the phrase bends around the head; `top` passes behind the head, `bottom` in front under the chin | `which`, `cx`, `cy`, `rx`, `ry`, `words`, `t1`, `size`, `off0`/`off1` (slide in px) | questions, "around", "everywhere" |
| `neon` | neon tube sign that flickers on, behind her | `text`, `t0`, `t1`, `x`, `y`, `size`, `colour` | light, shine, a brand name |
| `glass` | liquid-glass letters that refract the room, behind her | `text`, `t0`, `t1`, `x`, `y`, `size` | one strong short word |
| `wall` | lines painted on the wall in perspective, behind her | `lines` [{w, t, font?, fill?, size?}], `t1`, `x`, `y`, `size`, `tilt` | a remark placed on an empty wall |
| `chips` | UI pills that pop in one after another | `items` [{text, x, y, t, bg?, fg?, rot?}], `t1` | lists of options |
| `counter` | editor-style "frame 0081 / 1305" pill | `t0`, `t1`, `x`, `y` | talking about editing frame by frame |

Word options: `font` = sans / sans_xb / sans_md / callig / latin_it (use latin_it + fill goldgrad for English words), `fill` = white / cream / gold / creamgrad / goldgrad / [r,g,b], `box` = red / blue / yellow (word on a coloured box).

## Rules (check every preview)

- **Never over the face** (eyes, nose, mouth). Put text above the head, on the wall beside it, or on the chest.
- **Big and readable**: on a 1080-wide video use 85–100 px for small words, 250–330 px for the key calligraphy word, 110–160 px for arcs. Every phrase stays on screen until the next phrase starts in the same spot, and never less than 1 s; key words 1.2 s or more.
- **One big effect at a time**, at most two things on screen.
- **Hook in the first second**: a `hero` or an `arc` on the first words.
- **Safe zone**: keep text between 6% and 85% of the height and away from the right edge buttons.
- Copy the spoken words exactly; no tashkeel; English words stay in English letters.
- Behind / neon / glass / wall need empty wall behind the text; if the wall there is busy, move the text.
- Use 5–7 different styles in a 20–30 s reel and change style every 2–4 seconds.

## Credits and licences

Fonts: Alexandria, Aref Ruqaa, Amiri, Reem Kufi — SIL Open Font License (`fonts/OFL-LICENSES.txt`). Matting: Robust Video Matting by Peter Lin et al. (GPL-3.0), downloaded from its official GitHub release at first use.
