"""
Act 3: The Visualization (25-50s)
=================================
The hero scene: 3D Rizz Manifold with camera choreography.
"""

from manim import *
import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.colors import *
from utils.morphing import mascot_head_tilt, mascot_bounce
from utils.camera import orbit_3d, dramatic_3d_reveal


class Act3_TheVisualization(ThreeDScene):
    """
    The centerpiece: 3D surface with smooth camera work.
    Duration: ~25 seconds
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        
        # === BEAT 1: Equation Reminder (25-27s) ===
        equation_reminder = Text(
            "R(t) = ∫ Aura(x) · Sigma(x) dx",
            font_size=28,
            color=TEXT_SECONDARY,
            font="Arial"
        )
        equation_reminder.to_edge(UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(equation_reminder)
        self.play(FadeIn(equation_reminder), run_time=0.5)
        
        # === BEAT 2: 3D Setup (27-32s) ===
        # Start with flat camera angle for dramatic reveal
        self.set_camera_orientation(phi=10 * DEGREES, theta=-45 * DEGREES)
        
        # Create 3D axes with brainrot labels
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"color": BLUE_C, "stroke_width": 2}
        )
        
        # Labels
        x_label = Text("Skibidi", font_size=20, color=SKIBIDI_COLOR)
        y_label = Text("Aura", font_size=20, color=AURA_COLOR)
        z_label = Text("Rizz", font_size=20, color=RIZZ_COLOR)
        
        x_label.next_to(axes.x_axis.get_end(), RIGHT + DOWN * 0.3)
        y_label.next_to(axes.y_axis.get_end(), UP)
        z_label.next_to(axes.z_axis.get_end(), OUT + UP * 0.3)
        
        # The Rizz Manifold surface
        def rizz_manifold(u, v):
            x = u
            y = v
            # Complex wavy surface that looks "mathematical"
            z = (
                0.5 * np.sin(u * 1.5) * np.cos(v * 1.5) +
                0.3 * np.cos(u * 2 + v) +
                0.2 * np.sin(u - v * 0.5)
            )
            return np.array([x, y, z])
        
        surface = Surface(
            rizz_manifold,
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(32, 32),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, RIZZ_COLOR],
            stroke_color=WHITE,
            stroke_width=0.3
        )
        
        # Animate axes appearing
        self.play(Create(axes), run_time=1.5)
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.play(
            Write(x_label),
            Write(y_label),
            Write(z_label),
            run_time=0.8
        )
        
        # === BEAT 3: Dramatic Surface Reveal (32-37s) ===
        # Surface appears while camera tilts
        self.play(
            Create(surface),
            self.camera.animate.set_phi(70 * DEGREES),
            run_time=2.5,
            rate_func=smooth
        )
        
        # === BEAT 4: Orbit Sequence (37-43s) ===
        # Slow, elegant orbit
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(3)
        
        # === BEAT 5: Highlight the Peak (43-47s) ===
        self.stop_ambient_camera_rotation()
        
        # Add "Gyatt Point" label at a peak
        peak_label = Text(
            "Gyatt Point\n(Maximum Rizz)",
            font_size=16,
            color=BRAINROT_MAGENTA,
            font="Arial"
        )
        peak_label.move_to(np.array([0, 0, 1.5]))
        self.add_fixed_orientation_mobjects(peak_label)
        
        # Zoom camera slightly toward the peak
        self.play(
            FadeIn(peak_label, scale=0.5),
            self.camera.animate.set_theta(-30 * DEGREES),
            run_time=1.5
        )
        
        # === BEAT 6: Mascot Reaction (47-50s) ===
        # Placeholder for mascot - will be SVG
        mascot_placeholder = Text("🚽", font_size=48)
        mascot_placeholder.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(mascot_placeholder)
        
        self.play(FadeIn(mascot_placeholder, scale=0.5), run_time=0.5)
        
        # Head tilt reaction
        self.play(
            mascot_placeholder.animate.rotate(15 * DEGREES),
            run_time=0.3,
            rate_func=there_and_back
        )
        
        self.wait(0.5)
        
        # Store elements for transition
        self.surface = surface
        self.axes = axes


class Act3_QuickTest(ThreeDScene):
    """Minimal test version."""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        axes = ThreeDAxes()
        
        def simple_surface(u, v):
            return np.array([u, v, 0.5 * np.sin(u) * np.cos(v)])
        
        surface = Surface(
            simple_surface,
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, RIZZ_COLOR],
        )
        
        self.play(Create(axes), Create(surface))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)


if __name__ == "__main__":
    pass
