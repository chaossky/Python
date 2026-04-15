# from manim import *
# class DefaultTemplate(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.flip(RIGHT)  # flip horizontally
#         square.rotate(-3 * TAU / 8)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation

from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.9)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        
class SquareToCircle(Scene):
    def construct(self):
        self.camera.background_color=BLACK
        circle=Circle()
        circle.set_fill(PINK,opacity=0.5)
        
        square=Square()
        square.set_fill(BLUE, opacity=0.6)
        square.next_to(circle,DOWN,buff=0.5)
        self.play(Create(circle),Create(square))
        # square.rotate(2.5*PI)
        
        # self.play(Create(square))
        # self.play(Transform(square,circle))
        # self.play(FadeOut(square))
        