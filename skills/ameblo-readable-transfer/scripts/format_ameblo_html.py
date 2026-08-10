#!/usr/bin/env python3
import argparse
from html.parser import HTMLParser


SKIP_TAGS = {"script", "style", "pre", "code"}
BLOCK_TAGS = {"p", "li", "blockquote", "figcaption"}
BOUNDARIES = "、，,）)]】』」!！?？…：:"
CHUNKY_BLOCK_THRESHOLD = 165
SENTENCE_END_MARKS = {"。", "!", "！", "?", "？", "❓", "❗"}
ELLIPSIS_QUESTION_ENDINGS = {"…？", "...?", "...? ", "…?"}
EMOJI_JOINERS = {"\ufe0f", "\u200d", "•", "・"}
CLOSING_MARKS = {"」", "』", "）", ")", "]", "】", "》", "〉"}
CTA_MARKER = 'data-niji-office-cta="line"'
NIJI_OFFICE_LINE_CTA = f"""
<div {CTA_MARKER} style="margin:34px 0 10px;padding:22px 18px;border:2px solid #7edfe0;border-radius:18px;background:linear-gradient(135deg,#f2ffff 0%,#fff5fb 58%,#f7f1ff 100%);text-align:center;box-shadow:0 6px 18px rgba(126,223,224,0.18);">
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
""".strip()


def append_break_if_missing(out: list[str], rest: str) -> None:
    if not rest.startswith("<br><br>"):
        out.append("<br><br>")


def is_emoji_char(ch: str) -> bool:
    code = ord(ch)
    return (
        0x1F300 <= code <= 0x1FAFF
        or 0x2600 <= code <= 0x27BF
        or code in {0x3030, 0x303D, 0x3297, 0x3299}
    )


def add_sentence_spacing(
    text: str, count: int, every_sentence: bool = False
) -> tuple[str, int]:
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        out.append(ch)
        is_end = False
        if ch in SENTENCE_END_MARKS:
            is_end = True
            while i + 1 < len(text) and text[i + 1] in EMOJI_JOINERS | CLOSING_MARKS:
                i += 1
                out.append(text[i])
        elif is_emoji_char(ch):
            is_end = True
            while i + 1 < len(text) and (
                text[i + 1] in EMOJI_JOINERS or is_emoji_char(text[i + 1])
            ):
                i += 1
                out.append(text[i])
            while i + 1 < len(text) and text[i + 1] in CLOSING_MARKS:
                i += 1
                out.append(text[i])

        if is_end:
            count += 1
            if every_sentence or count % 2 == 0:
                append_break_if_missing(out, text[i + 1 : i + 12])
        i += 1
    return "".join(out), count


def add_long_block_spacing(text: str, threshold: int = CHUNKY_BLOCK_THRESHOLD) -> str:
    if len(text.strip()) < threshold:
        return text

    chunks = []
    current = []
    visible_len = 0
    i = 0
    while i < len(text):
        current.append(text[i])
        visible_len += 1
        if visible_len >= threshold:
            lookback = "".join(current)
            split_at = max(lookback.rfind(b) for b in BOUNDARIES)
            if split_at >= threshold // 2:
                left = lookback[: split_at + 1]
                right = lookback[split_at + 1 :]
                chunks.append(left)
                chunks.append("<br><br>")
                current = [right] if right else []
                visible_len = len(right)
        i += 1

    chunks.append("".join(current))
    return "".join(chunks)


def is_chunky_text(text: str, threshold: int = CHUNKY_BLOCK_THRESHOLD) -> bool:
    return len(text.strip()) >= threshold


def is_emotional_or_cta_text(text: str) -> bool:
    compact = text.strip()
    if not compact:
        return False
    hook_words = (
        "知りたくないですか",
        "できるとしたら",
        "もし、あなたが",
        "あなたが今",
        "次は、あなたの番",
        "ご相談ください",
        "お申込み",
        "申し込み",
        "ココナラ",
    )
    if any(word in compact for word in hook_words):
        return True
    if compact.startswith("「") and compact.endswith(("？」", "?」", "！」", "!」")):
        return True
    if compact.startswith("**") and compact.endswith("**"):
        return True
    return False


def is_parenthetical_aside(text: str) -> bool:
    compact = text.strip()
    return compact.startswith("（") and compact.endswith("）")


class AmebloFormatter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.out = []
        self.stack = []
        self.skip_depth = 0
        self.sentence_count = 0

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        if tag in SKIP_TAGS:
            self.skip_depth += 1
        attr_text = "".join(
            f' {name}' if value is None else f' {name}="{value}"'
            for name, value in attrs
        )
        self.out.append(f"<{tag}{attr_text}>")

    def handle_startendtag(self, tag, attrs):
        attr_text = "".join(
            f' {name}' if value is None else f' {name}="{value}"'
            for name, value in attrs
        )
        self.out.append(f"<{tag}{attr_text}>")

    def handle_endtag(self, tag):
        self.out.append(f"</{tag}>")
        if tag in SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if self.skip_depth:
            self.out.append(data)
            return
        in_block = bool(self.stack and self.stack[-1] in BLOCK_TAGS)
        single_sentence_spacing = in_block and (
            is_chunky_text(data) or is_emotional_or_cta_text(data) or is_parenthetical_aside(data)
        )
        text, self.sentence_count = add_sentence_spacing(
            data, self.sentence_count, every_sentence=single_sentence_spacing
        )
        if in_block and not any(mark in data for mark in SENTENCE_END_MARKS) and not any(
            is_emoji_char(ch) for ch in data
        ):
            text = add_long_block_spacing(text)
        if in_block and is_parenthetical_aside(data) and not text.rstrip().endswith("<br><br>"):
            text = text.rstrip() + "<br><br>"
        self.out.append(text)

    def handle_entityref(self, name):
        self.out.append(f"&{name};")

    def handle_charref(self, name):
        self.out.append(f"&#{name};")

    def get_html(self):
        return "".join(self.out)


def format_html(html: str) -> str:
    parser = AmebloFormatter()
    parser.feed(html)
    parser.close()
    return append_line_cta(parser.get_html())


def append_line_cta(html: str) -> str:
    if CTA_MARKER in html:
        before = html.split("<div " + CTA_MARKER, 1)[0].rstrip()
        return before + "\n\n" + NIJI_OFFICE_LINE_CTA + "\n"
    return html.rstrip() + "\n\n" + NIJI_OFFICE_LINE_CTA + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()
    with open(args.input, "r", encoding="utf-8-sig") as f:
        html = f.read()
    formatted = format_html(html)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(formatted)
    else:
        print(formatted)


if __name__ == "__main__":
    main()
