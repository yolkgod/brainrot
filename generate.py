#!/usr/bin/env python3
"""
generate.py — Brainrot Video Generator CLI
============================================
One-command pipeline to generate AI-powered brainrot videos.

Usage:
    # Random topic
    python generate.py --random

    # Specific topic
    python generate.py --topic "The Thermodynamics of the Grimace Shake"

Environment:
    GEMINI_API_KEY  — required for script writing and image generation.

Optimised for Mac M2 (Apple Silicon).
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from brainrot.script_writer import generate_script, pick_random_topic
from brainrot.image_generator import generate_scene_images
from brainrot.tts_engine import synthesize_scenes
from brainrot.transcriber import transcribe_scenes
from brainrot.renderer import render
from brainrot.compositor import compose

# ---------------------------------------------------------------------------
# Directories
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
ASSETS_DIR = OUTPUT_DIR / "generated_assets"
AUDIO_DIR = OUTPUT_DIR / "audio"
MEDIA_DIR = OUTPUT_DIR / "media"


def banner():
    print(
        r"""
 ____  ____    _    ___ _   _ ____   ___ _____
| __ )|  _ \  / \  |_ _| \ | |  _ \ / _ \_   _|
|  _ \| |_) |/ _ \  | ||  \| | |_) | | | || |
| |_) |  _ </ ___ \ | || |\  |  _ <| |_| || |
|____/|_| \_\_/   \_\___|_| \_|_| \_\\___/ |_|

   AI-Powered Brainrot Video Generator
   Gemini Script · Gemini Images · Pocket-TTS · MLX-Whisper · Manim
"""
    )


def run_pipeline(topic: str):
    """Execute the full brainrot generation pipeline."""
    start = time.time()

    # -- Prepare directories --
    for d in (OUTPUT_DIR, ASSETS_DIR, AUDIO_DIR, MEDIA_DIR):
        d.mkdir(parents=True, exist_ok=True)

    # -- Step 1: Generate script --
    print("\n🧠 Step 1/5 — Generating script with Gemini …")
    print(f"   Topic: {topic}")
    script = generate_script(topic)
    script_path = OUTPUT_DIR / "script.json"
    script_path.write_text(json.dumps(script, indent=2))
    print(f"   ✓ Script saved to {script_path}")
    print(f"   Title: {script['title']}")
    print(f"   Scenes: {len(script['scenes'])}")

    # -- Step 2: Generate images --
    print("\n🎨 Step 2/5 — Generating images with Gemini …")
    image_paths = generate_scene_images(script["scenes"], str(ASSETS_DIR))
    print(f"   ✓ {len(image_paths)} images generated")

    # -- Step 3: Generate TTS audio --
    print("\n🔊 Step 3/5 — Generating TTS with pocket-tts …")
    tts_paths = synthesize_scenes(script["scenes"], str(AUDIO_DIR))
    print(f"   ✓ {len(tts_paths)} audio clips generated")

    # -- Step 4: Transcribe for captions --
    print("\n📝 Step 4/5 — Transcribing with MLX-Whisper …")
    transcriptions = transcribe_scenes(tts_paths)
    print(f"   ✓ {len(transcriptions)} transcriptions complete")

    # -- Step 5: Render with Manim --
    print("\n🎬 Step 5/5 — Rendering with Manim (Mac M2 optimised) …")
    video_path = render(script, image_paths, str(MEDIA_DIR))
    print(f"   ✓ Rendered: {video_path}")

    # -- Step 6: Composite final video --
    print("\n🔧 Compositing final video …")
    final_path = str(OUTPUT_DIR / "final_brainrot.mp4")
    result = compose(video_path, tts_paths, transcriptions, final_path)
    print(f"   ✓ Final video: {result}")

    elapsed = time.time() - start
    print(f"\n✅ Done in {elapsed:.1f}s")
    return result


def main():
    banner()

    parser = argparse.ArgumentParser(
        description="Generate AI-powered brainrot videos.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python generate.py --random\n"
            '  python generate.py --topic "Sigma Male as a Markov Chain"\n'
        ),
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--random",
        action="store_true",
        help="Pick a random brainrot topic.",
    )
    group.add_argument(
        "--topic",
        type=str,
        help="Specify a custom topic for the video.",
    )

    args = parser.parse_args()

    # Validate environment
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable is not set.")
        print("   Get a key at https://ai.google.dev/")
        sys.exit(1)

    topic = args.topic if args.topic else pick_random_topic()
    run_pipeline(topic)


if __name__ == "__main__":
    main()
