import os

from manim import *
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from lectures.constants import MANIM_COMMAND


def get_axes_and_labels():
    axes = Axes(x_range=[-1, 10, 1], y_range=[-1, 10, 1], x_length=9, y_length=6,
                axis_config={"include_tip": False, "color": BLACK})
    return axes, axes.get_axis_labels().set_color(BLACK)


coordinates = [[1, 1], [1.5, 4], [2.5, 7], [4.5, 8], [7, 8.25], [9, 8.5]]


def get_crosses(ax: Axes):
    crosses = []
    for [x, y] in coordinates:
        crosses.append(Cross(Dot(ax.coords_to_point(x, y))))
    return crosses


class Underfitting(Scene):
    def construct(self):
        (ax, labels) = get_axes_and_labels()
        self.add(
            ax,
            labels,
            *get_crosses(ax),
            ax.plot_line_graph((-1, 10), (1, 10), add_vertex_dots=False, line_color=BLUE)
        )


class Fitting(Scene):

    def construct(self):
        (ax, labels) = get_axes_and_labels()
        values = {1: 0,
                  2: 5,
                  3: 7,
                  4: 7.7,
                  5: 7.95,
                  6: 8.1,
                  7: 8.25,
                  8: 8.4,
                  9: 8.5,
                  10: 8.6
                  }
        self.add(
            ax,
            labels,
            *get_crosses(ax),
            ax.plot(lambda x: values.get(x), [1, 10, 1], color=BLUE),
        )


class Overfitting(Scene):

    def construct(self):
        (ax, labels) = get_axes_and_labels()
        coordinates_array = np.array(coordinates)
        X = coordinates_array[:, 0].reshape(-1, 1)
        y = coordinates_array[:, 1]
        poly_features = PolynomialFeatures(degree=6)
        X_poly = poly_features.fit_transform(X)
        model = LinearRegression()
        model.fit(X_poly, y)
        self.add(
            ax,
            labels,
            *get_crosses(ax),
            ax.plot(lambda x: model.predict(poly_features.transform(np.array(x).reshape(-1, 1)))[0],
                    [0, 10, 1],
                    color=BLUE),
        )


if __name__ == '__main__':
    os.system(f"{MANIM_COMMAND} {__file__} Overfitting")
