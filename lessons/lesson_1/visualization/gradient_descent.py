import os

from manim import *

from lessons.constants import ANIM_COMMAND


class GradientDescent(Scene):
    """
    Alternative way to create tangent line:
        tl = always_redraw(
            lambda: TangentLine(
                plotted_parabola,
                x_tracker.get_value() / 10.0,
                length=4,
                color=GREEN,
            )
        )
        self.play(Create(VGroup(dot, tl)))
    """

    def construct(self):
        ax = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 10, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip": False, "color": BLACK}
        ).to_edge(DL)

        x_tracker = ValueTracker(2)
        vertex_x = 5

        def parabola(x):
            return .6 * (x - vertex_x) ** 2

        dot = Dot(point=ax.coords_to_point(x_tracker.get_value(), parabola(x_tracker.get_value())), color=RED)
        dot.add_updater(lambda x: x.move_to(ax.c2p(x_tracker.get_value(), parabola(x_tracker.get_value()))))

        plotted_parabola = ax.plot(lambda x: parabola(x), [1, 9, 1], color=BLUE)
        tangent = always_redraw(lambda: ax.get_secant_slope_group(
            x=x_tracker.get_value(),
            graph=plotted_parabola,
            dx=.001,
            secant_line_length=4,
            secant_line_color=RED,
        ))
        der_formula = MathTex("\\nabla Q=\\lim_{h \\to 0}\\frac{Q(w+h)-Q(w)}{h}", color=BLACK).shift(RIGHT * 4 + DOWN)

        self.add(
            ax,
            ax.get_axis_labels(x_label="w", y_label="Q(w)").set_color(BLACK),
            plotted_parabola,
        )
        self.play(Create(VGroup(dot, tangent)))
        self.play(Write(der_formula))
        self.play(x_tracker.animate.set_value(vertex_x), run_time=5)
        self.wait()


if __name__ == '__main__':
    os.system(f"{ANIM_COMMAND} {__file__} GradientDescent")
