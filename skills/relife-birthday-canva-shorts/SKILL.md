---
name: relife-birthday-canva-shorts
description: Support AI and Codex-assisted fortune-teller audience growth by planning, producing, publishing, and reporting reusable promotion workflows. Use when the user asks for AI☓codex占い師集客支援スキル, 占い師集客支援, Relife波動タロット YouTube Shorts, 誕生日占いランキング, Canva batch generation, fixed-audio muxing, YouTube posting, Notion reporting, or says スサノオで. The current implemented workflow creates, edits, audio-muxes, publishes, and verifies 神仏・開運・奇跡・守護・運命成就系 birthday-ranking Shorts from the approved Canva master, including the スサノオ source template, using fixed user-owned audio https://youtube.com/shorts/JR4FWOICOKA.
---

# AI☓codex占い師集客支援スキル

## Scope

This is the umbrella skill for AI and Codex-assisted fortune-teller audience growth.

The currently implemented production workflow is:

- Relife波動タロット向け誕生日占いYouTube Shorts
- Canva 5ページランキング動画
- 神仏・開運・奇跡・守護・運命成就系ネタ
- 固定音源 `JR4FWOICOKA` の合成
- YouTube投稿
- 公開状態と音声ありの検証
- Notion報告

Do not present this as a generic topic-generation skill. When posting is requested, carry the workflow through Canva creation, audio, upload, public verification, and reporting.

## Reporting Destination

Report future work for this skill to the Codex data-stock Notion page:

`https://app.notion.com/p/3b4dd83d18cb8159b907c930dac95466?pvs=204`

Use the linked operational memo when a detailed runbook is needed:

`https://app.notion.com/p/3b7dd83d18cb815d9b04c7ee32531e69`

## Golden Path

Run the workflow through posting, not just Canva editing.

1. Copy the approved Canva master template. Never edit the master directly.
2. Generate a fresh 5-page birthday-ranking concept set.
3. Validate title and appraisal character counts before Canva editing.
4. Edit only the intended Canva text fields and any user-specified background.
5. Preview all 5 pages, save/commit, and export the finished Canva video.
6. Add the fixed user-owned source audio before upload.
7. Verify the final MP4 has video and audio streams.
8. Publish to the connected Relife波動タロット YouTube account.
9. If Canva posts as private, open YouTube Studio, set visibility to public, and save.
10. Verify the public Shorts URL and audio availability.
11. Log/report the result to the Notion reporting page.

## Template Presets

Always copy the requested source template first. Never edit a source/master directly.

Default approved master template:

`https://www.canva.com/d/7ytV2frE7VcK71H`

Susanoo source template:

- Trigger phrase: `スサノオで`
- User shortlink: `https://canva.link/k1wrwwz7uc1s83g`
- Resolved design ID: `DAHBvlvQ5C0`
- Confirmed title: `誕生日占いアニメーション`
- Confirmed page count: 5
- Use this source whenever the user says `スサノオで`, `スサノオ版`, or gives the same shortlink. Copy it with `copy-design`, then run the normal 5-page birthday-ranking workflow.

Fixed audio source for future runs:

`https://youtube.com/shorts/JR4FWOICOKA`

Bundled audio asset, if present:

`assets/JR4FWOICOKA_audio.mp3`

## Simple Execution Mode

When the user says to keep it simple, save credits, or avoid making the PC heavy:

- Do not generate extra images, extra design variants, or long visual QA unless needed to catch a known failure.
- Prefer one Canva copy, one validated text draft, one export, one audio mux, one upload, and one final public/audio verification.
- Close unnecessary Canva or Studio tabs after they are no longer needed.
- Report only the result, public URL, final local file path, and any real blocker.
- Still do the minimum safety checks: title/appraisal counts, Mode Mincho/style preservation, audio stream presence, public visibility, and final URL.

## Content Rules

Create one vertical YouTube Shorts set with 5 pages. Each page is one theme and ranks 5 birthdays.

