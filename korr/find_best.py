import warnings
import numpy as np


def find_best(rho, pval, m=1, rlim=.4, plim=.01):
    """Find the N "best", i.e. high and most significant, correlations

    Parameters
    ----------
    rho : ndarray, list
        1D array with correlation coefficients

    pval : ndarray, list
        1D array with p-values

    m : int
        The desired number of indicies to return
        (How many "best" correlations to find?)

    rlim : float
        Desired minimum absolute correlation coefficient
        (Default: 0.40)

    plim : float
        Desired maximum p-value
        (Default: 0.01)

    Return
    ------
    selected : list
        Indicies of rho and pval of the "best" correlations.
    """
    # convert to lists
    n = len(rho)
    r = list(np.abs(rho))
    p = list(pval)
    i = list(range(n))

    # check m
    if m > n:
        warnings.warn(
            'm is bigger than the available correlations in rho and pval.')
        m = n

    # selected indicies
    selected = list()
    # (1) pick the highest |r| that are
    #   |r| >= r_lim
    #    p  <  p_lim
    it = 0
    while (len(selected) < m) and (it < n):
        # find the best |r| of the remaining values
        temp = r.index(max(r))  # temporary index of the remaining values
        best = i[temp]  # store original index  as 'best' before abort loop
        # check
        if (r[temp] >= rlim) and (p[temp] < plim):
            # delete from lists
            r.pop(temp)
            p.pop(temp)
            i.pop(temp)
            # append to abort
            selected.append(best)
        # next step
        it = it + 1
    # print(selected, i)

    # (2) Just pick the highest |r| of the remaining
    # with substantial p-values
    #    p  <  p_lim
    it = 0
    n2 = len(i)
    while (len(selected) < m) and (it < n2):
        # find the best |r| of the remaining values
        temp = r.index(max(r))  # temporary index of the remaining values
        best = i[temp]  # store original index  as 'best' before abort loop
        # check
        if (p[temp] < plim):
            # delete from lists
            r.pop(temp)
            p.pop(temp)
            i.pop(temp)
            # append to abort
            selected.append(best)
        # next step
        it = it + 1

    # (3) Pick the lowest p-values
    # If the correlations aren't useful, then prefer the p-values
    it = 0
    n3 = len(i)
    while (len(selected) < m) and (it < n3):
        # find the smallest p-value
        temp = p.index(min(p))
        best = i[temp]
        # delete from lists
        r.pop(temp)
        p.pop(temp)
        i.pop(temp)
        # append to abort
        selected.append(best)
        # next step
        it = it + 1

    return selected
