"""
Act 2: The Setup (10-25s)
=========================
Problem introduction with SVG morphing and equation buildup.
"""

from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.colors import *
from utils.morphing import *


class Act2_TheSetup(Scene):
    """
    Introduce the "problem" with SVG morphing and equation reveal.
    Duration: ~15 seconds
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        
        # === BEAT 1: The Question (10-13s) ===
        question = Text(
            "What exactly... is Rizz?",
            font_size=42,
            color=TEXT_PRIMARY,
            font="Arial"
        )
        
        self.play(Write(question), run_time=1.5)
        self.wait(1.0)
        
        # Move question up to make room
        self.play(
            question.animate.to_edge(UP, buff=1.0),
            run_time=0.8
        )
        
        # === BEAT 2: SVG Morph - Brain to Moyai (13-18s) ===
        # Placeholder shapes (will be replaced with actual SVGs)
        brain_placeholder = Circle(
            radius=1.0,
            color=BLUE_C,
            fill_opacity=0.7
        )
        brain_label = Text("🧠", font_size=72)
        brain_group = VGroup(brain_placeholder, brain_label)
        brain_group.move_to(LEFT * 2)
        
        moyai_placeholder = Circle(
            radius=1.0,
            color=SIGMA_COLOR,
            fill_opacity=0.7
        )
        moyai_label = Text("🗿", font_size=72)
        moyai_group = VGroup(moyai_placeholder, moyai_label)
        moyai_group.move_to(LEFT * 2)
        
        # Show brain
        self.play(FadeIn(brain_group, scale=0.5), run_time=0.8)
        self.wait(0.5)
        
        # Morph brain to moyai
        self.play(
            ReplacementTransform(brain_group, moyai_group, path_arc=45 * DEGREES),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(0.3)
        
        # Move moyai to side
        self.play(
            moyai_group.animate.scale(0.6).to_edge(LEFT, buff=0.5),
            run_time=0.8
        )
        
        # === BEAT 3: Equation Buildup (18-25s) ===
        # Build the equation piece by piece
        eq_parts = VGroup(
            Text("R(t)", font_size=36, color=RIZZ_COLOR),
            Text(" = ", font_size=36, color=TEXT_PRIMARY),
            Text("∫", font_size=48, color=TEXT_PRIMARY),
            Text(" Aura(x)", font_size=32, color=AURA_COLOR),
            Text(" · ", font_size=36, color=TEXT_PRIMARY),
            Text("Sigma(x)", font_size=32, color=SIGMA_COLOR),
            Text(" dx", font_size=32, color=TEXT_PRIMARY),
        )
        eq_parts.arrange(RIGHT, buff=0.1)
        eq_parts.move_to(RIGHT * 1.5)
        
        # Animate each part appearing
        for i, part in enumerate(eq_parts):
            self.play(
                FadeIn(part, shift=UP * 0.2),
                run_time=0.4
            )
            if i == 2:  # Pause on integral
                self.wait(0.3)
        
        # Highlight the key term
        self.play(
            Circumscribe(eq_parts[0], color=RIZZ_COLOR, fade_out=True),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # Store for transition
        self.equation = eq_parts
        
        # Fade out for next scene
        self.play(
            FadeOut(question),
            FadeOut(moyai_group),
            eq_parts.animate.to_edge(UP, buff=0.5).scale(0.8),
            run_time=1.0
        )


# For SVG version (when assets are available)
class Act2_WithSVG(Scene):
    """
    Version using actual SVG files from vtracer.
    Replace placeholders with:
        brain_svg = load_svg("assets/svg/brain.svg", color=BLUE_C)
        moyai_svg = load_svg("assets/svg/moyai.svg", color=SIGMA_COLOR)
    """
    pass


if __name__ == "__main__":
    pass