Allowed topic family only:

- 神仏
- 開運
- 奇跡
- 守護
- 守護神
- 守護霊
- ご先祖
- 供養
- 神様
- 仏様
- 七福神
- 龍神
- 天使
- 一粒万倍日
- 金運
- 良縁
- 運命の人
- 厄落とし
- 願いが叶う
- 人生好転

Use seasonal terms when they fit the timing, such as お盆, 供養, ご先祖, 迎え火, 送り火, 盆の祈り. Do not use seasonal words mechanically when they do not fit the theme.

Do not create pages that are only romance, only personality diagnosis, only scary prophecy, or only a psychology test. Romance is allowed only when framed as 良縁, 運命成就, 神仏の導き, or 開運.

## Title Rules

Titles are strict and must be validated before editing Canva.

- Count the complete displayed title after removing line breaks.
- Each title must be 14 to 16 Japanese characters.
- Do not lazily end titles with `誕生日占い`.
- In a 5-page batch, use five different ending patterns.
- Make titles sharp and varied without becoming fear-based.
- Include occasional command-style endings such as `受け取るべし`, `飛び込むべし`, `見落とすな`, `逃すな`, `動き出す人`.
- Avoid repeating the same structure, suffix, or emotional hook across pages.

Approved tone examples:

- `強き守護神の加護を受け取るべし`
- `龍神の大金脈へ今飛び込むべし`
- `七福神の大福徳を今日授かる人`
- `強い守護霊の合図を見落とすな`
- `奇跡の良縁へ今すぐ動き出す人`

## Appraisal Rules

Small appraisal lines are strict.

- Each 小文字鑑定 must be 14 to 15 Japanese characters.
- Keep each line short, mystical, positive, and save-worthy.
- Avoid visual overflow by using compact phrases.
- Do not repeat the same wording pattern too often.

## Ranking Rules

- Use `1日` through `31日`.
- Do not use impossible dates such as `33日` unless the user explicitly requests a special-number format.
- Within one page, never repeat a birthday date.
- Across different pages, birthday dates may repeat unless the user says not to.
- Use persuasive numerology-flavored logic, but do not over-explain inside the Canva video.

## Canva Editing Rules

Use the Canva connector whenever possible.

1. Copy the master with `copy-design` first unless the user explicitly says the current design is already a copy.
2. Start an editing transaction and inspect all 5 pages.
3. Identify only these editable text groups on each page:
   - theme title
   - `1位` to `5位` birthday text, such as `17日生まれ`
   - each rank's 小文字鑑定
4. Edit the 55 intended text fields only: 5 pages times 11 text fields.
5. Do not edit loading animations, rank reveal timing, CTA/follow banners, page count, or layout unless explicitly requested.
6. Preserve Mode Mincho / モード明朝 and existing text styling. If one page differs, align it to page 1 styling.
7. Put each page title into a clean two-line layout when the template is built that way. Align all 5 title boxes to the same font, size, center alignment, and visual position; do not leave one page with a different title design.
8. If the user specifies a background, use that exact background. If the background is already set, do not touch image/fill elements.
9. If the user asks for the local protective talisman background, look under Downloads for `【２号店】梵語の護符２` and use one suitable talisman image consistently across all 5 pages unless instructed otherwise.
10. Apply edits page by page or in multiple phases if safer.
11. Preview all 5 pages before commit.
12. Commit/save when the user approves, or when the active conversation includes standing save approval such as `保存OK この許可は不要`.
13. Save a local control text file under the current task output folder with final text, Canva URL, audio source, posting notes, and Notion report status.

## Text Validation

Before editing Canva, draft the 5 titles and 25 小文字鑑定 lines in a UTF-8 text file.

Run:

```powershell
python C:\Users\suket\.codex\skills\relife-birthday-canva-shorts\scripts\validate_counts.py <draft.txt>
```

The checker expects lines beginning with:

- `タイトル：`
- `小文字鑑定：`

