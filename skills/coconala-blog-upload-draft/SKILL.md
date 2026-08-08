---
name: coconala-blog-upload-draft
description: Create fact-checked Japanese Coconala blog articles from live product pages, generate a thumbnail and two article images in editable ChatGPT image chats, normalize all images below 700 KB, insert them into the native Coconala editor, and save and reopen the result as an unpublished draft. Use when the user asks Codex to take a Coconala blog from product research through image generation and live draft upload, including recurring-character references and post-save verification.
---

# Coconala Blog Upload Draft

## Run the workflow

1. Read `references/live-workflow.md` completely before writing, generating images, or operating Coconala.
2. Inspect the live product page and use only currently visible facts. Keep the user's adopted title exactly.
3. Write 1,000–1,400 Japanese characters with three two-line headings, two image placeholders, a clear CTA, and the product URL on the final line.
4. Create one article-specific ChatGPT chat. Send the thumbnail, body A, and body B requests one message at a time. Do not use Codex ImageGen for this workflow.
5. Visually inspect and download every actual generated image. For recurring characters, attach the reference image and preserve defining facial, clothing, color, and role details across all three images.
6. Run `scripts/normalize_blog_images.py` for each image. Honor the user's requested canvas; otherwise default to 1280 x 670. Keep every final file at or below 700 KB.
7. Verify the requested Coconala account before entering data. Insert the thumbnail as the cover and replace both body placeholders through the native image tool.
8. Apply native bold and center alignment to all six heading lines.
9. Click **下書き保存** only. Never click **公開設定** or confirm publication.
10. Reopen the exact edit URL and verify the account, exact title, draft timestamp, thumbnail, two body images, removed placeholders, and six persisted bold-centered heading lines.

## Handle blockers

- Stop before saving when the visible account is not the requested account.
- When ChatGPT is busy, wait in short intervals and resume the same chat. Do not duplicate a request merely because generation is slow.
- Treat a completion message as incomplete until the generated pixels are visible and checked.
- If a heading format does not survive reload, correct it and follow the persistence recovery in the reference.
- Distinguish locally prepared content from a live draft proven after reopening.

## Report evidence

Return the exact title, product URL, character count, three image dimensions and sizes, ChatGPT image chat URL, Coconala draft edit URL, saved timestamp, account, and confirmation that the article remains unpublished.
