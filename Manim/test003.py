from manim import *
import numpy as np

class DrawTangentWithAsymptotes(Scene):
    def construct(self):
        # 좌표축 생성
        axes = Axes(
            x_range=[-8, 8, 0.5],
            y_range=[-10, 10, 1],
            axis_config={"include_tip": False}
        )

        # 탄젠트 함수 그래프 생성
        tangent_graph = axes.plot(
            lambda x: np.tan(x),
            color=RED,
            discontinuities=[-5*np.pi/2,-3*np.pi/2, -np.pi/2, np.pi/2, 3*np.pi/2, 5*np.pi/2],
            dt=0.05  # 그래프의 부드러움 조절
        )

        # 점근선 생성: x = ±π/2, ±3π/2
        asymptotes = VGroup()
        for x in [-5*np.pi/2,-3*np.pi/2, -np.pi/2, np.pi/2, 3*np.pi/2, 5*np.pi/2]:
            line = axes.get_vertical_line(axes.c2p(x, 0), color=GRAY)
            asymptotes.add(line)

        # 라벨 추가
        label = axes.get_graph_label(tangent_graph, label="\\tan(x)")

        # 애니메이션
        self.play(Create(axes))
        self.play(Create(asymptotes))
        self.play(Create(tangent_graph), Write(label))
        self.wait()
