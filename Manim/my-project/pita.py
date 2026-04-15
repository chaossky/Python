from manim import *

class Pythagoras(Scene):
    def construct(self):
        # 화면의 바탕색을 검은색으로 지정
        self.camera.background_color=BLACK
        # 문자열을 여러 파트로 나눠서 전달
        formula = MathTex("a^2", "+", "b^2", "=", "c^2",font_size=90)

        formula.move_to(ORIGIN)

        self.play(Write(formula))
        self.wait(2)

        # 각 파트별 색상 지정
        formula[0].set_color(RED)    # a^2
        formula[2].set_color(BLUE)   # b^2
        formula[4].set_color(GREEN)  # c^2

        self.wait(2)
        
class PythagorasDiagram(Scene):
    def construct(self):
        # 화면의 바탕색을 검은색으로 지정
        self.camera.background_color=BLACK
        # 직각삼각형 (밑변 b, 높이 a, 빗변 c)
        triangle = Polygon(
            [0, 0, 0],   # 좌표 (0,0)
            [4, 0, 0],   # 밑변 끝점 (b)
            [0, 3, 0]    # 높이 끝점 (a)
        )
        triangle.set_fill(BLUE, opacity=0.3)
        triangle.set_stroke(WHITE, width=2)
        triangle.move_to(ORIGIN)

        # 각 변의 중점 좌표를 얻어서 라벨 배치
        # 밑변 b
        base_mid = (triangle.get_vertices()[0] + triangle.get_vertices()[1]) / 2
        #Brace(base_mid,sharpness=1)
        label_b = Tex("b").next_to(base_mid, DOWN, buff=0.2)

        # 높이 a
        height_mid = (triangle.get_vertices()[0] + triangle.get_vertices()[2]) / 2
        label_a = Tex("a").next_to(height_mid, LEFT, buff=0.2)

        # 빗변 c
        hyp_mid = (triangle.get_vertices()[1] + triangle.get_vertices()[2]) / 2
        label_c = Tex("c").next_to(hyp_mid, UP+RIGHT, buff=0.2)

        # 수식은 화면 아래쪽에 배치
        formula = MathTex("a^2 + b^2 = c^2")
        formula.move_to([-0.5,-2.5,0]) 

        # 애니메이션
        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
