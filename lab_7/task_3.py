import numpy as np

# termin do poniedzialku do 23:59
def estimate_pi(n):
    """
    Returns estimated value of pi.

    Funkcja szacuje wartość pi metodą probabilistyczną.
    Wygenerujmy m punktów z obszaru [-1,1]^2. Niech k określa liczbę punktów
    odległych od punku (0,0) o nie więcej niż 1. Proporcja 4k/m
    powinna szacować wartość pi.
    (1pkt).

    :param n: Number of points to made estimation.
    :type xy: int
    :return: Estimated Pi value
    :rtype: float
    """
    points = np.random.uniform(-1,1,(n,2))
    dist = (points[:, 0]**2 + points[:, 1]**2)**0.5
    k = np.where(dist < 1)[0].shape[0]
    return 4 * k / n


if __name__ == '__main__':


    np.testing.assert_approx_equal(estimate_pi(int(1e2)), np.pi, 1)
    np.testing.assert_approx_equal(estimate_pi(int(1e3)), np.pi, 2)
