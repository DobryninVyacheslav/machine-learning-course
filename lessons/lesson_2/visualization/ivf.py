import os
from manim import *
from manim import Dot, ORANGE
from itertools import chain

from lessons.constants import PICTURE_COMMAND


def get_arrow(start, end, color=ORANGE):
    return Arrow(
        start,
        end,
        color=color,
        stroke_width=0,
        background_stroke_color=color,
        background_stroke_width=5,
        background_stroke_opacity=1,
        max_tip_length_to_length_ratio=1,
    )


def get_dots_by_cluster_map(ax):
    return {
        # 1 cluster
        1: [
            Dot(ax.c2p(1, 3), color=BLUE),
            Dot(ax.c2p(2.5, 4), color=BLUE),
            Dot(ax.c2p(0.5, 9), color=BLUE),
            Dot(ax.c2p(2.9, 8), color=BLUE),
        ],
        # 2 cluster
        2: [
            Dot(ax.c2p(3, 1), color=BLUE),
            Dot(ax.c2p(3.5, 3), color=BLUE),
            Dot(ax.c2p(4.5, 1.5), color=BLUE),
            Dot(ax.c2p(7, 4), color=BLUE),
            Dot(ax.c2p(8, 2), color=BLUE),
            Dot(ax.c2p(7.2, 2.5), color=BLUE),
        ],
        # 3 cluster
        3: [
            Dot(ax.c2p(4.5, 7.8), color=BLUE),
            Dot(ax.c2p(4.2, 9.6), color=BLUE),
            Dot(ax.c2p(6, 8.5), color=BLUE),
            Dot(ax.c2p(9.5, 9), color=BLUE),
            Dot(ax.c2p(7.2, 7), color=BLUE),
        ],
        # 4 cluster
        4: [
            Dot(ax.c2p(9.5, 1.8), color=BLUE),
            Dot(ax.c2p(7.8, 5.4), color=BLUE),
            Dot(ax.c2p(9.6, 6.7), color=BLUE),
        ],
    }


def get_centroids(ax):
    return [
        Cross(Dot(ax.c2p(1.8, 6))),
        Cross(Dot(ax.c2p(6.7, 8))),
        Cross(Dot(ax.c2p(8.8, 5))),
        Cross(Dot(ax.c2p(5.5, 3))),
    ]


def get_dividing_lines(ax):
    common_point_1 = ax.c2p(3.9, 7)
    common_point_2 = ax.c2p(7, 5.7)
    return [
        Line(ax.c2p(2.3, 0), common_point_1, color=BLACK),
        Line(ax.c2p(3.5, 10), common_point_1, color=BLACK),
        Line(common_point_1, common_point_2, color=BLACK),
        Line(common_point_2, ax.c2p(9.4, 0), color=BLACK),
        Line(common_point_2, ax.c2p(10, 7.9), color=BLACK),
    ]


class IVF(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={
                "color": BLACK
            }
        )

        query_dot = Dot(ax.c2p(7, 1), radius=0.2, color=ORANGE)
        query_dot_text = Text("Вектор запроса", font_size=18, color=BLACK)
        query_dot_text.next_to(query_dot, DOWN)
        centroids = get_centroids(ax)
        dots_by_cluster_map = get_dots_by_cluster_map(ax)

        self.add(
            query_dot_text,
            *chain.from_iterable(dots_by_cluster_map.values()),
            *centroids,
            *get_dividing_lines(ax),
            query_dot,
        )
        for centroid in centroids[:-1]:
            arrow = get_arrow(query_dot.get_center(), centroid.get_center())
            self.play(Create(arrow))
            self.play(FadeOut(arrow))

        self.play(Create(get_arrow(query_dot.get_center(), centroids[-1].get_center(), color=BLUE_A)))

        for dot in dots_by_cluster_map[2][:-1]:
            arrow = get_arrow(query_dot.get_center(), dot.get_center())
            self.play(Create(arrow))
            self.play(FadeOut(arrow))

        self.play(Create(get_arrow(query_dot.get_center(), dots_by_cluster_map[2][-1].get_center(), color=GREEN)))
        self.play(FadeToColor(dots_by_cluster_map[2][-1], color=GREEN, run_time=1))
        self.wait(3)


if __name__ == '__main__':
    os.system(f"{PICTURE_COMMAND} {__file__} IVF")
