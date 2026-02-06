"""
Act 4: The Proof (50-60s)
=========================
Step-by-step derivation with highlighting and final reveal.
"""

from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.colors import *
from utils.morphing import circumscribe_term, indicate_with_flash


class Act4_TheProof(Scene):
    """
    The climactic "proof" with step-by-step reveals.
    Duration: ~10 seconds
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        
        # === BEAT 1: Setup the Derivation (50-52s) ===
        title = Text(
            "The Fundamental Theorem",
            font_size=36,
            color=TEXT_PRIMARY,
            font="Arial"
        )
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # === BEAT 2: Step-by-Step Derivation (52-57s) ===
        steps = VGroup(
            Text("Given: Skibidi → ∞", font_size=28, color=SKIBIDI_COLOR),
            Text("Therefore: Ohio → 0", font_size=28, color=OHIO_COLOR),
            Text("By substitution:", font_size=28, color=TEXT_SECONDARY),
        )
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.next_to(title, DOWN, buff=0.8)
        steps.shift(LEFT * 2)
        
        for step in steps:
            self.play(
                FadeIn(step, shift=RIGHT * 0.3),
                run_time=0.6
            )
            self.wait(0.3)
        
        # === BEAT 3: The Final Equation (57-60s) ===
        final_eq = Text(
            "∴  Sigma = Skibidi ÷ Ohio",
            font_size=42,
            color=RIZZ_COLOR,
            font="Arial"
        )
        final_eq.next_to(steps, DOWN, buff=0.8)
        final_eq.shift(RIGHT * 1)
        
        # Dramatic appearance
        self.play(
            Write(final_eq),
            run_time=1.2
        )
        
        # QED box
        qed = Text(
            "Q.E.D.",
            font_size=24,
            color=BRAINROT_MAGENTA,
            font="Arial"
        )
        qed.next_to(final_eq, RIGHT, buff=0.5)
        
        # Flash the final equation
        self.play(
            FadeIn(qed, scale=1.5),
            Circumscribe(final_eq, color=BRAINROT_MAGENTA, fade_out=True),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # Store for finale
        self.all_elements = VGroup(title, steps, final_eq, qed)


class Act5_TheFinale(Scene):
    """
    Chaos ending with glitch morph and singularity.
    Duration: ~5-10 seconds (as buffer/outro)
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_DARK
        
        # === BEAT 1: Everything on Screen ===
        # Recreate key elements for the finale
        final_eq = Text(
            "Sigma = Skibidi ÷ Ohio",
            font_size=42,
            color=RIZZ_COLOR,
            font="Arial"
        )
        
        self.play(FadeIn(final_eq), run_time=0.5)
        
        # === BEAT 2: The Glitch (Flashbang) ===
        flash = Rectangle(
            width=config.frame_width + 2,
            height=config.frame_height + 2,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=0
        )
        
        self.play(FadeIn(flash, run_time=0.05))
        self.play(FadeOut(flash, run_time=0.1))
        
        # === BEAT 3: Glitch Morph to Star ===
        chaos_star = Star(
            n=16,
            outer_radius=2.5,
            inner_radius=0.8,
            color=BRAINROT_MAGENTA,
            fill_opacity=0.9
        )
        chaos_star.move_to(ORIGIN)
        
        # Chaotic morph with path_arc = PI * 4
        self.play(
            Transform(final_eq, chaos_star, path_arc=PI * 4),
            run_time=1.5,
            rate_func=linear
        )
        
        # === BEAT 4: Singularity (Objects Sucked In) ===
        # Add floating terms that get sucked to center
        terms = VGroup(
            Text("OHIO", font_size=24, color=OHIO_COLOR),
            Text("GYATT", font_size=24, color=BRAINROT_CYAN),
            Text("RIZZ", font_size=24, color=RIZZ_COLOR),
            Text("SIGMA", font_size=24, color=SIGMA_COLOR),
        )
        
        # Position around the screen
        positions = [UL * 2.5, UR * 2.5, DL * 2.5, DR * 2.5]
        for term, pos in zip(terms, positions):
            term.move_to(pos)
        
        self.play(
            *[FadeIn(term, scale=0.5) for term in terms],
            run_time=0.3
        )
        
        # Suck everything to center
        self.play(
            *[term.animate.move_to(ORIGIN).scale(0.1) for term in terms],
            final_eq.animate.scale(0.1),
            run_time=1.0,
            rate_func=rush_into
        )
        
        # === BEAT 5: Silence + Final Text ===
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.3
        )
        
        self.wait(0.5)
        
        # Quiet ending text
        outro = Text(
            "This has been... educational.",
            font_size=28,
            color=TEXT_SECONDARY,
            font="Arial"
        )
        
        self.play(FadeIn(outro, run_time=1.0))
        self.wait(1.5)
        self.play(FadeOut(outro, run_time=0.5))


if __name__ == "__main__":
    pass
