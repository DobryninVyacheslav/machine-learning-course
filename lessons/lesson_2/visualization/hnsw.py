import os

from manim import *

from lessons.constants import PICTURE_COMMAND


def get_circle(point):
    circle = Circle(radius=0.3, color=DARK_BLUE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
    circle.set_x(point[0])
    circle.set_y(point[1])
    circle.set_z(point[2])
    return circle


def get_arrow(start, end):
    return Arrow(start, end, stroke_width=2)


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

        e_p_l2 = get_circle(axes.c2p(2, 4.5, 1))
        p2_l2 = get_circle(axes.c2p(2.1, 2, 1))
        group_2 = VGroup(
            layer_2,
            e_p_l2,
            p2_l2,
        )
        p1_l1 = get_circle(axes.c2p(2, 4.5, 0.5))
        p2_l1 = get_circle(axes.c2p(3.5, 4.6, 0.5))
        p3_l1 = get_circle(axes.c2p(3, 3.9, 0.5))
        p4_l1 = get_circle(axes.c2p(1.8, 2.8, 0.5))
        p5_l1 = get_circle(axes.c2p(2.1, 2, 0.5))
        p6_l1 = get_circle(axes.c2p(3.4, 2.5, 0.5))
        group_1 = VGroup(
            layer_1,
            Line(p1_l1.get_center(), p2_l1.get_center(), color=GRAY),
            Line(p1_l1.get_center(), p3_l1.get_center(), color=GRAY),
            Line(p2_l1.get_center(), p3_l1.get_center(), color=GRAY),
            Line(p3_l1.get_center(), p4_l1.get_center(), color=GRAY),
            Line(p4_l1.get_center(), p5_l1.get_center(), color=GRAY),
            p1_l1,
            p2_l1,
            p3_l1,
            p4_l1,
            p5_l1,
            p6_l1,
        )
        p1_l0 = get_circle(axes.c2p(2, 4.5, -0.25))
        p2_l0 = get_circle(axes.c2p(3.5, 4.6, -0.25))
        p3_l0 = get_circle(axes.c2p(3, 3.9, -0.25))
        p4_l0 = get_circle(axes.c2p(2, 3.8, -0.25))
        p5_l0 = get_circle(axes.c2p(1.8, 2.8, -0.25))
        p6_l0 = get_circle(axes.c2p(2.1, 2, -0.25))
        p7_l0 = get_circle(axes.c2p(3.4, 2.5, -0.25))
        p8_l0 = get_circle(axes.c2p(2.8, 3, -0.25))
        p9_l0 = get_circle(axes.c2p(3.5, 3.2, -0.25))
        group_0 = VGroup(
            layer_0,
            Line(p1_l0.get_center(), p4_l0.get_center(), color=GRAY),
            Line(p2_l0.get_center(), p4_l0.get_center(), color=GRAY),
            Line(p3_l0.get_center(), p4_l0.get_center(), color=GRAY),
            Line(p4_l0.get_center(), p5_l0.get_center(), color=GRAY),
            Line(p4_l0.get_center(), p8_l0.get_center(), color=GRAY),
            Line(p5_l0.get_center(), p8_l0.get_center(), color=GRAY),
            Line(p6_l0.get_center(), p8_l0.get_center(), color=GRAY),
            Line(p7_l0.get_center(), p8_l0.get_center(), color=GRAY),
            p1_l0,
            p2_l0,
            p3_l0,
            p4_l0,
            p5_l0,
            p6_l0,
            p7_l0,
            p8_l0,
            p9_l0,
        )
        self.add(
            group_2,
            group_1,
            group_0,
            DashedLine(e_p_l2.get_center(), p1_l1.get_center()),
            DashedLine(p6_l1.get_center(), p7_l0.get_center()),
            DashedLine(p5_l1.get_center(), p6_l0.get_center()),
            DashedLine(p4_l1.get_center(), p5_l0.get_center()),
            DashedLine(p2_l1.get_center(), p2_l0.get_center()),
            DashedLine(p1_l1.get_center(), p1_l0.get_center()),
        )
        self.play(Create(get_arrow(e_p_l2.get_center(), p2_l2.get_center())))
        self.play(Create(get_arrow(p2_l2.get_center(), p5_l1.get_center())))
        self.play(Create(get_arrow(p5_l1.get_center(), p6_l1.get_center())))
        self.play(Create(get_arrow(p6_l1.get_center(), p3_l1.get_center())))
        self.play(Create(get_arrow(p3_l1.get_center(), p3_l0.get_center())))
        self.play(Create(get_arrow(p3_l0.get_center(), p8_l0.get_center())))


if __name__ == '__main__':
    os.system(f"{PICTURE_COMMAND} {__file__} HNSW")
