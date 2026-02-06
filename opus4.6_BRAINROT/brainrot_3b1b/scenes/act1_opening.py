from manim import *
import sys
import os

# Add the parent directory to sys.path to allow importing from utils
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.colors import *
from utils.morphing import *

class Act1Opening(Scene):
    def construct(self):
        # 1. Setup Background
        self.camera.background_color = BACKGROUND_DARK
        
        # 2. Add Audio
        # Note: Manim's add_sound generally needs absolute paths or relative to execution
        audio_path = os.path.abspath("assets/audio/01_opening.mp3")
        self.add_sound(audio_path)
        
        # 3. Create the Equation (Navier-Stokes)
        # using Text since LaTeX is not installed
        ns_equation = VGroup(
            Text("ρ(∂v/∂t + v·∇v)", font_size=40, color=BLUE_C),
            Text("=", font_size=40),
            Text("-∇p + μ∇²v + f", font_size=40, color=RED_E)
        ).arrange(RIGHT)
        ns_equation.scale(1.5)
        
        # 4. Animate Equation Entry (Standard 3B1B Reveal)
        self.play(Write(ns_equation), run_time=2.0)
        self.wait(1)
        
        # 5. Highlight the complexity
        self.play(
            ns_equation.animate.scale(1.2).set_color(TEXT_PRIMARY),
            run_time=1.0,
            rate_func=smooth
        )
        self.wait(0.5)
        
        # 6. The "Solution" Reveal - Morph to Skibidi
        # Load the SVG
        skibidi_svg = load_svg_centered("assets/svg/Skibidi_toilet.svg", height=4.0)
        
        # Text "The Solution"
        solution_text = Text("The Solution", font_size=48, color=HIGHLIGHT_PRIMARY)
        solution_text.move_to(UP * 3)
        
        self.play(Write(solution_text))
        
        # Perform the Morph
        # We transform the equation directly into the SVG
        self.play(
            ReplacementTransform(ns_equation, skibidi_svg, path_arc=PI/2),
            run_time=2.5,
            rate_func=smooth
        )
        
        # 7. Final Polish
        self.play(
            skibidi_svg.animate.scale(1.1).set_color(BRAINROT_CYAN),
            run_time=1.0,
            rate_func=there_and_back
        )
        self.wait(2)