Fix all NG lines before Canva entry.

## Fixed Audio Workflow

The user owns the source Short and wants this audio reused every time:

`https://youtube.com/shorts/JR4FWOICOKA`

Use the bundled MP3 if it exists. If it is missing, extract the audio from the user-owned source Short and save it locally before continuing. Do not substitute arbitrary external audio.

Preferred reliable route:

1. Export the finished Canva design as an MP4.
2. Use `ffprobe` to confirm the raw export is 9:16 video, usually 1080x1920.
3. Use `ffmpeg` to mux the fixed MP3 into the exported MP4.
4. Use the media checker to verify the final MP4 contains both a video stream and an audio stream.
5. Only then upload or publish.

Run:

```powershell
python C:\Users\suket\.codex\skills\relife-birthday-canva-shorts\scripts\check_media_streams.py <final.mp4>
```

Canva preloaded-audio option:

- If a verified Canva base already contains the exact fixed audio, it may be used.
- Do not assume Canva preserved audio. Export and verify the MP4 before posting.
- If audio is missing after export, fall back to the MP3 + ffmpeg route.

## Publishing Route

Publishing is part of the skill.

Primary route:

1. Publish the verified audio-included video to the connected Relife波動タロット YouTube account.
2. Use fresh title/description based on the current 5-page content. Do not reuse previous post copy blindly.
3. Verify the final public Shorts URL.

Reliable Canva fallback used successfully on 2026-08-10:

1. Upload the final audio-included MP4 to Canva as a video asset.
2. Copy the Canva design as a one-page publishing copy.
3. Insert the final MP4 full-frame at `left=0`, `top=0`, `width=1080`, `height=1920`.
4. Commit the one-page publishing copy.
5. Publish this one-page copy through Canva's YouTube app.
6. In this fallback only, selecting `1ページ（現在のページ）` is correct because that one page contains the complete final video.
7. If Canva creates a private video, open YouTube Studio, change visibility to `公開`, and save.

Do not publish a normal 5-page Canva design while the page selection is only `1ページ（現在のページ）`; that posts only one page. The one-page exception applies only after the final full MP4 has been inserted into a single-page publishing copy.

## Final Verification

Treat the task as incomplete until all are true:

- Canva design was saved/committed.
- Exported/final MP4 has video and audio streams.
- The uploaded YouTube Short is public.
- The public Short has audio formats or plays with audio.
- A local log records the final Canva URL, YouTube URL, title, description or hashtags, source audio, final MP4 path, verification result, and Notion report status.
- The Codex data-stock Notion page has been updated when the user requested posting/reporting.

If an audio-less video is accidentally uploaded, delete it or keep it private according to the user's latest instruction. In the 2026-08-10 run, the user instructed deletion of the accidental no-audio upload.

## Do Not Repeat These Mistakes

- Do not confuse the umbrella title with the implemented workflow. The menu title is `AI☓codex占い師集客支援スキル`; the current workflow is birthday-ranking Shorts production.
- Do not stop after topic generation; complete Canva, audio, posting, verification, and reporting when posting is requested.
- Do not edit the master template.
- Do not ignore `スサノオで`; it means copy and use the Susanoo source template `DAHBvlvQ5C0`.
- Do not use `誕生日占い` as an easy repeated title ending.
- Do not use the same title ending pattern across all 5 pages.
- Do not create 小文字鑑定 shorter than 14 characters.
- Do not change the user's specified background.
- Do not change Mode Mincho / モード明朝 styling.
- Do not leave titles on mismatched fonts, one-line/uneven layouts, or jagged placement when the user asked for clean two-line titles.
- Do not treat a thumbnail or title match as proof; inspect the actual pages.
- Do not leave Canva edits uncommitted after save approval.
- Do not publish before audio is included.
- Do not claim audio is attached unless the final MP4 or final YouTube page proves it.
- Do not claim YouTube posting is complete until the public Shorts URL works.
