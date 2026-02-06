#!/bin/bash
# Render all scenes in 480p (Low Quality) for preview

echo "Rendering Act 1..."
manim -ql scenes/act1_opening.py Act1Opening

echo "Rendering Act 2..."
manim -ql scenes/act2_brain_topology.py Act2BrainTopology

echo "Rendering Act 3..."
manim -ql scenes/act3_rizz_limit.py Act3RizzLimit

echo "Rendering Act 4..."
manim -ql scenes/act4_torus_shake.py Act4TorusShake

echo "Rendering Act 5..."
manim -ql scenes/act5_conspiracy.py Act5Conspiracy

echo "Rendering Act 6..."
manim -ql scenes/act6_conclusion.py Act6Conclusion

echo "All renders complete! Check 'media/videos' folder."
