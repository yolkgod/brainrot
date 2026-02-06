# 🧠 Brainrot Video Generator

AI-powered pipeline for generating chaotic "brainrot" educational videos using
Manim, Gemini, pocket-tts, and MLX-Whisper. Optimised for **Mac M2** (Apple Silicon).

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your-key-here"

# Generate a video with a random topic
python generate.py --random

# Generate a video with a specific topic
python generate.py --topic "The Thermodynamics of the Grimace Shake"
```

## Pipeline

| Step | Tool | What it does |
|------|------|-------------|
| 1. Script | Gemini 2.5 Flash | Writes a structured JSON script with scenes, narration, and math |
| 2. Images | Gemini 2.0 Flash | Generates scene background art (no static assets needed) |
| 3. TTS | pocket-tts | Synthesizes narration audio for each scene |
| 4. Transcribe | mlx-whisper | Word-level timestamps for caption sync (Apple Silicon GPU) |
| 5. Render | Manim (Cairo) | Renders chaotic 9:16 animations (1080×1920) |
| 6. Composite | MoviePy | Layers audio + video, 1.35× speed-up, final export |

## Requirements

- Python 3.10+
- macOS with Apple Silicon (M1/M2/M3) recommended for MLX-Whisper
- `GEMINI_API_KEY` environment variable
- FFmpeg (`brew install ffmpeg`)

## Project Structure

```
brainrot/
├── generate.py              # CLI entry point (--random / --topic)
├── requirements.txt         # Python dependencies
├── brainrot/                # Core pipeline modules
│   ├── script_writer.py     # Gemini script generation
│   ├── image_generator.py   # Gemini image generation
│   ├── tts_engine.py        # pocket-tts synthesis
│   ├── transcriber.py       # MLX-Whisper transcription
│   ├── renderer.py          # Manim scene rendering
│   └── compositor.py        # Final video assembly
└── opus4.6_BRAINROT/        # Original brainrot reference
    ├── brain_rot.md          # The brainrot philosophy guide
    └── brainrot_3b1b/        # Original 3B1B-style implementation
```

## Reference

See [opus4.6_BRAINROT/brain_rot.md](opus4.6_BRAINROT/brain_rot.md) for the
complete brainrot philosophy, aesthetic rules, and content strategy guide.
