from manim import *

class DrawSine(Scene):
    def construct(self):
        # 좌표축 생성
        axes = Axes(
            x_range=[-15, 15, 1],
            y_range=[-1.2, 1.2, 0.5],
            axis_config={"include_tip": False}
        )

        # 사인 함수 정의 및 그래프 생성
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        # 그래프에 라벨 추가 (선택 사항)
        graph_label = axes.get_graph_label(graph, label="\\sin(x)")

        # 애니메이션 실행
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait()