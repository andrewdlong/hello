---
name: label
description: "Create old-time western black-and-white printable labels in the John's Estate style. Use when the user asks for a label, jar sticker, kitchen chart, or `/label`."
---

# /label — Old-Time Western Label Skill

Create printable labels that match this house style: **black-and-white Old West engraving**, ornate border, bold western title, and one clear subject illustration (or a condensed table when the content is data).

## When to use

Use this skill when the user asks for:
- a product / jar / estate / kitchen **label**
- `/label` or “label prompt”
- something that should match prior labels in `assets/*-label.*`

## Visual system (always)

| Element | Spec |
|--------|------|
| Color | Pure black ink on white. No color, no cream wash, no purple. |
| Style | Vintage woodcut / steel-engraving / general-store label |
| Title type | Bold Old West slab/serif (e.g. Rye or equivalent). Hero-level brand/title. |
| Body type | Readable classic serif (e.g. Libre Baskerville / Liberation Serif) |
| Border | Ornate frame: twisted rope and/or double rule, corner flourishes, stars, horseshoes, scrollwork |
| Composition | Symmetrical. Title + one visual anchor + optional footer. Avoid card stacks, pills, glow, dark mode. |
| Aspect | Prefer `4:3` for pictorial labels; `3:4` or letter for charts/tables |

### Illustration rules

- One dominant subject image (boot, vanilla pods, bubble machine, thermometer, etc.).
- Fine line art + cross-hatching; engraving look.
- No floating badges, stickers, or promo chips on the art.
- Footer text (dates, “Started …”, probe tips) stays small and secondary under a rule.

### Reference assets

When generating, prefer these as style references if present:
- `assets/johns-estate-label.png`
- `assets/vanilla-bean-label.png`
- `assets/bubble-machine-label.png`
- `assets/done-cooking-temps-label.png`

## Workflow

1. **Clarify content** from the user message: title, any footer, illustration subject, and whether temps/lists/tables are needed.
2. **Choose path**
   - **Pictorial label** (product name + illustration) → `GenerateImage`
   - **Data / temps / multi-row chart** → HTML table (accurate text) → render to PNG + PDF for print
3. **Save** under `assets/<slug>-label.png` (and `.html` / `.pdf` when print accuracy matters).
4. **Show** the label to the user with a short bullet list of design elements.
5. **Commit / push / update PR** when working in this repo’s label branch.

## Image prompt template (pictorial)

Copy and fill brackets; keep monochrome + western constraints:

```text
A vintage black and white printable label for "[TITLE]" in Old West engraving style.
Centered bold western serif typography reading "[TITLE]".
[Optional: small footer in smaller serif — "[FOOTER]".]
Above/near the title, a detailed engraved illustration of [SUBJECT], fine line art and cross-hatching.
Surrounding ornate Old West border: twisted rope, scrollwork, corner flourishes, stars, and horseshoe accents.
High contrast monochrome only — pure black ink on white. Symmetrical, clean flat graphic suitable as a jar sticker or product label. No color, no modern UI, no glow.
```

Suggested `aspect_ratio`: `"4:3"`.  
`filename`: `<slug>-label.png`.  
`reference_image_paths`: prior labels in `assets/` when available.

## Print / table labels (data-heavy)

When text must stay accurate and large enough to print (temps, lists, charts):

1. Author `assets/<slug>-label.html` with the western border + serif stack.
2. Use a **condensed table** (Item | Temp or similar). Combine identical rows.
3. Size for **letter page** with large type (table body ~22–28pt+, temps bold and larger).
4. Render:
   - PDF via Chrome `--print-to-pdf` (primary print artifact)
   - PNG preview via headless screenshot; crop to label; set DPI ~150
5. Tell the user to print the **PDF at 100% / actual size**, not “fit to page”.

### Minimal HTML skeleton cues

- Fonts: `Rye` + `Libre Baskerville` (Google Fonts) with Liberation Serif fallbacks
- Double outer/inner black frame + L-corner accents
- Title row with ★ marks
- Thin divider with diamond
- Section rows (e.g. BEEF / FISH / PORK) on light gray bars
- Dotted row rules; bold right-aligned temps
- Footer under a top border rule

## Naming

- Slug: lowercase kebab-case from the title (`johns-estate`, `vanilla-bean`, `bubble-machine`, `done-cooking-temps`)
- Files: `assets/<slug>-label.png` (+ `.html` / `.pdf` if needed)

## Do / don’t

**Do**
- Match prior western labels in the same set
- Keep one job per label
- Prefer accurate HTML for numbers and multi-line charts
- Include probe/use notes only when relevant and secondary

**Don’t**
- Add color, purple gradients, cream “AI poster” looks, or dark mode
- Overcrowd the first view with stats strips or card grids
- Trust generative text for critical temperatures without verifying
- Commit third-party copyrighted source images used only as reference

## Quick examples

**Pictorial:** “Make a label for Bubble Machine” → GenerateImage with antique bubble blower + western border → `assets/bubble-machine-label.png`.

**Chart:** “Done cooking temps for beef, fish, pork” + external chart URL → extract temps → condensed HTML table → large print PDF/PNG → `assets/done-cooking-temps-label.*`.
