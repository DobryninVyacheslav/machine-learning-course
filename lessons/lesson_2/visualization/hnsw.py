import os

from manim import *

from lessons.constants import PICTURE_COMMAND


def get_circle(point):
    circle = Circle(radius=0.3, color=DARK_BLUE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
    circle.set_x(point[0])
    circle.set_y(point[1])
    circle.set_z(point[2])
    return circle


class HNSW(ThreeDScene):
    def construct(self):
        resolution_fa = 1
        self.set_camera_orientation(phi=72 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))

        layer_2 = Surface(
            lambda u, v: axes.c2p(u, v, 1),
            resolution=(resolution_fa, resolution_fa),
            v_range=[1, 5],
            u_range=[1, 4],
        )
        layer_2.set_style(fill_opacity=0.3, stroke_width=4, stroke_color=GRAY)

        layer_1 = Surface(
            lambda u, v: axes.c2p(u, v, 0.5),
            resolution=(resolution_fa, resolution_fa),
            v_range=[1, 5],
            u_range=[1, 4],
        )
        layer_1.set_style(fill_opacity=0.3, stroke_width=4, stroke_color=GRAY)

        layer_0 = Surface(
            lambda u, v: axes.c2p(u, v, -0.25),
            resolution=(resolution_fa, resolution_fa),
            v_range=[1, 5],
            u_range=[1, 4],
        )
        layer_0.set_style(fill_opacity=0.3, stroke_width=4, stroke_color=GRAY)

        # layer_2.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        # self.add(axes)

        self.add(
            layer_0,
            layer_1,
            layer_2,
            get_circle(axes.c2p(2, 4.5, 1)),
            get_circle(axes.c2p(2, 4.5, 0.5)),
            get_circle(axes.c2p(2, 4.5, -0.25)),
            get_circle(axes.c2p(2.1, 2, 1)),
            get_circle(axes.c2p(2.1, 2, 0.5)),
            get_circle(axes.c2p(2.1, 2, -0.25)),
        )


if __name__ == '__main__':
    os.system(f"{PICTURE_COMMAND} {__file__} HNSW")
