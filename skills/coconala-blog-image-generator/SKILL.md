---
name: coconala-blog-image-generator
description: Generate and quality-check Coconala blog thumbnails and article images by extracting prompts from the local Blog Generator Pro one-click desk and transmitting them to ChatGPT's editable image generator, one image per message. Use when the user asks to create, recreate, repair, or lighten a Coconala blog thumbnail, eyecatch, or article image using the generator tool rather than generating inside Codex.
---

# Coconala Blog Image Generator

## Use the generator source

1. Read `references/generation-workflow.md` completely.
2. Locate the exact `ブログ制作ワンクリック卓.html` named or shown by the user. When similar files exist, verify the intended path before extracting anything.
3. Open the tool and use its image-generation output for the selected article. If browser interaction is unavailable, extract the generated text from the file logic without altering its rules.
4. Preserve the article title, theme, atmosphere, design type, and any explicit no-text instruction exactly.

## Transmit to ChatGPT

1. Use the user's signed-in ChatGPT browser session and create a new article-specific chat or tab.
2. Send the thumbnail request alone. Do not call Codex ImageGen and do not generate the image inside the Codex conversation.
3. When article images are requested, send A and B as separate second and third messages. Never request multiple images in one message.
4. Record the ChatGPT chat URL so the user can edit or retry the images later.

## Verify actual files

Inspect the displayed or downloaded image itself. Do not accept ChatGPT's text description as evidence. Confirm image count, independence, dimensions, file size, text rules, composition, and consistency with the article. Retry only the failed image with its exact failure reason.

Report a generation request as incomplete until the real image is visible and checked. Report a delivery as complete only after the file is downloaded, 1280 x 670 pixels, 700 KB or less, and visually acceptable.
