"""
Smooth Morphing Utilities
=========================
3Blue1Brown-style smooth transitions, SVG loading, and morph helpers.
"""

from manim import *
import numpy as np

# ============================================================================
# SVG LOADING HELPERS
# ============================================================================
def load_svg(filepath, color=None, height=2.0):
    """
    Load an SVG file and prepare it for animation.
    
    Args:
        filepath: Path to SVG file (from vtracer output)
        color: Fill color for the SVG (None to keep original)
        height: Target height (maintains aspect ratio)
    
    Returns:
        SVGMobject ready for animation
    """
    svg = SVGMobject(filepath)
    if color is not None:
        svg.set_color(color)
    svg.set_height(height)
    return svg


def load_svg_centered(filepath, color=None, height=2.0):
    """Load SVG and center it at origin."""
    svg = load_svg(filepath, color, height)
    svg.move_to(ORIGIN)
    return svg


# ============================================================================
# SMOOTH MORPH TRANSFORMS
# ============================================================================
def smooth_morph(scene, source, target, run_time=2.0, path_arc=0):
    """
    3B1B-style smooth morph between two objects.
    Uses ReplacementTransform for cleaner transitions.
    
    Args:
        scene: The Manim scene
        source: Starting mobject
        target: Ending mobject
        run_time: Duration of morph
        path_arc: Arc of the transformation path (0 = straight line)
    """
    scene.play(
        ReplacementTransform(source, target, path_arc=path_arc),
        run_time=run_time,
        rate_func=smooth
    )
    return target


def glitch_morph(scene, source, target, run_time=2.0):
    """
    Chaotic "glitch" morph with particles flying in loops.
    Uses path_arc = PI * 4 for maximum chaos.
    """
    scene.play(
        Transform(source, target, path_arc=PI * 4),
        run_time=run_time,
        rate_func=linear  # No smoothing for uncanny effect
    )
    return source


def text_to_svg_morph(scene, text_mob, svg_mob, run_time=2.0):
    """
    Morph text into an SVG shape.
    Useful for "Word Reification" effects.
    """
    # Match positions
    svg_mob.move_to(text_mob.get_center())
    return smooth_morph(scene, text_mob, svg_mob, run_time)


# ============================================================================
# HIGHLIGHTING (3B1B Style)
# ============================================================================
def highlight_term(scene, mobject, color, run_time=0.5, scale=1.2):
    """
    Highlight a term by changing its color and slightly scaling up.
    Classic 3B1B attention-directing technique.
    """
    scene.play(
        mobject.animate.set_color(color).scale(scale),
        run_time=run_time,
        rate_func=there_and_back_with_pause
    )


def indicate_with_flash(scene, mobject, color=YELLOW, run_time=0.8):
    """Flash a mobject to draw attention."""
    scene.play(
        Indicate(mobject, color=color, scale_factor=1.3),
        run_time=run_time
    )


def circumscribe_term(scene, mobject, color=YELLOW, run_time=1.0):
    """Draw a circle/rectangle around a term to highlight it."""
    scene.play(
        Circumscribe(mobject, color=color, fade_out=True),
        run_time=run_time
    )


# ============================================================================
# BUILD-UP ANIMATIONS (Piece by Piece)
# ============================================================================
def write_equation_parts(scene, equation_parts, colors=None, wait_time=0.3):
    """
    Write an equation piece by piece with optional coloring.
    
    Args:
        scene: Manim scene
        equation_parts: List of Text/MathTex mobjects
        colors: Optional list of colors for each part
        wait_time: Pause between each part
    """
    if colors is None:
        colors = [WHITE] * len(equation_parts)
    
    for part, color in zip(equation_parts, colors):
        part.set_color(color)
        scene.play(Write(part), run_time=0.8)
        scene.wait(wait_time)


def fade_in_sequence(scene, mobjects, direction=UP, lag_ratio=0.2, run_time=2.0):
    """
    Fade in multiple objects in sequence with a slight delay.
    Creates a "cascading" appearance effect.
    """
    animations = [
        FadeIn(mob, shift=direction * 0.3)
        for mob in mobjects
    ]
    scene.play(
        LaggedStart(*animations, lag_ratio=lag_ratio),
        run_time=run_time
    )


# ============================================================================
# MASCOT REACTIONS (For Skibidi Toilet or other SVG mascots)
# ============================================================================
def mascot_head_tilt(scene, mascot, angle=15, run_time=0.5):
    """Make mascot tilt its head in reaction."""
    scene.play(
        mascot.animate.rotate(angle * DEGREES),
        run_time=run_time,
        rate_func=there_and_back
    )


def mascot_bounce(scene, mascot, height=0.3, run_time=0.5):
    """Make mascot bounce up and down."""
    original_pos = mascot.get_center()
    scene.play(
        mascot.animate.shift(UP * height),
        run_time=run_time / 2,
        rate_func=smooth
    )
    scene.play(
        mascot.animate.move_to(original_pos),
        run_time=run_time / 2,
        rate_func=smooth
    )


def mascot_shake(scene, mascot, intensity=0.15, run_time=0.5):
    """Make mascot shake horizontally (confusion/surprise)."""
    original_pos = mascot.get_center()
    scene.play(
        mascot.animate.shift(RIGHT * intensity),
        run_time=run_time / 4,
        rate_func=linear
    )
    scene.play(
        mascot.animate.shift(LEFT * intensity * 2),
        run_time=run_time / 2,
        rate_func=linear
    )
    scene.play(
        mascot.animate.move_to(original_pos),
        run_time=run_time / 4,
        rate_func=linear
    )
