from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.colors import *
from utils.morphing import *

class Act3RizzLimit(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        
        # Audio
        self.add_sound(os.path.abspath("assets/audio/03_skibidi_infinity.mp3"))
        
        # 1. Setup Graph
        axes = Axes(
            x_range=[-1, 10, 1],
            y_range=[-2, 6, 1],
            x_length=9,
            y_length=5,
            axis_config={"color": BLUE_D},
        )
        
        # Manual Labels (No LaTeX)
        x_label = Text("Rizz", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Aura", font_size=24).next_to(axes.y_axis, UP)
        axes_labels = VGroup(x_label, y_label)
        
        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        
        # 2. Graph a function (Logarithmic growth)
        graph = axes.plot(lambda x: np.log(x + 1) * 2, color=YELLOW_E)
        
        # Manual graph label
        graph_label = Text("f(x) = ln(Mewing)", font_size=24, color=YELLOW_E)
        graph_label.next_to(graph, UP)
        
        self.play(Create(graph), Write(graph_label), run_time=1.5)
        
        # 3. The Sigma Summation visual
        # "The sum of all Rizz..."
        sigma_math = Text("Σ Looksmax(n) = Sigma", font_size=40)
        sigma_math.scale(1.5)
        sigma_math.set_color(TEXT_PRIMARY)
        sigma_math.move_to(UP * 2 + RIGHT * 2)
        
        self.play(Write(sigma_math))
        self.wait(1)
        
        # Focus on the Sigma symbol alone
        # We create a standalone Sigma for the morph target source
        sigma_symbol = Text("Σ", font_size=144).set_color(SIGMA_COLOR)
        sigma_symbol.move_to(ORIGIN)
        
        # Transition everything else away, keep the concept of Sigma
        self.play(
            FadeOut(axes), FadeOut(axes_labels), FadeOut(graph), FadeOut(graph_label),
            ReplacementTransform(sigma_math, sigma_symbol)
        )
        
        # 4. The Morph
        # Load Sigma Male SVG
        sigma_male = load_svg_centered("assets/svg/sigma_male.svg", height=5.0)
        
        # Dramatic pause
        self.wait(0.5)
        self.add_sound(os.path.abspath("assets/audio/06_sigma_equals.mp3"))
        
        # Morph
        self.play(
            ReplacementTransform(sigma_symbol, sigma_male),
            run_time=2.0,
            rate_func=smooth
        )
        
        # 5. Intense Stare Effect (Zoom in)
        self.play(
            self.camera.frame.animate.scale(0.6).move_to(sigma_male.get_top() + DOWN * 1.5),
            run_time=3.0,
            rate_func=linear
        )
        
        # Flash eyes (simple circles)
        left_eye = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(sigma_male.get_top() + DOWN * 1.0 + LEFT * 0.5)
        right_eye = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(sigma_male.get_top() + DOWN * 1.0 + RIGHT * 0.5)
        
        self.play(FadeIn(left_eye), FadeIn(right_eye), run_time=0.1)
        self.play(Indicate(left_eye, scale_factor=2), Indicate(right_eye, scale_factor=2))
