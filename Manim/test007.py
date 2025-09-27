from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)
        self.add(square)
        self.play(square.animate.rotate(60.0 * DEGREES), run_time=12)