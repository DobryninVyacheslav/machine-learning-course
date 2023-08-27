import os
from random import uniform

from manim import *


class Classification(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 10, 1],
            x_length=9,
            y_length=6,
            axis_config={
                "include_tip": False,
                "color": BLACK
            }
        )
        labels = ax.get_axis_labels()
        labels.set_color(BLACK)
        decision_boundary = DashedLine(ax.coords_to_point(0, 10), ax.coords_to_point(10, 0), color=DARK_BROWN)
        dot_radius = 0.2
        dots = []
        crosses = []
        for _ in range(20):
            dots.append(Dot(ax.coords_to_point(uniform(.1, 5), uniform(.1, 5)), radius=dot_radius, color=BLUE))
            dot = Dot(ax.coords_to_point(uniform(5, 10), uniform(5, 10)), radius=dot_radius)
            crosses.append(Cross(dot, stroke_color=PURPLE))
        self.add(
            ax,
            labels,
            decision_boundary,
            *dots,
            *crosses
        )


if __name__ == '__main__':
    os.system("manim -pqh classification.py Classification")
