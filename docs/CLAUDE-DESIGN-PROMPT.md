# Claude Design Prompts — Hero & Icons

Paste these into Claude Design (or any AI image tool: ChatGPT image, Midjourney, Ideogram, Flux). Two prompts: one for the hero, one for a 5-icon set.

Save the outputs to `docs/hero.png` (or `.gif`) and `docs/icons/<framework>.png` then uncomment the image references in `README.md`.

---

## Brand & visual direction

Use this in any image prompt as background context:

```
Brand: Visual Strategy Consultant — a tool that turns any LLM into a Tier-1
strategy consultant who breaks down complex business problems on a whiteboard.

Vibe:
- McKinsey/BCG/Bain whiteboard energy: structured, confident, slightly retro,
  zero corporate stock-photo gloss
- Black or near-black ink on warm white (egg-shell #F8F4EC, ivory, light cream)
- Hand-drawn-feeling lines but precise — like a senior partner at a glass
  whiteboard, not a doodle
- Optional accent color: a single muted ink tone (deep teal #156E6C OR rust
  #B5532A OR aged-paper sepia) used sparingly for emphasis
- Avoid: rainbow gradients, glassmorphism, neon, Web3, "AI-y" sci-fi visuals,
  corporate stock illustration, generic flat design

Typography in image:
- If using text, lean into a humanist serif (Source Serif Pro, Lora) or a
  confident sans-serif with character (Inter Tight, Söhne, Fraunces) — NOT
  generic Helvetica or Roboto
- Hand-lettered annotations are welcome
```

---

## Prompt 1 — Hero image (top of README)

```
A wide, cinematic 16:9 illustration in the style of a senior strategy
consultant's whiteboard. The whiteboard is photographed from a slight
three-quarter angle, with five distinct visual artifacts laid out left-to-right
across its surface, like a single complete analysis:

1. A nested bullet-point hierarchy (categories with sub-factors), drawn in
   black marker
2. An ASCII-style branching tree with three or four levels, also in black
3. A small comparison table with two columns, "Expected" vs "Actual",
   with check marks and X marks scribbled next to rows
4. A blockquote-style callout circled in a single accent color (deep teal or
   rust), labeled "the vital 20%"
5. Three labeled lines at the bottom: "Process / Result / Insight", with the
   "Insight" line underlined twice

Above all five, hand-lettered at the top of the whiteboard, the title:
"VISUAL STRATEGY CONSULTANT". Below the title, smaller and slightly off-axis,
the subtitle: "five frameworks. one whiteboard. every business problem."

Style: warm-white background (#F8F4EC), black ink, single accent color used
only on the blockquote circle and the "Insight" underline. Photographic but
clearly hand-drawn artifacts. Slight grain/texture suggesting a real
whiteboard. No people. No screens or laptops. No corporate gloss.

Aspect ratio: 16:9 wide
Resolution: at least 1600x900
File format: PNG with transparent or warm-white background
```

**Variants worth trying** (run this prompt 3–4 times with different seeds and pick the cleanest):

- Try once with a glass whiteboard (transparent surface, slight reflection)
- Try once with a paper-on-easel feel (more vintage, more texture)
- Try once flat-lay overhead (top-down view of a notebook page)

---

## Prompt 2 — Five framework icons (one per framework)

These go inside the README's "The five frameworks" table, or anywhere a small visual reference helps. Generate as a unified set so they look like siblings.

```
Generate FIVE small square icons (1:1 aspect ratio, 512x512 each), drawn in a
unified hand-drawn whiteboard style — black ink on warm white (#F8F4EC), with
a single accent color (deep teal #156E6C) used sparingly on one element of
each. Each icon is its own image.

Icon 1 — MECE: a 2x2 grid of distinct boxes with a single dot in each box.
The boxes don't overlap. Above the grid, the letters "MECE" hand-lettered.

Icon 2 — Issue Trees: a small branching tree, three levels deep, drawn with
ASCII-tree feel (├─, │, └─). The root node is circled in the accent color.

Icon 3 — Hypothesis-Driven: a two-column comparison sketch with "Expected"
on the left and "Actual" on the right, three rows, with a small check mark
in the top row of "Actual" drawn in the accent color.

Icon 4 — Pareto: a tall blockquote bar (vertical line with text beside it)
with one short bar drawn in the accent color labeled "20%", and three thin
gray bars labeled "80%" stacked below.

Icon 5 — So What?: three short horizontal lines stacked vertically, each
prefixed with a small circle. The bottom line (the "Insight") is underlined
twice in the accent color.

All five icons must:
- Use the same hand-drawn line weight
- Use the same warm-white background
- Look like they belong as a coherent set
- Be readable at 64x64 thumbnail size

Output: 5 separate PNG files, 512x512 each, transparent background preferred
or warm-white if transparency isn't supported.
```

---

## Prompt 3 — Animated hero GIF (optional)

If you want a 12-second screen-recording-style GIF for the README hero, this prompt produces frames you can stitch:

```
Create a 12-second animated sequence in 16:9 format showing the five
whiteboard artifacts from the hero illustration appearing one at a time,
left-to-right, as if drawn in real time by an unseen hand. Each artifact
takes about 2 seconds to "draw on", with a 0.4-second pause between them.

After all five are drawn, hold for 2 seconds on the complete whiteboard,
then fade gently.

Style: same as the hero illustration — black ink on warm white, single accent
color (deep teal) on the Pareto blockquote and the Insight underline.
Hand-drawn feel.

Frame rate: 12 fps (so ~144 frames total, but most can be held)
Resolution: 1200x675 (light enough to load fast in a README)
File: GIF, optimized to under 5 MB
```

If your image tool doesn't generate GIFs natively, generate ~8 keyframes
showing the whiteboard at progressively complete stages, then assemble in
[ezgif.com](https://ezgif.com/maker) or `ffmpeg`.

---

## Putting it in the README

Once you have `docs/hero.png` (or `.gif`):

1. Drop the file into the `docs/` folder of the repo.
2. In `README.md`, find the line:
   ```html
   <!-- ![teaser](docs/hero.gif) -->
   ```
3. Uncomment it (remove the `<!--` and `-->`).
4. Commit and push.

For the icon set, replace the "Visual format" cells in the framework table with `<img src="docs/icons/mece.png" width="48" />` etc., or add an Icons row above the table.

---

## A note on AI-generated visuals

Image models occasionally produce slightly off-kilter text. If "VISUAL STRATEGY CONSULTANT" comes out as "VlSUAL STRATAGY" or similar, regenerate. Don't ship typos in the hero image. Easier to add the text in post (Figma, Photoshop, even PowerPoint) than to fight the model into spelling correctly.
