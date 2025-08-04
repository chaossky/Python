from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle        
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        square = Square()  # create a square        
        square.rotate(PI/4 )
        
        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))
                  # rotate a certain amount
                  
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.9)  # set the color and transparency
        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
         # 두 도형을 하나의 그룹으로 정렬하고 중앙으로 이동
        # group = VGroup(circle, square).arrange(LEFT, buff=0.5).move_to(ORIGIN)
        square.next_to(circle, DOWN, buff=0.2)  # set the position
        self.play(Create(circle), Create(square))

        # square.next_to(circle, DOWN, buff=0.5)  # set the position
        # self.play(Create(circle), Create(square))  # show the shapes on screen
        
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
        
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
        
class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        circle.scale(0.3)  # 원 크기를 줄임
        square.scale(0.3)  # 정사각형 크기를 줄임
        triangle.scale(0.3)  # 삼각형 크기를 줄임

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)