"""
Audio Compositor for Brainrot Video - ALL TTS (Speedup)
=======================================================
Includes ALL TTS lines sped up by 1.45x to fit 17s.
Reduced Vine Booms as requested.
"""

import os
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

# ============================================================================
# PATHS
# ============================================================================
ASSET_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(ASSET_DIR, "assets", "audio")
VIDEO_DIR = os.path.join(ASSET_DIR, "media", "videos", "chaotic_main", "1920p15")

VIDEO_INPUT = os.path.join(VIDEO_DIR, "ChaoticBrainrot.mp4")
VIDEO_OUTPUT = os.path.join(ASSET_DIR, "final_output.mp4")

def audio_path(name):
    return os.path.join(AUDIO_DIR, name)

# ============================================================================
# TIMING MAP - TIGHT FIT (1.45x Speedup)
# ============================================================================
# Video is ~17.3s. TTS total at 1.45x is ~16.9s.

TTS_TIMING = [
    (0.0, "01_opening.mp3"),          
    (2.6, "02_consider.mp3"),         
    (4.2, "03_skibidi_infinity.mp3"), 
    (6.6, "04_rizz_manifold.mp3"),    
    (9.0, "05_gyatt_point.mp3"),     
    (11.8, "06_sigma_equals.mp3"),    
    (15.2, "07_educational.mp3"),     
]

# Reduced SFX - only key moments
SFX_TIMING = [
    (0.0, "vine_boom.mp3"),           # Opening
    (6.5, "bass_hit.mp3"),            # Graph transition
    (12.0, "vine_boom.mp3"),          # Proof reveal
    (14.5, "modem_screech.mp3"),      # Singularity
    (16.8, "discord_ping.mp3"),       # End
]

# ============================================================================
# AUDIO PROCESSING
# ============================================================================

def load_audio_with_timing(timing_list, video_duration, speed_factor=1.0):
    """Load audio clips, speed them up, and set timing."""
    clips = []
    
    for start_time, filename in timing_list:
        filepath = audio_path(filename)
        if os.path.exists(filepath):
            try:
                clip = AudioFileClip(filepath)
                
                # Apply speedup if needed
                if speed_factor != 1.0:
                    clip = clip.with_speed_scaled(speed_factor)
                
                clip = clip.with_start(start_time)
                clips.append(clip)
                
                end_time = start_time + clip.duration
                print(f"  ✓ {filename} ({speed_factor}x): {start_time:.1f}s - {end_time:.1f}s")
            except Exception as e:
                print(f"  ✗ Failed: {filename}: {e}")
        else:
            print(f"  ✗ Not found: {filepath}")
    
    return clips


def create_audio_mix(video_duration):
    """Create the complete audio mix."""
    # TTS with 1.45x speedup to fit everything
    print("\n=== Loading TTS (1.45x Speedup) ===")
    tts_clips = load_audio_with_timing(TTS_TIMING, video_duration, speed_factor=1.45)
    
    # SFX normal speed
    print("\n=== Loading SFX ===")
    sfx_clips = load_audio_with_timing(SFX_TIMING, video_duration, speed_factor=1.0)
    
    # Boost SFX volume
    boosted_sfx = [clip.with_volume_scaled(1.5) for clip in sfx_clips]
    
    # Combine
    all_clips = tts_clips + boosted_sfx
    
    if not all_clips:
        print("\n✗ No audio clips!")
        return None
    
    print(f"\n=== Total: {len(all_clips)} clips ===")
    return CompositeAudioClip(all_clips)


def composite_video_with_audio():
    """Add audio to video."""
    print("\n" + "="*50)
    print("BRAINROT AUDIO COMPOSITOR (FINAL)")
    print("="*50)
    
    print(f"\nLoading: {VIDEO_INPUT}")
    if not os.path.exists(VIDEO_INPUT):
        print("✗ Video not found!")
        return
    
    video = VideoFileClip(VIDEO_INPUT)
    print(f"  Duration: {video.duration:.2f}s")
    
    audio_mix = create_audio_mix(video.duration)
    if audio_mix is None:
        video.close()
        return
    
    print("\n=== Compositing ===")
    final = video.with_audio(audio_mix)
    
    print(f"\n=== Exporting ===")
    final.write_videofile(
        VIDEO_OUTPUT,
        codec="libx264",
        audio_codec="aac",
        fps=30,
        preset="fast"
    )
    
    print(f"\n✓ DONE: {VIDEO_OUTPUT}")
    video.close()


if __name__ == "__main__":
    composite_video_with_audio()
