import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_counts.py <draft.txt>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    ok = True
    seen = {"title": 0, "appraisal": 0}

    for line_no, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip().lstrip("\ufeff")
        if line.startswith("タイトル："):
            value = line.split("：", 1)[1].replace("\n", "")
            count = len(value)
            seen["title"] += 1
            if not 14 <= count <= 16:
                ok = False
                print(f"NG title line {line_no}: {count} chars: {value}")
            else:
                print(f"OK title line {line_no}: {count} chars: {value}")
        elif line.startswith("小文字鑑定："):
            value = line.split("：", 1)[1].replace("\n", "")
            count = len(value)
            seen["appraisal"] += 1
            if not 14 <= count <= 15:
                ok = False
                print(f"NG appraisal line {line_no}: {count} chars: {value}")
            else:
                print(f"OK appraisal line {line_no}: {count} chars: {value}")

    if seen["title"] == 0:
        ok = False
        print("NG: no タイトル： lines found")
    if seen["appraisal"] == 0:
        ok = False
        print("NG: no 小文字鑑定： lines found")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
