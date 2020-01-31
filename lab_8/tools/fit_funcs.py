# -*- coding: utf-8 -*-
import numpy
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

    x = xy[:,0]
    y = xy[:,1]
    x_sq = x*x
    y_sq = y*y
    x_times_y = x*y
    mean_x = numpy.mean(x)
    mean_y = numpy.mean(y)
    N = x.shape[0]
    A = ((N*sum(x*y))-(sum(x)*sum(y)))/((N*sum(x_sq))-sum(x)**2)
    B = (sum(y) - A*sum(x))/N
    return A, B
