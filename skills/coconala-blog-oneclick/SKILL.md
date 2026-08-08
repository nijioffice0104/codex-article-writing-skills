---
name: coconala-blog-oneclick
description: Create, revise, and save Coconala blog articles as drafts from a live product page, including fact-checked Japanese copy, Coconala-safe formatting, three lightweight images generated in the user's editable ChatGPT image chats, and post-save verification. Use when the user asks to write Coconala blogs, split existing products into article batches, recreate thumbnails, continue the blog one-click workflow, or save Coconala drafts without publishing.
---

# Coconala Blog One-Click

## Run the workflow

1. Read `references/prompt-template.md` completely before writing or operating the browser.
2. Collect the target account, product URL, adopted title, fixed first line, article memo, exclusions, and image style. Reuse supplied decisions exactly.
3. Open the live product page and extract only currently visible facts. Never invent reviews, qualifications, results, counts, scarcity, guarantees, or product conditions.
4. Produce the article in the required output order and run the text checks in the reference.
5. Generate three images through ChatGPT's own image generator in a new article-specific ChatGPT chat. Do not call Codex ImageGen for this workflow. Send one image request per message so the user can edit or retry each image later.
6. Visually inspect each actual generated image, download it, reduce it to 700 KB or less when needed, and confirm it is an independent 1280 x 670 image rather than a collage.
7. Before touching Coconala, verify the signed-in account is the requested account. Enter the title, body, native formatting, and images in the intended positions.
8. Save as a draft only. Never select or confirm publication.
9. Reopen or reload the exact draft and verify the account, title, draft state, saved timestamp, edit URL, body, and images. Report native formatting as complete only when it persists after reload.

## Handle blockers

- Stop before saving when the account cannot be verified.
- Keep the completed text and image prompts when Chrome control fails; report the exact unsaved step instead of claiming completion.
- If the editor strips bold or centering, preserve the content, list the intended formatting, and mark formatting as incomplete until verified in the native UI.
- Treat a generated-image message as incomplete until the actual image is visible and visually checked.

## Deliver completion evidence

Return the article title, product URL, character count, three image statuses, draft edit URL, saved timestamp, account, and explicit confirmation that it remains unpublished. Distinguish prepared content from a draft proven after reopening.
