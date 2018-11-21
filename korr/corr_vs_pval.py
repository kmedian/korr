import matplotlib.pyplot as plt
import numpy as np


def corr_vs_pval(r, pval, plim=0.01, rlim=0.4, dpi=96):
    """Histogram for correlation coefficients and its p-values (colored)

    Parameters:
    -----------
    r : np.ndarray
        Correlation coefficient matrix.
        The upper triangular elements are extracted if a NxN is provided.
        Otherwise provide a plain vector.

    pval : np.ndarray
        NxN matrix with p-values

    plim : float
        Discretionary alpha threshold to judge if a p-value is considered
        "significant" or not. (Default: 0.01 or 1%)

    rlim : float
        Descretionary threshold to judge if an absolute correlation
        coefficient is big enough. (Default: 0.4)

    dpi : int
        Set the resolution of the matplotlib graphics.

    Return:
    -------
    fig, ax
        matplotlib figure and axes for further tweaking
    """
    # reshape
    if len(r.shape) == 2:
        idx = (np.tri(N=r.shape[0], k=-1) == 1)
        r = r[idx]
        pval = pval[idx]

    # indicies for the three groups
    i1 = (pval >= plim)
    i2 = (pval < plim) & (np.abs(r) > rlim)
    i3 = (pval < plim) & (np.abs(r) <= rlim)

    # plot paramters
    absmax = np.max(np.abs(r))
    b = (np.arange(0, 21) / 10 - 1) * absmax
    c = plt.get_cmap('tab10').colors
    c = (c[1], c[8], c[7])

    # create plot
    fig, ax = plt.subplots(dpi=dpi)
    ax.hist((r[i1], r[i2], r[i3]), histtype='bar',
            stacked=True, bins=b, color=c)

    # legend, title, labels
    ax.legend(['p >= ' + str(plim),
               'p < ' + str(plim) + ' and |r| > ' + str(rlim),
               'p < ' + str(plim) + ' and |r| <= ' + str(rlim)],
              loc=2, bbox_to_anchor=(1.04, 1.04))
    ax.set_ylabel('frequency')
    ax.set_xlabel('correlation coefficient')

    # design grid
    ax.grid(color='darkgray', linestyle='-.')
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    # output figure/axes onbjects
    return fig, ax
