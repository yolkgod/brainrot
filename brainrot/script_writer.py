"""
Script Writer - Generates brainrot video scripts using Gemini.
===============================================================
Uses gemini-2.5-flash-preview-04-17 to write chaotic educational brainrot scripts
with structured scene breakdowns, TTS lines, and image prompts.
"""

import json
import os
import random

from google import genai
from google.genai import types

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_MODEL = "gemini-2.5-flash-preview-04-17"

RANDOM_TOPICS = [
    "The Navier-Stokes Equation of Rizz",
    "Topological Proof that Ohio is a Myth",
    "Sigma Male Grindset as a Markov Chain",
    "The Skibidi Toilet Hydrodynamics Problem",
    "Why Mewing Maximizes Jawline Eigenvalues",
    "Aura Points and the Riemann Hypothesis",
    "The Fanum Tax: A Game Theory Analysis",
    "Gyatt Distribution in Non-Euclidean Space",
    "Proving P = NP Using Brainrot",
    "The Thermodynamics of the Grimace Shake",
    "Looksmaxxing as Gradient Descent",
    "The Drake Equation but for Rizz",
    "Why Gen Alpha Speaks in Fourier Transforms",
    "Quantum Entanglement of Skibidi and Sigma",
    "The Fractal Geometry of TikTok Algorithms",
]

SYSTEM_PROMPT = """\
You are a brainrot video script writer in the style of 3Blue1Brown meets
internet brain-rot culture. You produce scripts for short-form vertical
videos (30-60 seconds) that apply serious math/science presentation to
absurd Gen-Alpha meme concepts.

RULES:
- The script must have 5-7 scenes.
- Each scene needs: narration text (1-2 sentences), a visual description
  for an image prompt, and a list of on-screen math/text elements.
- Use brainrot vocabulary: Skibidi, Sigma, Rizz, Ohio, Gyatt, Aura, Mog,
  Fanum Tax, Mewing, Looksmaxxing, etc.
- Include at least 2 fake LaTeX-style equations.
- The tone is deadpan educational — present memes as if they are
  serious academic discoveries.
- Keep narration SHORT and punchy for TTS.

OUTPUT FORMAT — respond with ONLY valid JSON matching this schema:
{
  "title": "string",
  "scenes": [
    {
      "scene_id": 1,
      "narration": "TTS text for this scene",
      "image_prompt": "Detailed image generation prompt for background visual",
      "math_elements": ["LaTeX string or on-screen text"],
      "duration_hint": 5
    }
  ]
}
"""


def _get_client() -> genai.Client:
    """Return a configured Gemini client."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY environment variable is required. "
            "Get one at https://ai.google.dev/"
        )
    return genai.Client(api_key=api_key)


def pick_random_topic() -> str:
    """Return a random brainrot topic."""
    return random.choice(RANDOM_TOPICS)


def generate_script(topic: str) -> dict:
    """
    Generate a brainrot video script for the given topic.

    Args:
        topic: The brainrot topic to write about.

    Returns:
        Parsed JSON dict with title and scenes list.
    """
    client = _get_client()

    response = client.models.generate_content(
        model=SCRIPT_MODEL,
        contents=f"Write a brainrot video script about: {topic}",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=1.0,
            max_output_tokens=2048,
        ),
    )

    raw = response.text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
    if raw.endswith("```"):
        raw = raw.rsplit("```", 1)[0]
    raw = raw.strip()

    script = json.loads(raw)
    return script
