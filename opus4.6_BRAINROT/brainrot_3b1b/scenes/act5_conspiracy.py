from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.colors import *
from utils.morphing import *

class Act5Conspiracy(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        self.add_sound(os.path.abspath("assets/audio/05_gyatt_point.mp3"))
        
        # 1. Random Vector Field
        # Representing "Chaotic Data Points"
        vectors = VGroup()
        for i in range(5):
            for j in range(5):
                start = np.array([i - 2, j - 2, 0]) * 1.5
                # Random direction
                end = start + np.array([np.random.uniform(-1, 1), np.random.uniform(-1, 1), 0])
                arrow = Arrow(start, end, buff=0, color=GREY)
                vectors.add(arrow)
                
        self.play(ShowIncreasingSubsets(vectors), run_time=2)
        
        # 2. Text "Connecting the Gyatts"
        text = Text("Aligning the Data...", font_size=36, color=GREEN_E)
        text.to_edge(UP)
        self.play(Write(text))
        
        # 3. Align Vectors to form a specific shape (Triangle)
        # We manually construct a Triangle and align the vectors to its edges
        target_triangle = Triangle(color=GREEN_E).scale(3)
        
        # We transform the group of arrows into the triangle
        self.play(
            ReplacementTransform(vectors, target_triangle),
            run_time=2.5,
            rate_func=smooth
        )
        
        # 4. Reveal Illuminati
        illuminati = load_svg_centered("assets/svg/Illuminati.svg", height=5.0)
        
        # The triangle fits perfectly into the illuminati shape roughly
        self.play(
            ReplacementTransform(target_triangle, illuminati),
            run_time=1.0,
            rate_func=smooth
        )
        
        # 5. X-Files Aura
        # Flash the background Green slightly
        self.play(
            Flash(illuminati, color=GREEN_E, line_length=1.0, num_lines=12),
            illuminati.animate.scale(1.2),
            run_time=1.5
        )
        self.wait(1)
