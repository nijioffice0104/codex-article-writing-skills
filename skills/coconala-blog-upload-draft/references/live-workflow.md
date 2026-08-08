# Live workflow

## Article contract

- Preserve the adopted title and any fixed first line exactly.
- Use three headings, each made of two standalone lines.
- Place `＜画像挿入：A＞` and `＜画像挿入：B＞` on standalone lines during preparation.
- End with a natural CTA and the live product URL on its own final line.
- Do not invent reviews, qualifications, results, counts, scarcity, guarantees, or product conditions.
- If a user-provided title conflicts with the current product page, keep the adopted title but state current product facts accurately in the body.

## ChatGPT image generation

- Use ChatGPT's editable image generator, not Codex ImageGen.
- Start a new article-specific chat and send one image request per message.
- Order: thumbnail, article image A, article image B.
- Thumbnail: use the adopted title only, exactly; reject extra text.
- Body images: no readable text, numbers, URL, logo, watermark, frame, collage, or split screen.
- Recurring character: attach the reference image in the first message and explicitly preserve its defining features in all later requests.
- Wait in short intervals when generation is slow. Download and visually inspect the actual image before continuing.

## Normalize images

Run:

```powershell
python scripts/normalize_blog_images.py source.png destination.jpg --width 1732 --height 903 --max-kb 700
```

Use the canvas explicitly requested by the user. If none is requested, use 1280 x 670. Verify the dimensions and byte size after conversion.

## Insert into Coconala

1. Open the blog list and verify the visible account name.
2. Choose **記事** and proceed to the editor.
3. Fill the exact title and body.
4. Click **カバー画像を設定**, upload the thumbnail, and click **決定** when the crop dialog appears.
5. Replace each body placeholder through the UI:
   - Click the placeholder line.
   - On the contenteditable editor, press `Home`, `Shift+End`, `Backspace`.
   - Click the camera-plus attachment button on the empty line.
   - Upload the matching body image.
   - Confirm the editor image count increases.
6. Format each heading line separately for reliability:
   - Select the entire line with `Home`, `Shift+End`.
   - Apply **太字**.
   - Reselect the line and apply **位置** for center alignment.
7. Click **下書き保存** only.

## Prove persistence

1. Return to the blog list. Verify the exact title is labeled **下書き** with a new timestamp.
2. Open that card's **編集する** action and record `/mypage/blogs/edit/<id>`.
3. In a fresh load, verify:
   - requested account;
   - exact title;
   - cover already set;
   - exactly two body images;
   - no placeholder text;
   - all six heading lines are bold and centered;
   - no publish action was taken.
4. Coconala may fail to persist center alignment on the final heading line. If so, reapply center alignment, make a harmless real edit such as appending one trailing space to the CTA, blur the editor, wait for **保存しました**, and reopen the edit URL. Do not report success until all six lines persist.
