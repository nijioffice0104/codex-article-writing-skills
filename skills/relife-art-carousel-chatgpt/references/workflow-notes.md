# Relife Art carousel references

## Default Instagram/TikTok carousel size

- Instagram carousel: 720x900px unless the user specifies otherwise.
- TikTok carousel: 720x900px when the user says to use the same carousel format.
- Coconala banner sizes are different; do not apply 720x900px to Coconala unless explicitly instructed.

## Common failure patterns to guard against

- ChatGPT creates one image containing several pages.
- ChatGPT creates a wide banner or square image instead of 720x900.
- ChatGPT changes `魂のレシピ` into a new design style.
- A red tag, border, string, or title is cropped by the canvas edge.
- Japanese text is too small or corrupted.
- Each slide has a different unrelated world view.
- The assistant reports completion after only sending the prompt.

## Preferred status wording

- `指示送信済みです。まだ生成完了は未確認です。`
- `生成停止ボタンなし・エラーなしなので、生成完了状態です。`
- `画像数は確認できましたが、文字切れ検品はまだです。`
- `検品でデザイン違いを確認したため、再生成指示を送ります。`
