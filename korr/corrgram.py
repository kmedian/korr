
import matplotlib.pyplot as plt
import numpy as np


def corrgram(r, pval, varnames=None, dpi=96, cmap='RdBu'):
    # cmap: RdBu, PuOr, coolwarm

    # use numbers as
    if varnames is None:
        varnames = [str(i) for i in range(r.shape[1])]

    # number of variables
    num = len(varnames)

    # create figure and axes objects
    fig, ax = plt.subplots(dpi=dpi, figsize=(num * .75, num * .75))
    # fig.tight_layout()

    # plot heatmap
    im = ax.imshow(r, cmap=cmap, interpolation='nearest', vmin=-1, vmax=1)

    # axis formating
    plt.yticks(range(num), varnames)
    plt.xticks(range(num), varnames, rotation=45,
               ha="left", rotation_mode="anchor")
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
    # annotate axes
    ax.set_xticks(np.arange(num + 1) - .5, minor=True)
    ax.set_yticks(np.arange(num + 1) - .5, minor=True)
    ax.tick_params(which="minor", bottom=False, left=False)

    # Turn spines off and create white grid.
    ax.grid(which="minor", color="white", linestyle='-', linewidth=3)
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    # colorbar
    cbar = ax.figure.colorbar(im, fraction=0.046, pad=0.04)
    cbar.set_clim(vmin=-1, vmax=+1)
    cbar.ax.set_ylabel('correlation coefficient', rotation=-90, va="bottom")
    cbar.outline.set_edgecolor('darkgray')

    # add text
    for i in range(num):
        for j in range(num):
            if i is not j:
                # concate the text
                strtxt = (
                    '+' if r[i, j] > 0 else ('-' if r[i, j] < 0 else '')) \
                    + "." + '{:02d}'.format(int(abs(r[i, j]) * 100)) \
                    + '\n(.{:03d})'.format(int(pval[i, j] * 1000))
                # color depending on the absolute corr coeff value
                strcol = "gray" if abs(r[i, j]) < 0.4 else "white"
                # add the text to the graph
                ax.text(j, i, strtxt, ha="center",
                        va="center", color=strcol)

    # white bg
    fig.patch.set_facecolor('white')

    # for later usage
    return fig, ax, cbar
