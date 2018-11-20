import scipy.stats  # pearsonr
import numpy as np


def find_unrelated(x, plim=0.1, axis=0):
    """Find indicies of insignificant un-/correlated variables

    Example:
    --------
        i, j = find_unrelated(x, plim, rlim)

    """
    # transpose if axis<>0
    if axis is not 0:
        x = x.T

    # read dimensions and allocate variables
    _, c = x.shape
    pairs = []

    # compute each (i,j)-th correlation
    for i in range(0, c):
        for j in range(i + 1, c):
            _, p = scipy.stats.pearsonr(x[:, i], x[:, j])
            if p > plim:
                pairs.append((i, j))
    # done
    return tuple(pairs)
