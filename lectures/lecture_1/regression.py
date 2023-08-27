from random import uniform
import os
from manim import *


class Regression(Scene):
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
        decision_boundary = DashedLine(ax.coords_to_point(0, 1), ax.coords_to_point(10, 9), color=DARK_BROWN)
        dot_radius = 0.2
        dots = []
        for i in range(30):
            if i < 3:
                x = (i + uniform(0, 4)) / 3.2
                y = (i + uniform(-1, 10)) / 3.2
            elif i > 17:
                x = (i + uniform(-4, 2)) / 3.2
                y = (i + uniform(-5, 5)) / 3.2
            else:
                x = (i + uniform(-2, 4)) / 3.2
                y = (i + uniform(-5, 5)) / 3.2
            dots.append(Dot(ax.coords_to_point(x, y), radius=dot_radius, color=BLUE))
        self.add(
            ax,
            labels,
            decision_boundary,
            *dots,
        )


if __name__ == '__main__':
    os.system("manim -pqh regression.py Regression")
