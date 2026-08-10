---
name: canva-instagram-reel-posting
description: Publish completed Canva vertical videos to Instagram Reels, including BGM checks, caption entry, optional Codex heartbeat posting at specified times, Threads cross-post prevention, account verification, and final Reel/profile proof. Use when the user asks to post, schedule-by-Codex, reserve, or manually publish Canva designs to Instagram, especially Relife birthday compatibility/ranking reels.
---

# Canva Instagram Reel Posting

## Core Rule

Treat Canva-to-Instagram work as incomplete until the actual Instagram result is verified. Do not stop at Canva save, Canva share-panel success, or a queued Codex reminder.

If the user asks for "reservation" but Canva scheduling is blocked by Meta/Facebook business connection, create Codex heartbeat automations for the requested times and use this thread to execute the live posting at each time.

## Required Tools

- Use the Canva connector for design metadata, page count, thumbnails, copies, and edit URLs.
- Use Chrome/browser control for Canva's Instagram share panel and live Instagram verification.
- Use Codex automations for "Codex will post at 20:00" style thread wakeups.
- If the task depends on current browser login state, verify the real tab state rather than assuming it persists.

## Posting Workflow

1. Confirm the intended Canva design ID, edit URL, title, page count, and visible content.
2. Confirm the design has suitable BGM. If audio was added in Canva UI, verify the track label and save state; if exporting locally, verify the final MP4 audio stream.
3. Open Canva's share panel and choose Instagram.
4. Select `Reel (video)` / `リール（動画）`.
5. Confirm the design is a multi-page reel. In Canva's Instagram panel, `ページを選択` can refer to the cover image; do not mistake cover selection for exporting only one page.
6. Set the cover to page 1 unless the user requests a different cover.
7. Enter a fresh caption matched to the theme. Use clipboard paste when Canva's caption field is inside an iframe or shadow-like UI.
8. Confirm the posting account, usually shown in the Instagram panel. For this workflow, the expected account has been `talot_relife_fukuoka` or the task-specific variant shown by Canva; report the exact visible account.
9. Check for Threads, Facebook, or cross-post toggles. Turn Threads sharing off unless the user explicitly asks for it.
10. Publish through Canva only when all visible settings are correct.
11. After publishing, open the resulting Instagram Reel URL and profile. Verify the account, Reel visibility, caption association, and normal profile/grid presence.

## Codex Heartbeat Posting

Use heartbeat automations when the user wants Codex to post later from this same task.

- Use one heartbeat per post date/time when each post has a distinct design, caption, or verification requirement.
- Anchor the time with an explicit timezone, e.g. Asia/Tokyo 20:00.
- Include the exact Canva edit URL, title, caption, BGM, target Instagram account, Threads-off requirement, and verification requirement in each automation prompt.
- If the automation tool rejects direct `DTSTART` on create, retry with `mode: suggested_create`.
- Explain that this is not true platform-side scheduling: Codex wakes and attempts the live post at that time.
- State the operational dependency plainly: the PC/session/browser must be available enough for Codex to control Canva and Instagram. If the PC is powered off, sleeping, offline, or logged out, Codex may wake but cannot complete browser-based posting without user action.

## Meta/Facebook Scheduling Block

Canva's native `予約投稿` can require connecting an Instagram business account through Facebook/Meta.

When the panel shows `FacebookでInstagramのビジネスアカウントと連携`:

- Do not claim Canva-side scheduling is complete.
- Try the connection flow only until it reaches a login or permissions page.
- If Facebook credentials or permissions are required, stop and ask the user to complete that step.
- Keep the live Canva/Meta state clear in the handoff.
- Offer the Codex heartbeat posting route as the fallback when the user accepts live-time posting instead of native Canva scheduling.

## Verification Standard

Report completion only after all relevant checks pass:

- Canva design saved.
- BGM present or final media has audio.
- Instagram format is Reel/video.
- Target account is verified on screen or final profile.
- Threads/cross-posting is off when requested.
- Final Reel URL is opened and the public result is visible.

If any item cannot be verified, say exactly which item is blocked and what user action is needed.

## Reference

For the 2026-08-10 Relife birthday compatibility batch and exact dates/captions, read `references/2026-08-10-relife-instagram-batch.md`.
