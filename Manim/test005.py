from manim import *

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#121212"
        ds_m = MathTex(r"\mathbb{A}", fill_color=logo_black).scale(10)
        ds_m.shift(2.0 * LEFT + 1.0 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)
        
class DrawCircle(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        logo_green = "#87c2a5"
        logo_black = "#121212"
        circle = Circle(3.0,color=logo_green, fill_opacity=1).shift(LEFT)
        logo = VGroup(circle)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)