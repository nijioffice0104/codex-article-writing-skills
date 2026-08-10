---
name: ameblo-readable-transfer
description: "Format, transfer, schedule, and monitor Niji Office note articles in Ameblo. Use when copying note.com articles to Ameblo, continuing sequential transfers in verified four-article batches with a four-hour cooldown, revising drafts or published posts without changing publication state, scheduling two posts per day at 07:00 and 20:00, monitoring note after the backlog is complete, or applying the Niji Office readable-spacing rule: meatball blocks are forbidden."
---

# Ameblo Readable Transfer

Read [references/niji-office-operations.md](references/niji-office-operations.md) before a live transfer, scheduling run, backlog-completion check, or note-update monitoring run.

## Core Rule

Preserve the article wording, title, images, links, and HTML structure as much as Ameblo allows. Only change spacing for readability.

Meatball blocks are forbidden. If a reader would see a dense clump of 3-5 lines, add breathing room even when the source technically has paragraphs.

Apply these spacing rules:

1. In normal visible text, add an Ameblo-safe blank line (`<br><br>`) after every two sentence endings.
   - Count `。`, `！`, `!`, `？`, `?`, `❓`, `❗`, and sentence-ending emoji such as `🥺`, `✨`, `🌈`, `😭`, `🥰`, `👍` as sentence endings.
   - This means short emotional paragraphs can still receive spacing every two beats, not only every two `。`.
2. In emotional storytelling,恋愛体験談, question hooks, and CTA lead-ins, favor one blank line after one sentence ending when the text is starting to clump.
   - Examples: `その答え、知りたくないですか？`, `こっそり視てもらうことができるとしたら…？`, `🥺✨`, `👍`.
   - Bold question lines and short reader-facing prompts should usually stand alone.
3. If a paragraph/list item/blockquote text becomes a long chunky block, add a blank line after sentence-like endings in that block.
   - Treat roughly 140-180 Japanese characters, or 4-5 mobile-readable lines, as a long block.
   - In chunky blocks, split after `。`, `！`, `?`, `？`, `❓`, `❗`, and sentence-ending emoji such as `🥺`, `✨`, `🌈`, `😭`, etc.
   - If the long block has none of those endings, prefer inserting after Japanese commas, pauses, closing brackets, or sentence-like boundaries.
   - Do not split inside URLs, HTML tags, tag attributes, image tags, or code/pre blocks.
4. Parenthetical punchlines or aside lines such as `（映像的には、イチャコラしていたみたいですｗｗ）` should not be glued to the next paragraph; add spacing after them when they appear as their own block.

## Transfer Workflow

1. Identify the target note.com article keys from the user's sequence.
2. Fetch source HTML from `https://note.com/api/v3/notes/<key>`.
3. Run `scripts/format_ameblo_html.py` on the `data.body` HTML.
4. Open Ameblo in the authenticated browser and use the article editor's HTML/source mode.
5. Insert the formatted HTML through the CodeMirror/source textarea, not the visual editor, whenever possible.
   - Use a fresh Ameblo editor tab for each new article. The legacy editor can retain stale CKEditor state when one tab is reused for multiple new posts.
   - If Ameblo offers to restore an agent-created unsaved duplicate from the same transfer attempt, choose not to restore it before inserting the verified source again.
   - Never paste article HTML into `meta_title` (the search display title). Keep that field empty unless the user explicitly requests an SEO title.
   - After source insertion, switch back to normal view and confirm that the article renders before saving.
6. Preserve existing publication intent:
   - If the user says publish, use `投稿する` and verify the public URL.
   - If the user says draft or does not specify, use `下書き保存`.
   - If the user has narrowed one article to public, keep only that article public and leave the rest as drafts.
7. Verify the Ameblo list state after saving: title, status, date, and article ID.

## Sequential Draft and Reservation Rule

When the user asks to continue transferring note articles, continue from the next untransferred note article in sequence. Exclude titles or note keys already present in Ameblo. Process no more than four new articles in one batch. After a completed and verified four-article batch, wait at least four hours before starting the next batch. A later batch on the same day is allowed after that cooldown.

For each transferred article:

1. Create or update the Ameblo article as a draft first.
2. Apply the readable-spacing rule before saving.
3. After the draft is saved, schedule two reservation posts per day: the morning slot at `07:00` and the evening slot at `20:00`.
4. Use the next open slot after the latest already published or scheduled Niji Office Ameblo article. Do not schedule a slot in the past. If four articles are transferred, use two consecutive days with two posts per day.
5. Keep source order: the next note article goes into the earliest open slot, followed by later articles chronologically.
6. Verify the final list state after scheduling: title, article ID, `予約投稿`, reservation date, and exact time (`07:00` or `20:00`).
7. If one article is intentionally public, keep that public article public and schedule only the newly transferred drafts.

## Four-Article Batch Cooldown

