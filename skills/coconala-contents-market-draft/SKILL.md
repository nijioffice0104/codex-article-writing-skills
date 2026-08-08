---
name: coconala-contents-market-draft
description: Create or update Coconala Contents Market PDF/file drafts from existing Coconala service pages. Use when the user asks to make Coconala contents-market drafts, convert existing service listings into contents-market listings, reuse existing service titles/descriptions/prices/thumbnails, add YouTube sample URLs to service introductions, or prepare unpublished drafts for a specified Coconala shop/account.
---

# Coconala Contents Market Draft

## Core Rules

- Work in Coconala Contents Market, normally at `https://coconala.com/contents_market/manage`.
- Save as an unpublished draft only. Do not publish, submit for sale, or proceed past preview/publish confirmation unless the user explicitly asks.
- Verify the active Coconala account name before editing if the user names a shop/account. Stop and ask the user to switch accounts if it is clearly the wrong account.
- For each source service URL, reuse:
  - title from the existing service unless the user asks for a rewritten title
  - price from the existing service
  - category best matching the product, usually `占い > 占いノウハウ` for astrology/fortune-telling learning PDFs
- Service introduction must include the user-provided YouTube URL. Put it under `▼サンプル動画` or `▼紹介動画`.
- Images must be newly generated square thumbnails based on the existing service thumbnail composition. Do not use blur, do not crop important content, and do not simply stretch or center-crop the old image.

## Inputs To Collect

Proceed when the user provides:

- One or more existing Coconala service URLs.
- One YouTube URL per draft, or a mapping such as `マヤ: <url>`, `インド: <url>`.
- The target shop/account if relevant.
- A final PDF/file path if known. If not known, search local likely locations for matching PDFs.

If a YouTube URL is missing for a draft, ask for it before saving that draft.

## Workflow

1. Read each existing service page.
   - Extract title, subtitle if useful, service content, purchase notes if relevant, price, category, and thumbnail images.
   - Prefer the first main service image as the thumbnail reference.

2. Create or locate the sale file.
   - If the user says the PDF is local, search likely folders such as `Downloads`, `Documents`, Desktop, and obvious project folders.
   - Match by keywords from the service title, e.g. `インド`, `占星`, `マヤ`, `KIN`, `暦`.
   - If no real file is found and the user asked for a placeholder, create a clearly temporary PDF. Otherwise ask.

3. Generate the square thumbnail.
   - Save the existing service thumbnail locally as a reference image.
   - Use `imagegen` to create a new 1:1 square thumbnail preserving the original composition:
     - large Japanese title block
     - original right/left character placement
     - original background theme and motifs
     - readable text hierarchy
   - Prompt constraints must include: no blur, no cropped text, no watermark, no extra brand logos, high readability at thumbnail size.
   - Save the generated image into the workspace, then upload that generated square image.

4. Write the Contents Market service introduction.
   - Follow this structure unless the user specifies another reference:

```text
<1-2 sentence overview of what the PDF/file is and who it helps>

▼サンプル動画
<YouTube URL>

【この教材でできること】
・...
・...
・...

【魅力ポイント】
<why this product is useful and easy to use>

【こんな方におすすめ】
<target buyers>

納品PDFを開き、順番に読み進めながらワークとしてご活用ください。
```

   - Keep under Coconala's field limit, commonly 1000 characters.
   - Remove placeholder warnings before final draft save unless the user wants them.

5. Create or update the draft in Coconala Contents Market.
   - Choose `ファイル` for PDF/file products.
   - Upload sale file first.
   - Upload generated square thumbnail as `検索結果表示画像`.
   - Fill title, category, price, and introduction.
   - Save with `下書き保存`.

6. Verify after saving.
   - Reopen the edit page or inspect the saved draft.
   - Confirm:
     - sale file is present and correct
     - generated square thumbnail is present
     - title is present
     - category is present
     - price matches the source service
     - service introduction includes the YouTube URL
     - draft status is not published unless explicitly requested

## Browser Notes

- Use the browser skill for live Coconala pages and uploads.
- Read the browser file-upload documentation before uploading through Coconala if it has not already been read in the current session.
- If deleting an existing uploaded image/file, be careful: Coconala shows similar trash buttons for the sale file and display image. Verify which item disappeared after clicking.
- If deleting the sale file resets the form, immediately re-upload the real file and restore title, category, price, and introduction before saving.

## Thumbnail Prompt Pattern

Use a prompt like this, adapted to the service:

```text
Use case: ads-marketing
Asset type: Coconala contents market square thumbnail
Primary request: Recreate this thumbnail as a clean 1:1 square image, preserving the original composition and concept without simply cropping.
Input images: Image 1 is the reference for composition, colors, character placement, and text hierarchy.
Style/medium: polished Japanese digital illustration thumbnail, clean readable typography, soft pastel spiritual/fortune-telling design.
Composition/framing: square 1024x1024. Keep all important elements fully visible with balanced spacing. Expand/redesign top and bottom areas naturally so nothing is cut off.
Text (verbatim): "<copy important text from the source thumbnail>"
Constraints: no blur, no cropped text, no watermark, no extra brand logos, high readability at small thumbnail size.
```

## Completion Report

Tell the user:

- Which drafts were updated/created.
- Which PDFs/files were uploaded.
- Whether thumbnails were regenerated and uploaded.
- Which YouTube URLs were inserted.
- Any remaining placeholders or items needing user review.
