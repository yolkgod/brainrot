"""
Camera Choreography Utilities
=============================
3Blue1Brown-style camera movements: smooth zooms, orbits, focus tracking.
"""

from manim import *
import numpy as np

# ============================================================================
# 2D CAMERA MOVEMENTS (For Scene class)
# ============================================================================
def zoom_to_object(scene, target, zoom_factor=2.0, run_time=2.0):
    """
    Smoothly zoom the camera to focus on a specific object.
    Works with standard Scene (2D).
    """
    scene.play(
        scene.camera.frame.animate.set_width(
            target.get_width() * zoom_factor
        ).move_to(target),
        run_time=run_time,
        rate_func=smooth
    )


def zoom_out_full(scene, run_time=1.5):
    """Reset camera to full frame view."""
    scene.play(
        scene.camera.frame.animate.set_width(config.frame_width).move_to(ORIGIN),
        run_time=run_time,
        rate_func=smooth
    )


def pan_to_object(scene, target, run_time=1.5):
    """Pan camera to center on an object without changing zoom."""
    scene.play(
        scene.camera.frame.animate.move_to(target),
        run_time=run_time,
        rate_func=smooth
    )


def dramatic_zoom_in(scene, target, final_width=3.0, run_time=1.5):
    """
    Dramatic zoom into an object - good for equation reveals.
    """
    scene.play(
        scene.camera.frame.animate.set_width(final_width).move_to(target),
        run_time=run_time,
        rate_func=rush_into  # Accelerating zoom
    )


def slow_zoom_out(scene, run_time=3.0):
    """Very slow zoom out for contemplative moments."""
    scene.play(
        scene.camera.frame.animate.set_width(config.frame_width * 1.2).move_to(ORIGIN),
        run_time=run_time,
        rate_func=smooth
    )


# ============================================================================
# 3D CAMERA MOVEMENTS (For ThreeDScene class)
# ============================================================================
def orbit_3d(scene, rate=0.15, duration=3.0):
    """
    Smooth ambient camera rotation for 3D scenes.
    Classic 3B1B 3D graph presentation.
    """
    scene.begin_ambient_camera_rotation(rate=rate)
    scene.wait(duration)
    scene.stop_ambient_camera_rotation()


def zoom_to_3d_object(scene, target, phi=70, theta=-45, distance=8, run_time=2.0):
    """
    Move 3D camera to focus on a specific object.
    
    Args:
        phi: Polar angle (tilt up/down) in degrees
        theta: Azimuthal angle (rotation around z) in degrees
        distance: Distance from target
    """
    scene.move_camera(
        phi=phi * DEGREES,
        theta=theta * DEGREES,
        frame_center=target.get_center(),
        run_time=run_time
    )


def dramatic_3d_reveal(scene, initial_phi=0, final_phi=70, run_time=2.0):
    """
    Dramatic camera tilt from flat to 3D perspective.
    Great for revealing 3D surfaces.
    """
    scene.move_camera(
        phi=final_phi * DEGREES,
        run_time=run_time,
        rate_func=smooth
    )


def top_down_view(scene, run_time=1.5):
    """Switch to top-down view of 3D scene."""
    scene.move_camera(
        phi=0,
        theta=-90 * DEGREES,
        run_time=run_time
    )


def side_view(scene, run_time=1.5):
    """Switch to side view of 3D scene."""
    scene.move_camera(
        phi=90 * DEGREES,
        theta=0,
        run_time=run_time
    )


# ============================================================================
# FOCUS TRACKING (Keep camera on moving object)
# ============================================================================
class CameraFollower:
    """
    Utility class to make camera follow a moving object.
    """
    def __init__(self, scene, target, smoothing=0.1):
        self.scene = scene
        self.target = target
        self.smoothing = smoothing
        self._active = False
    
    def start(self):
        """Start following the target."""
        self._active = True
        def updater(frame, dt):
            if self._active:
                current = frame.get_center()
                target = self.target.get_center()
                new_pos = current + self.smoothing * (target - current)
                frame.move_to(new_pos)
        
        self.scene.camera.frame.add_updater(updater)
        self._updater = updater
    
    def stop(self):
        """Stop following."""
        self._active = False
        self.scene.camera.frame.remove_updater(self._updater)


# ============================================================================
# PRESET CAMERA SEQUENCES
# ============================================================================
def equation_focus_sequence(scene, equation, key_term=None):
    """
    Standard sequence: show equation, zoom to key term, zoom out.
    """
    scene.wait(0.5)
    if key_term:
        zoom_to_object(scene, key_term, zoom_factor=3.0, run_time=1.5)
        scene.wait(1.0)
    zoom_out_full(scene, run_time=1.0)


def reveal_sequence_3d(scene, surface):
    """
    Reveal a 3D surface with dramatic camera work.
    """
    # Start from flat view
    scene.set_camera_orientation(phi=10 * DEGREES, theta=-45 * DEGREES)
    scene.play(Create(surface), run_time=2.0)
    
    # Dramatic tilt to 3D
    dramatic_3d_reveal(scene, initial_phi=10, final_phi=70, run_time=2.0)
    
    # Slow orbit
    orbit_3d(scene, rate=0.1, duration=3.0)
