from manim import *

class PythagorasDiagram(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # 직각삼각형
        A = [0, 0, 0]
        B = [4, 0, 0]
        C = [0, 3, 0]
        triangle = Polygon(A, B, C)
        triangle.set_fill(BLUE, opacity=0.3)
        triangle.set_stroke(WHITE, width=2)
        triangle.move_to(ORIGIN)

        # 각 변을 Line으로 정의
        base_line = Line(A, B)
        height_line = Line(A, C)
        hyp_line = Line(B, C)

        # Brace와 라벨 붙이기
        brace_b = Brace(base_line, DOWN)
        label_b = brace_b.get_text("b")

        brace_a = Brace(height_line, LEFT)
        label_a = brace_a.get_text("a")

        brace_c = Brace(hyp_line, UP)
        label_c = brace_c.get_text("c")

        # 수식은 화면 아래쪽 특정 좌표에 배치
        formula = MathTex("a^2 + b^2 = c^2")
        formula.move_to([0, -2.5, 0])

        # 애니메이션
        self.play(Create(triangle))
        self.play(Create(brace_b), Write(label_b))
        self.play(Create(brace_a), Write(label_a))
        self.play(Create(brace_c), Write(label_c))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)