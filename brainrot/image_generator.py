"""
Image Generator - Creates visual assets using Gemini native image generation.
==============================================================================
Uses gemini-2.0-flash-exp for native image generation to create brainrot
visual assets (backgrounds, meme images, diagrams) without static files.
"""

import os
from pathlib import Path

from google import genai
from google.genai import types

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
IMAGE_MODEL = "gemini-2.0-flash-exp"


def _get_client() -> genai.Client:
    """Return a configured Gemini client."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY environment variable is required. "
            "Get one at https://ai.google.dev/"
        )
    return genai.Client(api_key=api_key)


def generate_image(prompt: str, output_path: str) -> str:
    """
    Generate a single image from a text prompt using Gemini native image
    generation and save it to *output_path*.

    Args:
        prompt: Descriptive image generation prompt.
        output_path: File path to save the resulting image (PNG).

    Returns:
        The absolute path of the saved image.
    """
    client = _get_client()

    response = client.models.generate_content(
        model=IMAGE_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["Image", "Text"],
        ),
    )

    # Walk through parts and save the first image
    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            return os.path.abspath(output_path)

    raise RuntimeError(f"No image returned by Gemini for prompt: {prompt!r}")


def generate_scene_images(scenes: list[dict], output_dir: str) -> list[str]:
    """
    Generate images for every scene in a script.

    Args:
        scenes: List of scene dicts, each containing an ``image_prompt`` key.
        output_dir: Directory where images will be saved.

    Returns:
        List of file paths for the generated images (one per scene).
    """
    paths: list[str] = []
    for scene in scenes:
        scene_id = scene["scene_id"]
        prompt = (
            f"{scene['image_prompt']}. "
            "Style: vibrant neon colors on dark background, "
            "9:16 vertical aspect ratio, digital art, "
            "high contrast brainrot aesthetic, glowing elements."
        )
        out = os.path.join(output_dir, f"scene_{scene_id}.png")
        print(f"  Generating image for scene {scene_id} …")
        path = generate_image(prompt, out)
        paths.append(path)
    return paths
