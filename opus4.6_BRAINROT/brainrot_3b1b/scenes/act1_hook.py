"""
Act 1: The Hook (0-10s)
========================
Title sequence with elegant reveal and first morph.
"""

from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.colors import *
from utils.morphing import *


class Act1_TheHook(Scene):
    """
    The opening hook - elegant title that morphs into brainrot.
    Duration: ~10 seconds
    """
    
    def construct(self):
        # Set elegant dark background
        self.camera.background_color = BACKGROUND_DARK
        
        # === BEAT 1: Title Fade In (0-3s) ===
        title = Text(
            "The Mathematics of Rizz",
            font_size=56,
            color=TEXT_PRIMARY,
            font="Arial"
        )
        
        subtitle = Text(
            "Advanced Topics in Theoretical Brainrot",
            font_size=28,
            color=TEXT_SECONDARY,
            font="Arial"
        )
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Elegant fade in
        self.play(
            FadeIn(title, shift=UP * 0.3),
            run_time=1.5
        )
        self.play(
            Write(subtitle),
            run_time=1.2
        )
        self.wait(0.5)
        
        # === BEAT 2: The Morph (3-7s) ===
        # "Advanced Topics" morphs into "Skibidi Studies"
        new_subtitle = Text(
            "Skibidi Studies",
            font_size=28,
            color=BRAINROT_CYAN,
            font="Arial"
        )
        new_subtitle.move_to(subtitle.get_center())
        
        # Smooth morph with slight path arc
        self.play(
            ReplacementTransform(subtitle, new_subtitle, path_arc=30 * DEGREES),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Flash highlight on the new text
        self.play(
            Indicate(new_subtitle, color=BRAINROT_MAGENTA, scale_factor=1.2),
            run_time=0.5
        )
        
        # === BEAT 3: Clear for Next Scene (7-10s) ===
        self.wait(0.5)
        
        # Elegant fade out
        self.play(
            FadeOut(title, shift=UP * 0.3),
            FadeOut(new_subtitle, shift=DOWN * 0.3),
            run_time=1.0
        )
        
        # Brief pause before next act
        self.wait(0.3)


# Quick test
if __name__ == "__main__":
    pass
