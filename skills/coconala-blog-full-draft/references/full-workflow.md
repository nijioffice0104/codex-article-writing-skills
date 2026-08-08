# Full Coconala blog draft workflow

## Inputs

Collect these before execution when they are not already supplied:

- target Coconala account;
- live product URL;
- adopted article title;
- fixed first line, if any;
- article memo or angle;
- required inclusions;
- exclusions;
- image style;
- recurring-character reference image, if any.

Reuse supplied decisions exactly.

If the adopted article title, concept, or headings are not supplied, design them after product research using `article-planning-playbook.md`. Do not ask the user to fill routine gaps when the live product page gives enough safe material to proceed.

## Product research

Open the live product page and extract only visible facts. Safe facts include service content, target reader, visible flow, visible cautions, price, seller wording, and product URL.

Do not invent or imply:

- reviews or ratings not visible;
- qualifications, awards, or credentials not visible;
- sales counts, favorites, remaining slots, scarcity, guarantees, or success results;
- medical, legal, financial, or other expert conclusions.

When the adopted title is stronger than the product page wording, keep the adopted title but make the body fact-safe.

## Article planning

Before drafting, create an internal reader-facing plan:

- target reader and likely hesitation;
- reader's ideal state after reading;
- product value supported by visible facts;
- safe trust support from visible facts;
- missing details that must not be invented;
- title candidates if no title is fixed;
- three two-line headings;
- natural CTA direction.

Use the plan to make the article feel like it is speaking to the reader, not merely reporting product features. Do not include the internal plan in the Coconala post unless the user asks for it.

If details are missing, compensate with reader pain, visible process, and safe service fit. Mark uncertain items in working notes, but remove unresolved bracket notes from the final Coconala body before upload.

## Article contract

- Japanese body length target: `1000` to `1400` characters unless the user asks otherwise.
- Preserve the adopted title exactly.
- If no adopted title was supplied, choose the strongest safe title from the planning step and use it consistently for the article, thumbnail prompt, upload title, and completion report.
- Preserve a fixed first line exactly when provided.
- Use three headings, each as two standalone lines.
- During preparation, place two standalone placeholders:
  - `[画像挿入A]`
  - `[画像挿入B]`
- End with a natural CTA and the live product URL on its own final line.
- Keep the tone warm, concrete, and Coconala-safe.
- Avoid Markdown marks, HTML tags, and fake formatting inside the body.
- Keep heading lines separate from the body so native Coconala bold and center alignment can be applied.

## Claude Code prose pass

When a usable Claude Code session is available, send the prepared article draft to Claude Code before image generation or Coconala upload.

Ask Claude Code to:

- make the Japanese body natural, friendly, warm, and easy to read;
- keep the tone approachable rather than salesy or stiff;
- preserve the adopted title exactly;
- preserve all six heading lines and the two-line heading structure;
- preserve `[逕ｻ蜒乗諺蜈･A]` and `[逕ｻ蜒乗諺蜈･B]` exactly;
- preserve the final CTA and product URL;
- use only product-page facts already extracted by Codex;
- avoid adding reviews, ratings, sales counts, guarantees, credentials, scarcity, success claims, or expert conclusions;
- return only the revised title and body, plus a short note if anything could not be improved safely.

Use this prompt shape:

```text
Use the coconala-blog-full-draft prose pass.
Please rewrite the following Coconala blog draft into natural, friendly Japanese.
Preserve the exact title, all two-line headings, image placeholders, CTA, product URL, and all factual limits.
Do not add new facts, results, reviews, qualifications, guarantees, scarcity, or sales claims.
Return only the revised title and body.

[draft here]
```

After receiving the Claude Code revision, compare it against the original facts and reject or repair any added claim before continuing. If Claude Code is unavailable, blocked, or cannot be verified, perform the same prose pass in Codex and state the fallback in the completion report.

## Image prompt sequence

Use ChatGPT's editable image generator in the user's signed-in browser session. Create one new article-specific chat and keep its URL.

Send exactly one image request per message:

1. Thumbnail / eyecatch, normally in Relife Art style.
2. Body image A.
3. Body image B.

Common requirements:

- Default canvas: `1280 x 670` unless the user requests a different canvas.
- Final file size: `700 KB` or less.
- One independent image.
- No collage, grid, split screen, contact sheet, mockup, preview board, or comparison layout.
- Do not reuse unrelated past images.
- Use a fresh image for the article.

Thumbnail requirements:

- Default to Relife Art generator/workflow styling for the thumbnail when the user does not specify another style. Include `https://relife-art-generator.hidemiya.chatgpt.site/` as style context when useful.
- Use the Relife Art visual world as inspiration, but keep the final Coconala canvas, normally `1280 x 670`. Do not switch to `720 x 900` unless the user explicitly asks for Instagram carousel output.
- Include the adopted article title exactly when text is requested.
- Do not add subtitle text, numbers, URL, logo, watermark, or extra claims.
- If the user requests no text, make it completely textless.

Body image A requirements:

- Match the first half of the article: reader's worry, realization, or emotional context.
- No readable text, numbers, URL, logo, watermark, or frame.

Body image B requirements:

- Match the second half of the article: relief, next step, service fit, or future-facing image.
- No readable text, numbers, URL, logo, watermark, or frame.

Recurring-character requirements:

- Attach the reference image in the first image request when available.
- Preserve defining face, hair, clothing, colors, role, and mood across all three images.
- Do not alter the character into a different person or unrelated style.

## Image inspection

Inspect the actual visible/downloaded pixels, not ChatGPT's text.

Pass criteria:

- expected count exists;
- every image is independent;
- dimensions match the requested canvas after normalization;
- each final file is `700 KB` or less;
- thumbnail title is correct when text is requested;
- body images have no readable text;
- no logo, URL, watermark, or unwanted frame;
- no broken anatomy, unreadable artifacts, or obvious design mismatch.

If an image fails, retry only that image and state the exact failure in the retry prompt.

## Normalize images

Run:

```powershell
python scripts/normalize_blog_images.py source.png destination.jpg --width 1280 --height 670 --max-kb 700
```

Use the user's requested canvas if different. Verify output dimensions and byte size after conversion.

## Coconala upload

1. Open Coconala in the signed-in browser.
2. Verify the visible account matches the requested account. Stop before saving if it does not.
3. Create a new blog article or open the intended edit page.
4. Enter the exact title and body.
5. Set the thumbnail/cover image using the native cover-image tool.
6. Replace `[画像挿入A]` and `[画像挿入B]` with the matching body images using the native editor image tool.
7. Apply native bold and center alignment to all six heading lines.
8. Save as draft only.
9. Never select publish, public release, or publication confirmation.

## Persistence proof

After saving:

1. Return to the blog list or reload the exact edit page.
2. Open the exact draft edit URL.
3. Verify:
   - requested account;
   - exact title;
   - draft/unpublished state;
   - saved timestamp;
   - cover image exists;
   - exactly two body images exist;
   - placeholders are gone;
   - body text persisted;
   - all six heading lines remain bold and centered.

If formatting fails to persist, reapply it, make a harmless real edit such as adding one trailing space to the CTA, blur the editor, wait for the save indication, and verify again.

## Completion report

Report completion only with:

- title;
- product URL;
- character count;
- image filenames, dimensions, and file sizes;
- ChatGPT image chat URL;
- Coconala draft edit URL;
- saved timestamp;
- verified account;
- confirmation that it remains unpublished.