- Starting August 11, 2026, transfer at most four new note articles per run.
- Save every transferred article as a draft first. Never use immediate publication merely to save layout, banners, headers, or CTA changes.
- After the batch is saved and reopened for verification, do not start another transfer batch for at least four hours.
- The four-hour cooldown applies to transfer work, not to the publication cadence.
- Publication remains limited to two posts per day: `07:00` and `20:00`, using the next open future slots in source order.
- Layout-only revisions must preserve each article's current state: draft, future reservation, or already public.
- Before ending each run, verify the exact article IDs, titles, statuses, dates, times, fixed results header, fixed CTA, and mobile-width behavior.

## Backlog Completion and Ongoing Monitoring

1. Build the current note inventory from `https://note.com/niji_office` and extract each `/n/<note-key>` URL in source order.
2. Build the Ameblo inventory from the authenticated article list and record title, article ID, status, and scheduled or published time.
3. Treat the historical backlog as complete only when every current note key has one verified Ameblo article. Title similarity alone is not sufficient when a note key can be checked.
4. After the backlog is complete, check the note profile on each monitoring run. Transfer only note keys that were not present in the previous verified inventory.
5. Process at most four new note articles per run and wait at least four hours before another transfer run.
6. Save each new article as a draft first, then assign only the next open `07:00` or `20:00` future reservation slots. Never publish immediately unless the user explicitly names that article for immediate publication.
7. If no unseen note key exists, make no Ameblo changes and report `NO_CHANGE` with the checked note coverage.
8. Persist or report the note-key-to-Ameblo-ID mapping after every successful run so later monitoring cannot create duplicates.

## Thumbnail and Banner Guardrail

- Ameblo can automatically use an image from the article body as the article-list thumbnail when no dedicated cover image is available.
- Before adding or replacing a fixed body banner, inspect the article's cover image and the public article-list thumbnail.
- Do not assume a mobile-only CSS rule prevents thumbnail selection; hidden body images can still be selected by Ameblo.
- Never change an article's intended thumbnail as an unnoticed side effect. If a fixed banner becomes the thumbnail, preserve the existing state and report the conflict before applying that banner to more articles unless the user has approved the shared thumbnail.
- Sidebar banners must remain separate from article-body banners. A no-link banner must not gain an anchor wrapper during revisions.

## Ameblo Field Limits

- Ameblo article titles have a 48-character input limit. If a note title exceeds it, shorten only the title while preserving its subject and promise; do not alter the article body.
- After a draft save, reopen the exact edit page and verify the rendered body, image count, links, and one fixed LINE CTA.
- For a future reservation, the article list may show `全員に公開` together with a future date rather than the literal text `予約投稿`. Treat the future date/time plus the post-completion page as the authoritative reservation signal.

## Fixed Results Header Block

Every Niji Office Ameblo article should start with the same results header in the article body HTML source. Add it once at the very beginning of the formatted article HTML, before the source article body.

Use the marker `data-niji-office-results="v1"`. Never add a second copy when revising or resaving an article. Keep this block separate from the fixed LINE CTA at the bottom.

Use responsive inline styles only. The outer block and all children must stay within the article width on mobile (`width:100%;max-width:100%;box-sizing:border-box`).

Required results:

- AI x Canva SNS templates were introduced by Nishinippon Shimbun.
- A 60-year-old woman in Toyama grew from 220 to 10,000 followers using AI-made Canva SNS templates; there are multiple achievers.
- AI x Coconala automation earned two Platinum badges across seven operated accounts.
- Individual fortune-teller course/customer-acquisition support contributed more than JPY 4 million in increased sales.

Preferred header HTML:

```html
<div data-niji-office-results="v1" style="width:100%;max-width:100%;margin:0 auto 28px;box-sizing:border-box;border:1px solid #d9eeee;border-radius:8px;background:#ffffff;box-shadow:0 3px 12px rgba(20,83,104,0.10);overflow:hidden;text-align:left;">
  <div style="height:5px;background:linear-gradient(90deg,#31c8c1 0%,#6fb8ff 34%,#b390f4 66%,#ff77a8 100%);"></div>
  <div style="padding:17px 16px 15px;box-sizing:border-box;">
    <p style="margin:0 0 4px;text-align:center;font-size:19px;line-height:1.5;color:#123b68;font-weight:700;">虹オフィスの実績</p>
    <p style="margin:0 0 14px;text-align:center;font-size:13px;line-height:1.7;color:#3d7779;">占い師の集客・商品設計・AI活用をサポート</p>
    <div style="margin:0 0 8px;padding:10px 11px;box-sizing:border-box;border-left:4px solid #24bdb7;background:#effcfa;font-size:14px;line-height:1.75;color:#26364a;"><span style="color:#0faea7;font-weight:700;">✔</span> <a href="https://ameblo.jp/niji-offfice/entry-12975337022.html" target="_blank" rel="noopener noreferrer" style="color:#0b7f9b;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;"><strong>AI☓Canva SNSテンプレ</strong>が西日本新聞社に紹介されました！</a></div>
    <div style="margin:0 0 8px;padding:10px 11px;box-sizing:border-box;border-left:4px solid #4b9ff3;background:#f0f7ff;font-size:14px;line-height:1.75;color:#26364a;"><span style="color:#318bea;font-weight:700;">✔</span> AIで作るCanva SNSテンプレで富山の60歳のお婆ちゃんが、<strong style="color:#e94f86;">220→1万フォロワー達成</strong>　実績者多数</div>
    <div style="margin:0 0 8px;padding:10px 11px;box-sizing:border-box;border-left:4px solid #9873e6;background:#f7f3ff;font-size:14px;line-height:1.75;color:#26364a;"><span style="color:#8660da;font-weight:700;">✔</span> <strong>AI☓ココナラで自動化</strong>→プラチナバッジ2つ獲得（運用7社）</div>
    <div style="margin:0;padding:10px 11px;box-sizing:border-box;border-left:4px solid #ff6696;background:#fff2f7;font-size:14px;line-height:1.75;color:#26364a;"><span style="color:#f04f86;font-weight:700;">✔</span> 占い講座個別集客：<strong style="color:#e94f86;">売上upに400万円以上貢献</strong></div>
  </div>
</div>
```

