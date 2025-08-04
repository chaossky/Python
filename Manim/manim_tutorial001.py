from manim import *

class NameOfAnimation(Scene):
    def construct(self):
        
        box=Rectangle(
            width=1,
            height=1,
            fill_color=RED_B,
            fill_opacity=0.5,
            stroke_color=GREEN_C,
            stroke_opacity=0.7
        )
        # Create a square
        self.add(box)  
        self.play(
            box.animate.shift(RIGHT*2),
            run_time=2
        )   
        self.play(
            box.animate.shift(UP*3),
            run_time=2
        )
        self.play(
            box.animate.shift(DOWN*3+LEFT*5),
            run_time=2
        )
        self.play(
            box.animate.shift(UP*1.5+RIGHT*1),
            run_time=2
        )