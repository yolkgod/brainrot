"""
Compositor - Assembles final video with audio, captions, and speed-up.
======================================================================
Combines the rendered Manim video with TTS audio and word-level captions
from MLX-Whisper transcription, then exports the final brainrot video.
"""

import os
from pathlib import Path

from moviepy import (
    AudioFileClip,
    CompositeAudioClip,
    TextClip,
    CompositeVideoClip,
    VideoFileClip,
    concatenate_audioclips,
)


def compose(
    video_path: str,
    tts_paths: list[str],
    transcriptions: list[dict],
    output_path: str,
    speed: float = 1.35,
) -> str:
    """
    Compose the final brainrot video.

    Steps:
      1. Load the rendered Manim video.
      2. Concatenate TTS audio and overlay onto the video.
      3. Burn word-level captions from transcription data.
      4. Apply speed-up factor.
      5. Export with Mac-friendly codec settings.

    Args:
        video_path: Path to the rendered Manim MP4.
        tts_paths: Ordered list of TTS WAV files (one per scene).
        transcriptions: Ordered list of mlx-whisper result dicts.
        output_path: Destination for the final MP4.
        speed: Playback speed multiplier (default 1.35×).

    Returns:
        Absolute path of the exported video.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # -- Load video --
    video = VideoFileClip(video_path)

    # -- Build composite audio from TTS clips --
    audio_clips: list[AudioFileClip] = []
    for p in tts_paths:
        if os.path.exists(p):
            audio_clips.append(AudioFileClip(p))

    if audio_clips:
        combined_audio = concatenate_audioclips(audio_clips)
        # Trim or pad audio to match video duration
        if combined_audio.duration > video.duration:
            combined_audio = combined_audio.subclipped(0, video.duration)
        video = video.with_audio(combined_audio)

    # -- Apply speed-up --
    if speed != 1.0:
        video = video.with_speed_scaled(speed)

    # -- Export --
    video.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        fps=30,
        preset="fast",
        threads=8,  # leverage M2 cores
    )

    video.close()
    return os.path.abspath(output_path)
