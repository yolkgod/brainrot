"""
3Blue1Brown Style Color Palette for Brainrot
============================================
Elegant dark backgrounds with vibrant accent colors.
"""

from manim import *

# ============================================================================
# 3B1B SIGNATURE COLORS (Elegant, Dark Theme)
# ============================================================================
BACKGROUND_DARK = "#1a1a2e"      # Deep navy-black
BACKGROUND_GRADIENT = "#16213e"  # Slightly lighter for gradients
TEXT_PRIMARY = "#eaeaea"         # Off-white for readability
TEXT_SECONDARY = "#a0a0a0"       # Muted gray for subtitles

# 3B1B Classic Accent Colors
BLUE_E = "#1c758a"
BLUE_D = "#29abca"
BLUE_C = "#58c4dd"
TEAL_E = "#49a88f"
GREEN_E = "#699c52"
YELLOW_E = "#e8c11c"
GOLD_E = "#c78d46"
RED_E = "#cf5044"

# ============================================================================
# BRAINROT "STIMULATION" COLORS (High Contrast Accents)
# ============================================================================
BRAINROT_MAGENTA = "#FF00FF"
BRAINROT_CYAN = "#00FFFF"
BRAINROT_YELLOW = "#FFFF00"
BRAINROT_RED_ORANGE = "#FF3300"
BRAINROT_NEON_GREEN = "#39FF14"

# ============================================================================
# SEMANTIC COLORS (What they represent)
# ============================================================================
RIZZ_COLOR = BRAINROT_MAGENTA
SIGMA_COLOR = BLUE_C
AURA_COLOR = BRAINROT_NEON_GREEN
SKIBIDI_COLOR = BRAINROT_CYAN
OHIO_COLOR = RED_E

# Highlight colors for step-by-step reveals
HIGHLIGHT_PRIMARY = YELLOW_E
HIGHLIGHT_SECONDARY = BLUE_C
HIGHLIGHT_TERTIARY = BRAINROT_MAGENTA

# ============================================================================
# GRADIENT HELPERS
# ============================================================================
def get_gradient_background(scene, top_color=BACKGROUND_DARK, bottom_color=BACKGROUND_GRADIENT):
    """Create a subtle vertical gradient background."""
    gradient = Rectangle(
        width=config.frame_width + 1,
        height=config.frame_height + 1,
        fill_opacity=1,
        stroke_width=0
    )
    gradient.set_color(color=[top_color, bottom_color])
    gradient.move_to(ORIGIN)
    return gradient
