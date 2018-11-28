import warnings
import numpy as np


def find_worst(rho, pval, m=1, rlim=.10, plim=.35):
    """Find the N "worst", i.e. insignificant/random and low, correlations

    Parameters
    ----------
    rho : ndarray, list
        1D array with correlation coefficients

    pval : ndarray, list
        1D array with p-values

    m : int
        The desired number of indicies to return
        (How many "worst" correlations to find?)

    rlim : float
        Desired maximum absolute correlation coefficient
        (Default: 0.10)

    plim : float
        Desired minimum p-value
        (Default: 0.35)

    Return
    ------
    selected : list
        Indicies of rho and pval of the "worst" correlations.
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
    # (1) pick the highest/worst p-value
    #   |r| <= r_lim
    #    p  >  p_lim
    it = 0
    while (len(selected) < m) and (it < n):
        temp = p.index(max(p))  # temporary index of the remaining values
        worst = i[temp]  # store original index  as 'worst' before abort loop
        # check
        if (r[temp] <= rlim) and (p[temp] > plim):
            # delete from lists
            r.pop(temp)
            p.pop(temp)
            i.pop(temp)
            # append to abort
            selected.append(worst)
        # next step
        it = it + 1
    # print(selected, i)

    # (2) Just pick the highest/worst p-value of the remaining
    # with bad correlations
    #    |r| <=  r_lim
    it = 0
    n2 = len(i)
    while (len(selected) < m) and (it < n2):
        temp = p.index(max(p))  # temporary index of the remaining values
        worst = i[temp]  # store original index  as 'worst' before abort loop
        # check
        if (r[temp] <= rlim):
            # delete from lists
            r.pop(temp)
            p.pop(temp)
            i.pop(temp)
            # append to abort
            selected.append(worst)
        # next step
        it = it + 1

    # (3) Pick the lowest correlations
    it = 0
    n3 = len(i)
    while (len(selected) < m) and (it < n3):
        # find the smallest p-value
        temp = r.index(min(r))
        worst = i[temp]
        # delete from lists
        r.pop(temp)
        p.pop(temp)
        i.pop(temp)
        # append to abort
        selected.append(worst)
        # next step
        it = it + 1

    return selected
