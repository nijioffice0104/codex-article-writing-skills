import json
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_media_streams.py <video.mp4>", file=sys.stderr)
        return 2

    video_path = Path(sys.argv[1])
    if not video_path.exists():
        print(f"NG: file not found: {video_path}", file=sys.stderr)
        return 1

    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        print("NG: ffprobe was not found on PATH", file=sys.stderr)
        return 1

    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(video_path),
        ],
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stderr.strip() or "NG: ffprobe failed", file=sys.stderr)
        return 1

    data = json.loads(result.stdout)
    streams = data.get("streams", [])
    video_streams = [s for s in streams if s.get("codec_type") == "video"]
    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]
    duration = float(data.get("format", {}).get("duration") or 0)

    ok = True
    if not video_streams:
        ok = False
        print("NG: no video stream")
    if not audio_streams:
        ok = False
        print("NG: no audio stream")
    if duration <= 0:
        ok = False
        print("NG: duration is zero")

    if ok:
        first_video = video_streams[0]
        first_audio = audio_streams[0]
        print(
            "OK: video={width}x{height} audio={audio_codec} duration={duration:.3f}s".format(
                width=first_video.get("width", "?"),
                height=first_video.get("height", "?"),
                audio_codec=first_audio.get("codec_name", "?"),
                duration=duration,
            )
        )
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
