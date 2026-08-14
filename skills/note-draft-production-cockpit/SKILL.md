---
name: note-draft-production-cockpit
description: Finish long-form note.com drafts from an existing manuscript or live note editor by preserving the original text, applying note-ready headings/bold/bullets, planning and generating thumbnails plus explanatory in-article images, inserting images in the correct positions, saving as draft, and verifying the final unpublished state. Use when the user asks to prepare, decorate, upload, finish, relay images into, or make a note article ready to post, especially with Blog Generator Pro, ChatGPT image relay, note editor URLs, thumbnails, H2 images, or strict "do not publish" requirements.
---

# Note Draft Production Cockpit

Use this skill as the operating checklist for turning a completed note manuscript or existing note editor draft into a publish-ready but unpublished draft.

## First Rule

Preserve the user's manuscript and newest instruction. If the user says the article is already written or pasted into note, do not rewrite it; only adjust formatting, headings, spacing, bold, bullets, and image placement unless they explicitly ask for prose editing.

Never click the final publish button. Stop at saved draft or publish preflight only when asked, and report that the article is still unpublished.

## Required Workflow

1. Open or inspect the exact target article, draft, local manuscript, and any reference image.
2. Record the title, target URL, current draft state, H2 count, requested image count, and whether the user wants prose editing or decoration only.
3. Locate and use Blog Generator Pro when the user requires it. If the required BGP cockpit cannot be found or run, report the exact blocker instead of silently switching to manual work.
4. Decorate the article without changing meaning: H2/H3, bold, bullets, spacing, separators, quotes, and CTA placement.
5. Plan every image before generating: thumbnail plus each requested H2/body image, with insertion position, purpose, composition, and short readable Japanese text.
6. Generate images in batches where the active ChatGPT or image workflow supports it. Avoid one-by-one credit-wasting loops unless the tool only supports single-image calls.
7. Save images into a dedicated local folder with non-duplicated names and separate `thumbnail`, `body`, and `rejected` or `reference` subfolders when useful.
8. Insert images in relay order: title/intro, thumbnail, H2, matching image, body, next H2, matching image. Do not dump images at the end.
9. Verify the rendered editor after reload or equivalent durable state: text present, headings visible, images inserted at intended points, no prompt text leaked, no duplicate image, draft saved, not published.
10. Report with the completion checklist from `references/high-speed-note-workflow.md`.

## Decision Points

- **Decoration-only request:** Keep every sentence as-is except minimal line breaks or formatting. Do not improve the opening sentence, tone, or wording.
- **Editing request:** Improve clarity, opening hook, human tone, and note readability while preserving facts, numbers, lived experience, product names, service names, and CTA.
- **Exact image count request:** Obey the user count. If H2 count and requested image count conflict, state the mapping before generation and follow the newest instruction.
- **Reference design request:** Use the reference only for style, layout, color, and diagram language. Do not copy logos, brands, marks, or copyrighted text.
- **Failure:** Retry only the failed step. Do not regenerate accepted images, wipe the article, or restart the whole workflow.

## Read When Needed

Read `references/high-speed-note-workflow.md` when executing a live note completion task, building image prompts, handling Blog Generator Pro, or preparing the final checklist.
