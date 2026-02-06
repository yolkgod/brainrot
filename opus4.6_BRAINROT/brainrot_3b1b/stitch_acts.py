import os
from moviepy import *

# Define the sequence of files
# These paths are based on the standard Manim output structure for -ql (480p15)
clips_paths = [
    "media/videos/act1_opening/480p15/Act1Opening.mp4",
    "media/videos/act2_brain_topology/480p15/Act2BrainTopology.mp4",
    "media/videos/act3_rizz_limit/480p15/Act3RizzLimit.mp4",
    "media/videos/act4_torus_shake/480p15/Act4TorusShake.mp4",
    "media/videos/act5_conspiracy/480p15/Act5Conspiracy.mp4",
    "media/videos/act6_conclusion/480p15/Act6Conclusion.mp4"
]

clips = []
for path in clips_paths:
    if os.path.exists(path):
        print(f"Loading {path}...")
        clips.append(VideoFileClip(path))
    else:
        print(f"WARNING: File not found: {path}")

if clips:
    print("Concatenating clips...")
    final_clip = concatenate_videoclips(clips)
    
    # Increase speed to 1.35x as requested by user
    print("Applying speedup (1.35x)...")
    final_clip = final_clip.with_speed_scaled(1.35)
    
    output_path = "final_brainrot_3b1b.mp4"
    print(f"Writing final video to {output_path}...")
    final_clip.write_videofile(output_path, fps=15) # Match the input fps
    print("Done!")
else:
    print("No clips found to concatenate.")
