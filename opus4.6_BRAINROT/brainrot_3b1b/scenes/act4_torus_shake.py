from manim import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.colors import *
from utils.morphing import *

class Act4TorusShake(ThreeDScene):
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        self.add_sound(os.path.abspath("assets/audio/04_rizz_manifold.mp3"))
        
        # 1. Setup 3D Camera
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        
        # 2. Create Torus (The "Rizz Manifold")
        torus = Torus(major_radius=2, minor_radius=0.8, resolution=(16, 16))
        torus.set_color(color=BRAINROT_MAGENTA)
        torus.set_opacity(0.8)
        
        # Add labels in 3D space
        label = Text("The Manifold", font_size=36).to_corner(UL)
        self.add_fixed_in_frame_mobjects(label)
        
        self.play(Create(torus), Write(label))
        
        # Rotate it
        self.begin_ambient_camera_rotation(rate=0.4)
        self.play(torus.animate.rotate(PI, axis=RIGHT), run_time=2)
        
        # 3. Morph to Grimace Shake
        # Important: Stop camera rotation and reset for flat SVG view
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1.5)
        
        # Load Grimace Shake
        shake = load_svg_centered("assets/svg/grimace_shake.svg", height=4.5)
        # Svg is 2D, make sure it's visible in our 3D scene (on Z=0 plane)
        
        # The Torus needs to flatten or just transform
        # We can treat the torus as a mobject
        
        self.play(
            ReplacementTransform(torus, shake),
            run_time=2.0,
            rate_func=smooth
        )
        
        # 4. Shake Effect
        # A literal shake for the shake
        self.play(
            shake.animate.scale(1.2), # Bulge
            rate_func=wiggle,
            run_time=1.0
        )
        
        # Color shift to purple
        self.play(
            shake.animate.set_color(PURPLE_E),
            run_time=0.5
        )
        self.wait(1)
