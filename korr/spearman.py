import scipy.stats  # spearmanr
import numpy as np


def spearman(x, axis=0):
    """Spearman's Rho as Rank Correlation Matrix(for ordinal data)

    Parameters
    ----------
    x : ndarray
        data set

    axis : int, optional
        Variables as columns is the default (axis=0).
        If variables are in the rows use axis=1

    Returns
    -------
    r : ndarray
        Rank Correlation Matrix (Spearman rho)

    p : ndarray
        p-values
    """
    # transpose if axis<>0
    if axis is not 0:
        x = x.T

    # read dimensions and
    n, c = x.shape

    # check if enough variables provided
    if c < 2:
        raise Exception(
            "Only " + str(c) + " variables provided. Min. 2 required.")

    # allocate variables
    r = np.ones((c, c))
    p = np.zeros((c, c))

    # compute each (i,j)-th correlation
    for i in range(0, c):
        for j in range(i + 1, c):
            r[i, j], p[i, j] = scipy.stats.spearmanr(x[:, i], x[:, j])
            r[j, i] = r[i, j]
            p[j, i] = p[i, j]

    # done
    return r, p
