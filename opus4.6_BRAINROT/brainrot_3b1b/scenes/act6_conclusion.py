from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.colors import *
from utils.morphing import *

class Act6Conclusion(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        self.add_sound(os.path.abspath("assets/audio/07_educational.mp3"))
        
        # 1. Final Statement
        statement = Text("Therefore, sticking out your Gyatt...", font_size=32)
        statement.move_to(UP * 1)
        
        statement2 = Text("...is purely topological.", font_size=32, color=YELLOW_E)
        statement2.next_to(statement, DOWN)
        
        self.play(Write(statement), run_time=1.5)
        self.play(Write(statement2), run_time=1.5)
        
        self.wait(1)
        
        # 2. Q.E.D. Box
        qed_box = Square(side_length=0.5, fill_color=WHITE, fill_opacity=1, color=WHITE)
        qed_box.next_to(statement2, RIGHT, buff=0.5)
        
        qed_text = Text("Q.E.D.", font_size=24)
        qed_text.next_to(qed_box, DOWN)
        
        self.play(DrawBorderThenFill(qed_box), Write(qed_text))
        
        # 3. The Final Stamp (Moai)
        # It should fall from the top
        moai = load_svg_centered("assets/svg/moai.svg", height=4.0)
        moai.move_to(UP * 4) # Start off screen
        
        # "Thud" effect
        self.play(
            moai.animate.move_to(ORIGIN),
            run_time=0.4,
            rate_func=rush_into
        )
        self.add_sound("assets/audio/bass_hit.mp3") # Optional impact sound
        
        # Camera Shake on impact
        self.play(
            self.camera.frame.animate.shift(DOWN * 0.1),
            run_time=0.05
        )
        self.play(
            self.camera.frame.animate.shift(UP * 0.1),
            run_time=0.05
        )
        
        self.wait(2)