## Fixed Article CTA Block

Every Niji Office Ameblo article should end with the same LINE consultation CTA in the article body HTML source. Add it at the very bottom of the article HTML after the readable-spacing pass.

Use one fixed block with the marker `data-niji-office-cta="line"` so the CTA can be replaced without duplication when an existing article is revised.

CTA intent:

- Lead readers from Ameblo to Niji Office LINE, then ask them to send `個別相談希望`.
- Make the support scope clear: Coconala customer acquisition, service/product design, profile and listing improvement, AI x Canva templates, automation support, and fortune-teller skill lessons.
- Keep the tone clean, friendly, pastel, and Coconala-like Niji Office branding. Do not imitate Coconala exactly.
- Use inline HTML styles for Ameblo stability.

Preferred CTA HTML:

```html
<div data-niji-office-cta="line" style="margin:34px 0 10px;padding:22px 18px;border:2px solid #7edfe0;border-radius:18px;background:linear-gradient(135deg,#f2ffff 0%,#fff5fb 58%,#f7f1ff 100%);text-align:center;box-shadow:0 6px 18px rgba(126,223,224,0.18);">
  <div style="display:inline-block;margin-bottom:10px;padding:5px 14px;border-radius:999px;background:#ffffff;color:#00a9b5;font-size:13px;font-weight:bold;border:1px solid #b9f1ef;">
    虹オフィスの個別相談
  </div>
  <div style="font-size:20px;line-height:1.7;font-weight:bold;color:#1f2f68;margin-bottom:12px;">
    占い師さんの集客・商品づくりを、<br>
    やさしく整えます。
  </div>
  <div style="font-size:14px;line-height:1.9;color:#333;margin-bottom:16px;">
    ココナラ集客、商品設計、プロフィール改善、AI×Canva活用、鑑定力講座まで。<br>
    「何から直せばいいか分からない」段階でも大丈夫です。
  </div>
  <div style="margin:0 auto 18px;max-width:460px;">
    <span style="display:inline-block;margin:3px;padding:5px 10px;border-radius:999px;background:#eaffff;color:#008c99;font-size:12px;font-weight:bold;">集客導線</span>
    <span style="display:inline-block;margin:3px;padding:5px 10px;border-radius:999px;background:#fff0f7;color:#e83f7d;font-size:12px;font-weight:bold;">商品設計</span>
    <span style="display:inline-block;margin:3px;padding:5px 10px;border-radius:999px;background:#f3edff;color:#7b55d9;font-size:12px;font-weight:bold;">AI×Canva</span>
    <span style="display:inline-block;margin:3px;padding:5px 10px;border-radius:999px;background:#eef6ff;color:#1d75d8;font-size:12px;font-weight:bold;">鑑定力講座</span>
  </div>
  <a href="https://lin.ee/ShPqtm8" target="_blank" rel="noopener noreferrer" style="display:inline-block;padding:14px 28px;border-radius:999px;background:#ff4f8b;color:#fff;text-decoration:none;font-size:17px;font-weight:bold;box-shadow:0 5px 14px rgba(255,79,139,0.30);">
    LINEで「個別相談希望」と送る
  </a>
  <div style="font-size:12px;color:#777;line-height:1.7;margin-top:14px;">
    売り込みではなく、今の状況を整理するところからで大丈夫です。
  </div>
</div>
```

## Validation

Before saving, compare:

- title matches the note source or user-approved Ameblo title,
- formatted HTML length is nonzero and contains expected image/link counts,
- spacing additions are present,
- no raw script or broken tag fragments were introduced.

After saving, reopen the edit list or public URL. Do not rely only on a button click.
