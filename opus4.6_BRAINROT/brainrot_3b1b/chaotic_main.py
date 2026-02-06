"""
BRAINROT CHAOS VIDEO - The REAL Version
========================================
9:16 vertical, constant jitter, physics, flashbangs, immediate chaos.
Following brain_rot.md principles:
- Painful clashing colors
- No smooth animations (linear rate_func)
- ADHD jitter on EVERYTHING
- Flashbangs between scenes
- Triple gravity physics
- Glitch morphs with path_arc = PI * 4

Usage:
    manim -pql --config_file config.cfg chaotic_main.py ChaoticBrainrot
"""

from manim import *
import numpy as np
import random
import os

# ============================================================================
# CONFIG: 9:16 VERTICAL (TikTok/Reels/Shorts)
# ============================================================================
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

# ============================================================================
# BRAINROT COLOR PALETTE (PAINFUL CLASHING)
# ============================================================================
BG_DARK = "#0a0a0a"
BRAINROT_MAGENTA = "#FF00FF"
BRAINROT_CYAN = "#00FFFF"
BRAINROT_YELLOW = "#FFFF00"
BRAINROT_RED = "#FF3300"
BRAINROT_GREEN = "#39FF14"
WHITE = "#FFFFFF"

CHAOS_COLORS = [BRAINROT_MAGENTA, BRAINROT_CYAN, BRAINROT_YELLOW, BRAINROT_RED, BRAINROT_GREEN]

# ============================================================================
# ASSET PATHS
# ============================================================================
ASSET_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(ASSET_DIR, "assets", "svg")
AUDIO_DIR = os.path.join(ASSET_DIR, "assets", "audio")

def svg_path(name):
    return os.path.join(SVG_DIR, name)

def audio_path(name):
    return os.path.join(AUDIO_DIR, name)


# ============================================================================
# ADHD JITTER (Constant vibration on EVERYTHING)
# ============================================================================
def add_jitter(mob, intensity=0.08):
    """Add constant random shake to any mobject."""
    original_center = mob.get_center().copy()
    
    def jitter_update(m, dt):
        offset = np.array([
            random.uniform(-intensity, intensity),
            random.uniform(-intensity, intensity),
            0
        ])
        m.move_to(original_center + offset)
    
    mob.add_updater(jitter_update)
    return mob


def add_jitter_group(mobs, intensity=0.08):
    """Add jitter to a list of mobjects."""
    for mob in mobs:
        add_jitter(mob, intensity)


# ============================================================================
# TRIGGER WORD EFFECTS
# ============================================================================
def trigger_flash(scene, mob, color=BRAINROT_MAGENTA):
    """Flash + Wiggle on trigger words."""
    scene.play(
        Wiggle(mob, scale_value=1.3, rotation_angle=0.1 * TAU),
        Flash(mob.get_center(), color=color, line_length=0.5),
        run_time=0.3,
        rate_func=linear
    )


