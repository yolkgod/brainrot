"""
Transcriber - Word-level transcription using MLX-Whisper.
==========================================================
Uses mlx-whisper with the ``whisper-large-v3-turbo`` model (optimised for
Apple Silicon) to produce word-level timestamps for caption sync.
"""

import mlx_whisper

# HuggingFace repo for the MLX-optimised large model.
MODEL_REPO = "mlx-community/whisper-large-v3-turbo"


def transcribe(audio_path: str) -> dict:
    """
    Transcribe an audio file and return word-level timestamps.

    Args:
        audio_path: Path to a WAV/MP3 file.

    Returns:
        The full mlx-whisper result dict containing ``text`` and ``segments``
        (each segment has a ``words`` list when ``word_timestamps=True``).
    """
    result = mlx_whisper.transcribe(
        audio_path,
        path_or_hf_repo=MODEL_REPO,
        word_timestamps=True,
    )
    return result


def transcribe_scenes(audio_paths: list[str]) -> list[dict]:
    """
    Transcribe a list of audio files (one per scene).

    Args:
        audio_paths: Ordered list of audio file paths.

    Returns:
        List of transcription result dicts (one per scene).
    """
    results: list[dict] = []
    for i, path in enumerate(audio_paths, 1):
        print(f"  Transcribing scene {i} …")
        results.append(transcribe(path))
    return results
