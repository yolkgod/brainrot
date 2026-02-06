"""
TTS Engine - Text-to-speech using pocket-tts.
==============================================
Generates speech audio for each scene's narration using the lightweight,
CPU-friendly pocket-tts library.
"""

import os
from pathlib import Path

import scipy.io.wavfile as wav
from pocket_tts import TTSModel


# Module-level cache so the model is loaded only once per process.
_model: TTSModel | None = None
_voice_state = None


def _get_model():
    """Lazy-load the TTS model and default voice."""
    global _model, _voice_state
    if _model is None:
        _model = TTSModel.load_model()
        _voice_state = _model.get_state_for_audio_prompt("alba")
    return _model, _voice_state


def synthesize(text: str, output_path: str) -> str:
    """
    Synthesize *text* to a WAV file at *output_path*.

    Args:
        text: The narration string.
        output_path: Destination .wav file path.

    Returns:
        Absolute path of the saved WAV.
    """
    model, voice = _get_model()
    audio = model.generate_audio(voice, text)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    wav.write(output_path, model.sample_rate, audio.cpu().numpy())
    return os.path.abspath(output_path)


def synthesize_scenes(scenes: list[dict], output_dir: str) -> list[str]:
    """
    Generate TTS audio for every scene.

    Args:
        scenes: List of scene dicts with ``narration`` keys.
        output_dir: Directory to write WAV files.

    Returns:
        Ordered list of WAV file paths.
    """
    paths: list[str] = []
    for scene in scenes:
        scene_id = scene["scene_id"]
        out = os.path.join(output_dir, f"tts_{scene_id}.wav")
        print(f"  Synthesizing TTS for scene {scene_id} …")
        path = synthesize(scene["narration"], out)
        paths.append(path)
    return paths
