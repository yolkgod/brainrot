"""
Renderer - Manim scene renderer optimised for Apple Silicon (Mac M2).
======================================================================
Dynamically builds a Manim Scene from a generated script and renders it
with Metal-friendly settings for fast output on macOS.
"""

import os
import random
import textwrap
from pathlib import Path

import numpy as np
from manim import (
    BOLD,
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    TAU,
    UP,
    WHITE,
    Axes,
    Create,
    FadeIn,
    FadeOut,
    Flash,
    GrowFromCenter,
    MathTex,
    Rectangle,
    Scene,
    Star,
    Text,
    VGroup,
    Wiggle,
    config,
    linear,
    rush_into,
)

# ---------------------------------------------------------------------------
# Brainrot palette
# ---------------------------------------------------------------------------
BG_DARK = "#0a0a0a"
CHAOS_COLORS = ["#FF00FF", "#00FFFF", "#FFFF00", "#FF3300", "#39FF14"]


def _jitter(mob, intensity=0.08):
    """Attach a per-frame random-shake updater."""
    centre = mob.get_center().copy()

    def _upd(m, dt):
        m.move_to(
            centre
            + np.array(
                [
                    random.uniform(-intensity, intensity),
                    random.uniform(-intensity, intensity),
                    0,
                ]
            )
        )

    mob.add_updater(_upd)
    return mob


def _flashbang(scene):
    """Full-screen white flash."""
    flash = Rectangle(
        width=12, height=20, fill_color=WHITE, fill_opacity=1, stroke_width=0
    )
    scene.add(flash)
    scene.wait(0.05)
    scene.remove(flash)


# ---------------------------------------------------------------------------
# Dynamic scene builder
# ---------------------------------------------------------------------------
def _build_scene_class(script: dict, image_paths: list[str]):
    """
    Return a new Manim Scene subclass whose ``construct`` method renders
    every scene from the generated script.
    """

    class BrainrotGenerated(Scene):
        def construct(self):
            # -- 9:16 vertical config --
            config.frame_width = 9
            config.frame_height = 16
            config.pixel_width = 1080
            config.pixel_height = 1920
            self.camera.background_color = BG_DARK

            _flashbang(self)

            for idx, scene_data in enumerate(script["scenes"]):
                self._render_scene(scene_data, idx)

            # Singularity finale
            self._singularity()

        # ----------------------------------------------------------
        def _render_scene(self, scene_data: dict, idx: int):
            """Render a single script scene."""
            narration = scene_data.get("narration", "")
            math_elements = scene_data.get("math_elements", [])

            # -- Background image (if generated) --
            if idx < len(image_paths) and os.path.exists(image_paths[idx]):
                from manim import ImageMobject

                bg = ImageMobject(image_paths[idx])
                bg.height = config.frame_height
                bg.set_opacity(0.35)
                self.add(bg)

            # -- Title caption --
            caption = Text(
                textwrap.fill(narration, width=28),
                font_size=32,
                color=random.choice(CHAOS_COLORS),
                font="Arial",
                weight=BOLD,
            )
            caption.to_edge(UP, buff=1.5)
            self.play(FadeIn(caption, shift=DOWN * 0.5), run_time=0.3, rate_func=linear)
            _jitter(caption, 0.06)

            # -- Math elements --
            y_offset = 1.0
            math_mobs = []
            for elem in math_elements:
                try:
                    mob = MathTex(elem, color=random.choice(CHAOS_COLORS))
                except Exception:
                    mob = Text(elem, font_size=24, color=random.choice(CHAOS_COLORS))
                mob.move_to(DOWN * y_offset)
                self.play(GrowFromCenter(mob), run_time=0.3)
                _jitter(mob, 0.05)
                math_mobs.append(mob)
                y_offset += 1.8

            # Hold
            self.wait(max(scene_data.get("duration_hint", 4) * 0.4, 1.0))

            # Transition flash
            _flashbang(self)

            # Clean up
            caption.clear_updaters()
            for m in math_mobs:
                m.clear_updaters()
            self.play(
                FadeOut(caption, run_time=0.1),
                *[FadeOut(m, run_time=0.1) for m in math_mobs],
                run_time=0.15,
            )
            # Remove background
            for mob in list(self.mobjects):
                self.remove(mob)

        # ----------------------------------------------------------
        def _singularity(self):
            """Black-hole singularity finale."""
            terms = ["SKIBIDI", "SIGMA", "RIZZ", "OHIO", "GYATT", "MOG", "AURA"]
            objs = []
            for i, t in enumerate(terms):
                angle = i * (TAU / len(terms))
                txt = Text(
                    t,
                    font_size=28,
                    color=random.choice(CHAOS_COLORS),
                    weight=BOLD,
                )
                txt.move_to(
                    np.array([5 * np.cos(angle), 5 * np.sin(angle), 0])
                )
                self.add(txt)
                _jitter(txt, 0.1)
                objs.append(txt)

            self.wait(0.3)

            star = Star(
                n=16, outer_radius=0.5, inner_radius=0.2,
                color=WHITE, fill_opacity=1,
            )
            star.move_to(ORIGIN)
            self.add(star)

            for o in objs:
                o.clear_updaters()

            self.play(
                *[
                    o.animate(rate_func=rush_into).move_to(ORIGIN).scale(0.01)
                    for o in objs
                ],
                star.animate.scale(3),
                run_time=1.0,
            )
            _flashbang(self)
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.1)

            outro = Text("This has been…\neducational.", font_size=28, color=WHITE)
            self.play(FadeIn(outro), run_time=0.5)
            self.wait(1.0)
            self.play(FadeOut(outro), run_time=0.3)

    return BrainrotGenerated


def render(script: dict, image_paths: list[str], output_dir: str) -> str:
    """
    Render the generated script to an MP4 video.

    Mac M2 optimisations applied:
      - ``--renderer=cairo`` (avoids OpenGL issues on macOS)
      - Medium quality (720p) for speed
      - 30 fps

    Args:
        script: The parsed script dict (from script_writer).
        image_paths: List of generated image file paths per scene.
        output_dir: Directory for Manim media output.

    Returns:
        Path to the rendered MP4 file.
    """
    SceneClass = _build_scene_class(script, image_paths)

    # Configure Manim for Mac M2 optimised rendering
    config.frame_width = 9
    config.frame_height = 16
    config.pixel_width = 1080
    config.pixel_height = 1920
    config.frame_rate = 30
    config.media_dir = output_dir
    config.quality = "medium_quality"
    config.renderer = "cairo"
    config.disable_caching = True

    scene = SceneClass()
    scene.render()

    # Locate the rendered file
    rendered = Path(output_dir) / "videos" / "1080p30" / "BrainrotGenerated.mp4"
    if not rendered.exists():
        # Fallback: search for any mp4 under output_dir
        for mp4 in Path(output_dir).rglob("*.mp4"):
            return str(mp4)
    return str(rendered)
