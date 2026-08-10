# Niji Office note to Ameblo Operations

## Targets

- note source: `https://note.com/niji_office`
- Ameblo account: `niji-offfice`
- public blog: `https://ameblo.jp/niji-offfice/`
- LINE CTA: `https://lin.ee/ShPqtm8`
- newspaper article: `https://ameblo.jp/niji-offfice/entry-12975337022.html`

Never store passwords, one-time codes, or browser cookies in the skill, Notion, GitHub, logs, or reports.

## One Run

1. Read the note profile and collect article URLs shaped as `/n/<note-key>` in source order.
2. Read the authenticated Ameblo article list and collect article ID, title, state, date, and time.
3. Compare by stored note key first, then use title and source links as supporting evidence.
4. Select no more than four unseen note keys.
5. Fetch each note body from `https://note.com/api/v3/notes/<note-key>`.
6. Preserve wording, images, links, and source order. Apply only the approved readable-spacing transformation.
7. Add exactly one results header and exactly one LINE CTA.
8. Save as a draft first and reopen the exact edit page.
9. Assign the next open future reservation slots, with no more than two posts on one day: `07:00` and `20:00`.
10. Reopen the article list and public preview. Verify IDs, titles, states, dates, times, image widths, links, and markers.
11. Record the note-key-to-Ameblo-ID mapping and the completion time.
12. Stop after four articles. Do not start another transfer batch for at least four hours.

## Readability

- Meatball blocks are forbidden.
- In ordinary prose, insert visual breathing room after two sentence endings.
- Treat `。`, `！`, `!`, `？`, `?`, and sentence-ending emoji as endings.
- When a block reaches roughly four or five mobile lines, allow spacing after one ending.
- Emotional hooks, bold questions, asides, and CTA lead-ins should usually stand alone.
- Never split URLs, HTML tags, attributes, embedded cards, or code blocks.

## Fixed Article Structure

Order the body as follows:

1. results header: `data-niji-office-results="v1"`
2. transferred and formatted note body
3. LINE CTA: `data-niji-office-cta="line"`
4. optional approved mobile banner: `data-niji-office-mobile-banner="automation"`

Deduplicate each marker before saving. A fixed block must appear zero or one time, never twice.

The results item about the newspaper must link to the newspaper-report Ameblo article. The CTA must link to LINE and instruct the reader to send `個別相談希望`.

## Publication Safety

- New transfers start as drafts.
- Immediate publication requires an explicit article-level instruction from the user.
- Future reservations use only `07:00` and `20:00` and remain in note source order.
- Layout-only work must preserve the existing state: draft, future reservation, or public.
- Never click `投稿する` merely to save HTML, headers, CTA, banners, or spacing on a draft.
- A future-dated item may display `全員に公開` in the Ameblo list. Verify the future date and exact time before deciding that it is already live.

## Thumbnail Safety

Ameblo may choose a body image as the article-list thumbnail. CSS display rules do not prevent this selection.

For every banner change:

1. inspect the dedicated cover image,
2. inspect the public `entrylist.html` thumbnail,
3. confirm the banner is not silently replacing a topic-specific thumbnail,
4. preserve a no-link requirement when specified,
5. verify the visible image stays inside the article width on mobile.

If the fixed banner becomes the thumbnail unexpectedly, stop propagation and report the affected article IDs before revising more articles.

## Backlog Complete Mode

The backlog is complete only when every note key currently visible on the note profile maps to one verified Ameblo article.

After completion:

- monitor the note profile for unseen keys,
- transfer new keys in source order,
- use the same four-article batch and four-hour cooldown,
- keep publication at two posts per day,
- do nothing when no unseen key exists,
- report the checked coverage and `NO_CHANGE`.

## Required Verification Report

Report these fields after every run:

- checked note coverage and newest note key,
- selected note keys,
- Ameblo article IDs and titles,
- draft, reservation, or public state,
- exact reservation date and time,
- results-header count,
- CTA count,
- mobile-banner count,
- public thumbnail result,
- horizontal-overflow result,
- duplicate and skipped-item list,
- earliest allowed next batch time.