# ============================================================================
# MAIN CHAOTIC SCENE
# ============================================================================
class ChaoticBrainrot(Scene):
    """
    60-second brainrot following brain_rot.md principles.
    IMMEDIATE CHAOS from frame 1.
    """
    
    def construct(self):
        self.camera.background_color = BG_DARK
        
        # FRAME 1: FLASHBANG OPENING
        self.flashbang()
        
        # 0-5s: CHAOS INTRO
        self.chaos_intro()
        
        # 5-15s: SVG MORPHING MAYHEM
        self.morphing_section()
        
        # 15-30s: 3D GRAPH WITH PHYSICS
        self.graph_with_physics()
        
        # 30-45s: THE "PROOF" 
        self.the_proof()
        
        # 45-60s: SINGULARITY FINALE
        self.singularity_finale()
    
    def flashbang(self):
        """White screen flash - the brainrot punctuation."""
        flash = Rectangle(
            width=12, height=20,
            fill_color=WHITE, fill_opacity=1, stroke_width=0
        )
        self.add(flash)
        self.wait(0.05)
        self.remove(flash)
    
    def chaos_intro(self):
        """IMMEDIATE OVERSTIMULATION - No slow buildup."""
        
        # === FALLING TERMS (Simulated Triple Gravity) ===
        terms = ["SKIBIDI", "SIGMA", "RIZZ", "OHIO", "GYATT"]
        falling_texts = []
        
        for i, term in enumerate(terms):
            text = Text(
                term,
                font_size=36,
                color=random.choice(CHAOS_COLORS),
                font="Arial",
                weight=BOLD
            )
            # Spread across top, staggered
            text.move_to(np.array([
                random.uniform(-3, 3),
                10 + i * 1.5,  # Start above screen
                0
            ]))
            falling_texts.append(text)
            self.add(text)
        
        # Aggressive fall (triple gravity feel)
        fall_anims = []
        for text in falling_texts:
            end_y = random.uniform(-5, -3)
            fall_anims.append(
                text.animate(rate_func=linear).move_to(
                    np.array([text.get_center()[0] + random.uniform(-1, 1), end_y, 0])
                )
            )
        
        self.play(*fall_anims, run_time=0.8)
        
        # Add jitter to all fallen texts
        add_jitter_group(falling_texts, 0.1)
        
        # === MAIN TITLE SLAM ===
        title = Text(
            "RIZZ",
            font_size=120,
            color=BRAINROT_MAGENTA,
            font="Arial",
            weight=BOLD
        )
        title.move_to(UP * 4)
        
        # Slam in from top
        self.play(
            title.animate(rate_func=linear).move_to(UP * 2),
            run_time=0.2
        )
        
        # Trigger effect
        trigger_flash(self, title, BRAINROT_CYAN)
        add_jitter(title, 0.15)
        
        # === SKIBIDI TOILET ENTRANCE ===
        try:
            skibidi = SVGMobject(svg_path("Skibidi_toilet.svg"))
            skibidi.set_height(3)
            skibidi.move_to(DOWN * 2)
            # skibidi.set_color(WHITE) # REMOVED: Keep original colors
            
            # Slide in from side
            skibidi.shift(RIGHT * 8)
            self.add(skibidi)
            self.play(
                skibidi.animate(rate_func=linear).shift(LEFT * 8),
                run_time=0.3
            )
            add_jitter(skibidi, 0.08)
            self.skibidi = skibidi
        except:
            # Fallback if SVG fails
            skibidi = Text("🚽", font_size=100)
            skibidi.move_to(DOWN * 2)
            self.add(skibidi)
            add_jitter(skibidi, 0.08)
            self.skibidi = skibidi
        
        self.wait(0.5)
        
        # FLASHBANG transition
        self.flashbang()
        
        # Clear for next section
        for text in falling_texts:
            text.clear_updaters()
        title.clear_updaters()
        self.skibidi.clear_updaters()
        
        self.play(
            *[FadeOut(t, run_time=0.1) for t in falling_texts],
            FadeOut(title, run_time=0.1),
            run_time=0.15
        )
        
        self.title_for_morph = title
    
    def morphing_section(self):
        """SVG transitions with visual chaos (no complex morphs to avoid crash)."""
        
        # === SKIBIDI → ILLUMINATI TRANSITION ===
        try:
            illuminati = SVGMobject(svg_path("Illuminati.svg"))
            illuminati.set_height(4)
            # illuminati.set_color(BRAINROT_YELLOW) # REMOVED: Keep original colors
            illuminati.move_to(ORIGIN)
            
            # FadeTransform instead of complex path_arc (avoids segfault)
            # Add spinning + scaling for visual chaos
            self.play(
                self.skibidi.animate.scale(0.1).rotate(TAU * 2),
                run_time=0.5,
                rate_func=linear
            )
            self.remove(self.skibidi)
            
            # Illuminati appears with flash
            self.flashbang()
            illuminati.scale(0.1)
            self.add(illuminati)
            self.play(
                illuminati.animate.scale(10),  # 0.1 * 10 = 1.0 scale
                run_time=0.3,
                rate_func=linear
            )
            add_jitter(illuminati, 0.1)
            self.skibidi = illuminati
            
        except Exception as e:
            # Fallback
            triangle = Triangle(fill_opacity=0.8, color=BRAINROT_YELLOW)
            triangle.set_height(4)
            self.flashbang()
            self.remove(self.skibidi)
            self.add(triangle)
            self.skibidi = triangle
        
        self.wait(0.3)
        
        # === AMOGUS WORD REIFICATION ===
        sus_text = Text("SUS", font_size=80, color=BRAINROT_RED, weight=BOLD)
        sus_text.move_to(DOWN * 4)
        self.add(sus_text)
        add_jitter(sus_text, 0.1)
        
        self.play(
            sus_text.animate(rate_func=linear).move_to(DOWN * 2),
            run_time=0.2
        )
        
        try:
            amogus = SVGMobject(svg_path("amogus.svg"))
            amogus.set_height(2.5)
            # amogus.set_color(BRAINROT_RED) # REMOVED: Keep original colors
            amogus.move_to(DOWN * 2)
            
            # Spin out text, flash, spin in amogus
            self.play(
                sus_text.animate.scale(0.1).rotate(TAU),
                run_time=0.3,
                rate_func=linear
            )
            self.remove(sus_text)
            self.flashbang()
            amogus.scale(0.1)
            self.add(amogus)
            self.play(
                amogus.animate.scale(10).rotate(-TAU * 0.5),
                run_time=0.3
            )
            add_jitter(amogus, 0.08)
        except:
            pass
        
        self.wait(0.3)
        self.flashbang()
        
        # Clear
        self.skibidi.clear_updaters()
        sus_text.clear_updaters()
        self.play(
            FadeOut(self.skibidi),
            FadeOut(sus_text),
            run_time=0.15
        )
    
    def graph_with_physics(self):
        """3D-style graph with falling objects."""
        
        # === EQUATION SLAM ===
        equation = Text(
            "R = ∫ Skibidi × Aura dx",
            font_size=32,
            color=WHITE
        )
        equation.to_edge(UP, buff=1)
        
        self.play(
            FadeIn(equation, shift=DOWN * 2),
            run_time=0.3,
            rate_func=linear
        )
        add_jitter(equation, 0.05)
        
        # === FAKE 3D AXES ===
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=7,
            axis_config={"color": BRAINROT_CYAN}
        )
        axes.move_to(DOWN * 1)
        
        x_label = Text("Skibidi", font_size=18, color=BRAINROT_MAGENTA)
        y_label = Text("Aura", font_size=18, color=BRAINROT_GREEN)
        x_label.next_to(axes.x_axis, DOWN)
        y_label.next_to(axes.y_axis, LEFT)
        
        self.play(Create(axes), run_time=0.5, rate_func=linear)
        self.add(x_label, y_label)
        add_jitter(x_label, 0.05)
        add_jitter(y_label, 0.05)
        
        # === SURFACE (Fake 3D with 2D) ===
        # Create a wavy parametric curve to simulate surface
        curve = axes.plot(
            lambda x: 0.8 * np.sin(x * 2) + 0.3 * np.cos(x * 3),
            x_range=[-2.5, 2.5],
            color=BRAINROT_MAGENTA
        )
        
        self.play(Create(curve), run_time=0.8, rate_func=linear)
        
        # === PHYSICS: FALLING GRIMACE ===
        try:
            grimace = SVGMobject(svg_path("grimace_shake.svg"))
            grimace.set_height(1.5)
            grimace.move_to(UP * 8)
            self.add(grimace)
            
            # Triple gravity fall
            self.play(
                grimace.animate(rate_func=rush_into).move_to(DOWN * 2),
                run_time=0.4
            )
            
            # Bounce
            self.play(
                grimace.animate(rate_func=there_and_back).shift(UP * 0.5),
                run_time=0.2
            )
            add_jitter(grimace, 0.1)
            
        except:
            pass
        
        # === GYATT POINT LABEL ===
        peak_label = Text(
            "GYATT POINT",
            font_size=24,
            color=BRAINROT_YELLOW,
            weight=BOLD
        )
        peak_label.move_to(UP * 0.5 + RIGHT * 0.5)
        
        self.play(FadeIn(peak_label, scale=1.5), run_time=0.2)
        trigger_flash(self, peak_label, BRAINROT_YELLOW)
        add_jitter(peak_label, 0.08)
        
        self.wait(0.5)
        self.flashbang()
        
        # Clear
        for mob in [equation, x_label, y_label, peak_label]:
            mob.clear_updaters()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.15
        )
    
    def the_proof(self):
        """Step-by-step 'proof' with trigger effects."""
        
        # === TITLE ===
        title = Text(
            "THE PROOF",
            font_size=48,
            color=BRAINROT_CYAN,
            weight=BOLD
        )
        title.to_edge(UP, buff=1.5)
        
        self.play(FadeIn(title, shift=DOWN), run_time=0.2)
        add_jitter(title, 0.08)
        
        # === STEPS ===
        steps = [
            ("Given:", "Skibidi → ∞", BRAINROT_CYAN),
            ("Therefore:", "Ohio → 0", BRAINROT_RED),
            ("Thus:", "Sigma = Skibidi ÷ Ohio", BRAINROT_MAGENTA),
        ]
        
        step_mobs = []
        y_pos = 3
        
        for label, content, color in steps:
            step_label = Text(label, font_size=24, color=WHITE)
            step_content = Text(content, font_size=32, color=color, weight=BOLD)
            
            step_group = VGroup(step_label, step_content)
            step_group.arrange(RIGHT, buff=0.3)
            step_group.move_to(UP * y_pos)
            
            self.play(
                FadeIn(step_group, shift=RIGHT * 2),
                run_time=0.3,
                rate_func=linear
            )
            
            # Trigger on key term
            trigger_flash(self, step_content, color)
            add_jitter(step_content, 0.06)
            
            step_mobs.append(step_group)
            y_pos -= 2
            
            self.wait(0.3)
        
        # === SIGMA MALE REVEAL ===
        try:
            sigma = SVGMobject(svg_path("sigma_male.svg"))
            sigma.set_height(4)
            # sigma.set_color(BRAINROT_MAGENTA) # REMOVED: Keep original colors
            sigma.move_to(DOWN * 3)
            
            self.play(
                GrowFromCenter(sigma),
                run_time=0.5
            )
            add_jitter(sigma, 0.1)
            
        except:
            qed = Text("Q.E.D.", font_size=48, color=BRAINROT_MAGENTA, weight=BOLD)
            qed.move_to(DOWN * 3)
            self.play(GrowFromCenter(qed), run_time=0.3)
            add_jitter(qed, 0.1)
        
        self.wait(0.5)
        self.flashbang()
        
        # Clear updaters
        title.clear_updaters()
        for step in step_mobs:
            for sub in step:
                if hasattr(sub, 'clear_updaters'):
                    sub.clear_updaters()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.15
        )
    
    def singularity_finale(self):
        """Everything gets sucked into a black hole."""
        
        # === SPAWN CHAOS OBJECTS ===
        chaos_objects = []
        terms = ["OHIO", "GYATT", "RIZZ", "SIGMA", "SKIBIDI", "MOG", "AURA"]
        
        for i, term in enumerate(terms):
            angle = i * (TAU / len(terms))
            radius = 5
            
            text = Text(
                term,
                font_size=28,
                color=random.choice(CHAOS_COLORS),
                weight=BOLD
            )
            text.move_to(np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ]))
            chaos_objects.append(text)
            self.add(text)
            add_jitter(text, 0.1)
        
        self.wait(0.3)
        
        # === THE SINGULARITY (Black Hole) ===
        singularity = Star(
            n=16,
            outer_radius=0.5,
            inner_radius=0.2,
            color=WHITE,
            fill_opacity=1
        )
        singularity.move_to(ORIGIN)
        self.add(singularity)
        
        # === SUCK EVERYTHING IN ===
        # Clear jitter first
        for obj in chaos_objects:
            obj.clear_updaters()
        
        suck_anims = []
        for obj in chaos_objects:
            suck_anims.append(
                obj.animate(rate_func=rush_into).move_to(ORIGIN).scale(0.01)
            )
        
        self.play(
            *suck_anims,
            singularity.animate.scale(3),
            run_time=1.0
        )
        
        # === FINAL FLASHBANG ===
        self.flashbang()
        
        # === OUTRO ===
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.1
        )
        
        outro = Text(
            "This has been...\neducational.",
            font_size=28,
            color=WHITE
        )
        self.play(FadeIn(outro), run_time=0.5)
        self.wait(1.5)
        
        # Discord ping moment
        self.play(FadeOut(outro), run_time=0.3)


# ============================================================================
# QUICK TEST (Faster render)
# ============================================================================
class QuickChaosTest(Scene):
    """Quick test of jitter and flashbang."""
    
    def construct(self):
        config.frame_width = 9
        config.frame_height = 16
        self.camera.background_color = BG_DARK
        
        # Flashbang
        flash = Rectangle(width=12, height=20, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.add(flash)
        self.wait(0.05)
        self.remove(flash)
        
        # Jittery text
        text = Text("SKIBIDI", font_size=72, color=BRAINROT_MAGENTA, weight=BOLD)
        self.add(text)
        add_jitter(text, 0.15)
        
        self.wait(2)
