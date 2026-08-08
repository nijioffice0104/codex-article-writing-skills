---
name: relife-art-carousel-chatgpt
description: Generate Instagram carousel images in ChatGPT using the user's Relife Art generator workflow, then verify completion and visual requirements. Use when the user asks to create, send, continue, inspect, save, or QA Instagram/TikTok carousel images through ChatGPT or the Relife Art generator, especially 魂のレシピ, 720x900px carousel posts, independent-image generation, prompt submission, image-count checks, and design/style inspection.
---

# Relife Art Carousel ChatGPT

## Purpose

Use this skill to operate the user's established workflow for creating Instagram/TikTok carousel images through ChatGPT with Relife Art generator-style prompts, then verify whether generation finished and whether the output follows the requested format.

The user cares most about: exact design continuity, one independent image per output, strict canvas size, readable Japanese text, no contact sheets/grids, and honest inspection instead of claiming completion too early.

## Core workflow

1. Clarify the active scope only if it is genuinely ambiguous:
   - theme/title;
   - number of carousel images;
   - size, usually `720x900px` for Instagram/TikTok carousel;
   - design style, such as `魂のレシピ`;
   - whether to create in a new ChatGPT room or continue a confirmed URL.
2. If the user says to work in ChatGPT, use the Chrome browser session because it usually has their logged-in ChatGPT state. Do not generate the images inside Codex unless the user explicitly asks Codex/imagegen to do it here.
3. If the user provides a confirmed ChatGPT conversation URL, continue there. Otherwise, create one new ChatGPT room per theme unless the user asks for a different grouping.
4. Submit a strict generation prompt. Include the generator URL as context when requested: `https://relife-art-generator.hidemiya.chatgpt.site/`.
5. Wait for generation to finish. Do not leave the user without updates during long waits.
6. Verify completion before reporting success:
   - no visible stop-generating button;
   - no error message;
   - prompt text for the target theme exists in the room;
   - expected number of generated image IDs or visible images can be found;
   - if possible, inspect the images visually for style, text, cropping, and size cues.
7. If verification is partial because ChatGPT virtualized older images or the browser cannot expose them, say exactly what was verified and what remains unverified.
8. If the user asks to save or organize images, use the browser `pageAssets` capability when available, download/bundle the correct image assets, then folder them by theme/title. Do not rename or overwrite user files destructively.

## Standard prompt rules for Instagram carousel

Always include these constraints unless the user overrides them:

- Output one independent image at a time; never a contact sheet, grid, collage, preview, mockup, multiple-card list, or thumbnail sheet.
- Canvas must be `720px × 900px`, vertical 4:5, full-canvas use.
- Important text, tags, borders, and decorations must stay inside a safe margin; do not crop strings, tags, strings, borders, or ornaments.
- Japanese text must be large, accurate, and readable on a phone.
- Avoid overpacking. Assume delivery around 700KB if the user asks for lightweight files.
- No price text unless explicitly requested.
- No CTA arrows or direction arrows when the user says CTA arrows are forbidden.
- One theme should have one consistent visual world. Do not vary each slide into unrelated designs.

## 魂のレシピ style lock

When the user asks for `魂のレシピ`, keep the exact visual family:

- white card paper or thin cream background;
- large whitespace and clean layout;
- dark-brown Mincho-style Japanese headline;
- thin gold double border inset from the canvas edge;
- top-left red hanging warning tag with string;
- top-center label `魂のレシピ / Recipe for the Soul`;
- top-right white feather and warm gold light;
- small lower motifs such as bell, moon, notebook, checklist, flowers, branches, or simple symbolic items;
- delicate gold lines, tiny botanical decorations, and a calm elegant mood.

Avoid:人物写真メイン, 派手背景, 別テンプレ, 雑誌風, 広告バナー風, 過剰なスピリチュアルポスター, unrelated colors, and changing the design family slide by slide.

## Prompt skeleton

Use this skeleton and fill it with the user supplied theme/content.

```text
重要：これはChatGPT内の画像生成タスクです。
Relife Artデザインツール風のInstagramカルーセル画像を作成します。
https://relife-art-generator.hidemiya.chatgpt.site/

【絶対条件】
- 出力は1枚ずつの独立画像。1枚の中に複数ページを並べない。
- contact sheet / grid / collage / mockup / preview / 複数カード一覧 / サムネイル一覧は禁止。
- キャンバスは横720px × 縦900px。縦長4:5。サイズ厳守。
- 画像全体をフルキャンバスで使う。横長・正方形・余白だらけは禁止。
- 重要な文字・赤タグ・装飾・枠は安全余白内に入れる。文字切れ禁止。
- 日本語は大きく、正確に、読みやすく。文字化け禁止。
- 700KB程度で納品する前提のため、過密にしすぎない。
- 価格表記なし。CTA矢印なし。
- 生成後、自分で検品し、サイズ違い・文字切れ・グリッド化・誤字・デザイン違いがあれば再生成する。

【デザイン】
魂のレシピ：白いカード紙／薄いクリーム背景／ダークブラウン明朝／赤い注意タグ／細い金枠／羽根／金色の光／鈴／植物の小枝／清潔感／上品。怖さは煽るが、美しくシンプル。

【このチャット名】
{chat_name}

【作成する画像】
{theme_or_count}
{slide_texts}
```

## Verification checklist

Before saying “できました,” check and report concisely:

- expected count vs found/generated count;
- generation stopped cleanly, with no stop button;
- no visible ChatGPT error;
- whether the right theme text is present;
- whether visible image dimensions/aspect ratio look correct;
- whether the design matches the locked style;
- whether any text appears cropped, unreadable, or obviously wrong.

If only the prompt was sent and the images are still generating, say “送信済み・生成中” rather than “完了.”
If generation is complete but visual inspection is not done, say “生成完了、検品は未完.”
If downloaded/saved files are requested, only say “保存済み” after local files exist and the folder path is verified.

## User communication

Use warm, brief Japanese updates. The user prefers decisive execution, but appreciates knowing whether the state is:

- 指示送信済み;
- 生成中;
- 生成完了;
- 検品中;
- 要再生成;
- 保存整理済み.

When there is uncertainty, name it directly and avoid overclaiming.
