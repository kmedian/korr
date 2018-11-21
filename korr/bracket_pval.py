import matplotlib.pyplot as plt
import numpy as np


def bracket_pval(r, pval, plim=[.1, .01, .001], nbins=None, dpi=96):
    # reshape if r and pval are matricies
    # otherwise corr[i,j] would be counted twice
    if len(r.shape) == 2:
        idx = (np.tri(N=r.shape[0], k=-1) == 1)
        r = r[idx]
        pval = pval[idx]

    # Use nbins=20 from [-1,+1] for correlations
    if nbins is None:
        absmax = np.max(np.abs(r))
        nbins = (np.arange(0, 21) / 10 - 1) * absmax

    # set limits for p-values
    if isinstance(plim, list):
        plim = sorted(plim, reverse=True) + [0]
    elif isinstance(plim, int):
        plim = [pow(10, -i) for i in range(1, plim + 1)] + [0]

    # create subsets
    xlist = []
    names = []
    # add the subset pval=1 to the first plim item
    xlist.append(r[(pval >= plim[0])])
    names.append('p >= ' + str(plim[0]))
    # add the rest
    for i in range(1, len(plim)):
        pup = plim[i - 1]
        plo = plim[i]
        xlist.append(r[(pup > pval) & (pval >= plo)])
        names.append(str(pup) + ' > p >= ' + str(plo))

    # create histogram
    fig, ax = plt.subplots(dpi=dpi)
    ax.hist(xlist, histtype='bar', stacked=True, bins=nbins)

    # annotation
    ax.legend(names, loc=2, bbox_to_anchor=(1.04, 1.04))
    ax.set_ylabel('frequency')
    ax.set_xlabel('correlation coefficient')

    # design grid
    ax.grid(color='darkgray', linestyle='-.')
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    # output figure objects
    return fig, ax, xlist, names
