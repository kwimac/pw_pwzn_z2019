import numpy as np


def least_sq(xy):
    """
    Fits linear function to given vector of 2D points.

    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.
    (1 pkt.)

    A = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    B = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: vector of 2D points (shape (2, n))
    :type xy: np.ndarray
    :return: Tuple of fitted parameters
    """
    x = xy[0]
    y = xy[1]

    sum_x2 = np.sum(x ** 2)
    sum_y = np.sum(y)
    sum_x = np.sum(x)
    sum_xy = np.sum(x * y)
    n = len(x)

    delta = n * (sum_x2) - (sum_x) ** 2
    a = ((sum_x2) * (sum_y) - (sum_x) * (sum_xy)) / delta
    b = (n * (sum_xy) - (sum_x) * (sum_y)) / delta

    return a, b