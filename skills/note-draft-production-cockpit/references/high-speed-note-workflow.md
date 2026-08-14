# High-Speed Note Workflow

## Intake Checklist

Capture these before editing:

- Target note URL or local manuscript path
- Whether text is already pasted into note
- User instruction mode: decoration-only or rewrite/edit allowed
- Title and first line
- H2 count and current table of contents
- Exact requested image count, if any
- Thumbnail requirement and size
- In-article image requirement and mapping
- Required tool, especially Blog Generator Pro
- Reference image style and prohibited elements
- Public/private state and save target

## Blog Generator Pro Rule

If the user names Blog Generator Pro or the Coconala / note production cockpit, find that exact local tool or browser tab first. Known clues from prior work:

- Cockpit name: `Coconala / note production cockpit`
- Tool name: `Blog Generator Pro`
- Purpose: blog article, thumbnail, and in-article image prompt generation in one flow
- Prior local clue: `blog-oneclick.html`

Do not replace BGP with a generic prompt, manual formatting, or another project tool unless the user explicitly authorizes that change. If BGP is unreachable, report:

- searched paths or tabs
- exact URL or file attempted
- error text or observable blocker
- which work can continue without violating the user's rules

## Prose Rules

If editing is allowed:

- Prioritize the first line after the title.
- Make the opening specific, surprising, and connected to the reader's problem.
- Keep the tone at about practical textbook 7, human spoken explanation 3.
- Use natural connectors such as `で、`, `なので、`, `つまり、`, `ただ、`, `実際、`, and `ちなみに` where they improve flow.
- Use `〜なんです。` sparingly to soften stiff explanation.
- Do not use exaggerated promises, fabricated outcomes, or unsupported numbers.

If decoration-only:

- Do not rewrite sentences.
- Do not change claims, examples, numbers, titles, or CTA.
- Limit changes to heading levels, bold, bullets, spacing, separators, and image insertion.

## Note Decoration Rules

- Set true H2 formatting for all large headings.
- Use H3 only when it reduces confusion inside a long H2 section.
- Bold only scan-worthy phrases, numbers, named concepts, and conclusions.
- Convert 3 or more short parallel lines into bullets when it improves readability.
- Keep the article mostly prose. Do not turn the whole article into bullets.
- Remove production notes, prompt text, diagnostic logs, and image-generation instructions from the final note body.

## Image Planning

Before generation, create an internal table:

| No | File name | Insert position | Role | Visual form | Required text |
| --- | --- | --- | --- | --- | --- |
| 01 | 01_thumbnail.png | thumbnail/top | Whole article promise | Eye-catch | Title or short hook |
| 02 | 02_h2-01_overview.png | H2-1 direct child | Concept | Diagram | Short Japanese labels |

Image count rules:

- Thumbnail is counted separately unless the user says total includes it.
- For "H2 image under every large heading", count every H2 first and create one image per H2.
- If the user later says "total N including thumbnail", remap transparently and do not create extra images.
- Do not create several near-identical images. Vary layouts such as hub-and-spoke, before/after, pipeline, checklist, map, comparison, dashboard, staircase, and summary board.

## Image Design Rules

Default note explainer style:

- 1280 x 670 px unless the user specifies another size
- white or very light gray background
- clean diagram layout
- pastel base with orange accent when Coconala/note business content is involved
- flat icons or silhouettes only
- readable Japanese text included when the user asks for explainer images
- short labels, arrows, circles, badges, underlines, and `POINT` chips

Prohibited:

- unrelated stock photos
- copied third-party logos or brand names
- watermarks
- tiny unreadable Japanese
- too much text
- collage or multi-design grids
- generated numbers not present in the manuscript
- duplicate or near-duplicate designs

## Image Generation and Storage

- Generate by batch when the active ChatGPT relay can handle it. Use batches of up to 10 images.
- If only single image calls are available, keep the accepted images and continue sequentially without regenerating accepted work.
- Save files under a dedicated local folder, for example:

```text
deliverables/note-production/<article-slug>/
  reference/
  thumbnail/
  body/
  rejected/
  prompts/
  verification/
```

- Name files with stable numbers and purpose:

```text
01_thumbnail.png
02_h2-01_overview.png
03_h2-02_before-after.png
```

- Check dimensions, file size if required, visual readability, and duplicate hashes or obvious duplicate screenshots before upload.

## Note Insertion Rules

- Insert the thumbnail in the note thumbnail/cover field when available, not merely at the top of the body, unless the platform blocks cover upload.
- Insert body images immediately under their mapped H2 or mapped paragraph.
- Work from top to bottom to preserve order.
- After image insertion, inspect the editor DOM or rendered view to ensure images are not all grouped at the end.
- Save draft and reload or reopen the exact edit URL when possible.

## Recovery Rules

- If upload fails, retry the specific upload once or twice, then preserve local files and report the blocker.
- If one generated image fails, regenerate only that image.
- If formatting fails in a live editor, preserve the local decorated HTML/Markdown and report which visual state was verified.
- If the browser loses the target tab, reopen the exact note URL and inspect state before continuing.
- If a publish preflight opens, do not publish.

## Completion Report

Report every item explicitly:

- Blog Generator Pro: used or not used; if not, why
- Target note URL
- Article state: draft/unpublished or blocker
- Text mode: decoration-only or edited
- H2 count
- Requested image count
- Thumbnail created and inserted
- Body images created and inserted
- Image count matches mapping
- Design requirements honored
- Image size and readability checked
- Headings, bold, bullets, separators checked
- No production notes or prompt text remain
- No duplicate or near-duplicate images
- Saved/reopened verification performed
- Items not completed and exact reason, or `なし`
