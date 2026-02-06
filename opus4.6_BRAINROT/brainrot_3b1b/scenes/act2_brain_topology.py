from manim import *
import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.colors import *
from utils.morphing import *

class Act2BrainTopology(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        audio_path = os.path.abspath("assets/audio/02_consider.mp3")
        self.add_sound(audio_path)

        # 1. Initial State: The Brain
        brain_svg = load_svg_centered("assets/svg/brain.svg", height=3.5)
        brain_svg.set_color(TEAL_E)
        
        title = Text("Consider the Topology", font_size=40, color=TEXT_SECONDARY)
        title.to_edge(UP)
        
        self.play(
            FadeIn(title, shift=DOWN),
            DrawBorderThenFill(brain_svg),
            run_time=2.0
        )
        self.wait(1)

        # 2. Rotation (Pseudo-3D)
        self.play(
            Rotate(brain_svg, angle=2*PI, axis=UP),
            run_time=3.0,
            rate_func=smooth
        )

        # 3. Create the field of Amogus
        # We want to replace the brain with many small impostors
        amogus_group = VGroup()
        for _ in range(20):
            # Random position within a rough circle
            radius = random.uniform(0, 2.5)
            angle = random.uniform(0, 2*PI)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            # Load amogus
            # Create a fresh copy for each instance avoids reference issues
            mob = load_svg("assets/svg/amogus.svg", height=0.5)
            mob.move_to([x, y, 0])
            
            # Random colors from our palette
            color = random.choice([RED_E, BLUE_C, YELLOW_E, BRAINROT_MAGENTA, BRAINROT_NEON_GREEN])
            mob.set_color(color)
            
            amogus_group.add(mob)

        # 4. The "Discovery" - It's made of Impostors
        self.play(
            TransformMatchingShapes(brain_svg, amogus_group),
            run_time=2.0,
            rate_func=smooth
        )
        
        # 5. Chaos ensues
        self.play(
            *[
                ApplyMethod(mob.shift, np.array([random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), 0])) 
                for mob in amogus_group
            ],
            run_time=1.0,
            rate_func=wiggle
        )
        self.wait(2)
