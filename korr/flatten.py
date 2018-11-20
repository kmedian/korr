import pandas as pd
import numpy as np


def flatten(rho, pval, sortby="cor"):
    """Flatten correlation and p-value matrix

    Parameters:
    -----------
    rho : ndarray
        Correlation Matrix

    pval : ndarray
        Matrix with p-values

    sortby : str
        sort the output table by
        - "cor"  the highest absolute correlation coefficient
        - "pval" the lowest p-value

    Return:
    -------
    tab : ndarray
        Table with (i, j, cor, pval) rows

    Example:
    --------
        from korr import pearson, flatten
        rho, pval = pearson(X)
        tab = flatten(rho, pval, sortby="pval")
        tab.values
    """
    n = rho.shape[0]

    idx = np.triu_indices(n, k=1)

    tab = pd.DataFrame(
        columns=['i', 'j', 'cor', 'pval'],
        data=np.c_[idx[0], idx[1], rho[idx], pval[idx]])
    tab[['i', "j"]] = tab[['i', "j"]].astype(int)

    if sortby == "cor":
        tab['abscor'] = np.abs(tab['cor'])
        tab.sort_values(by='abscor', inplace=True, ascending=False)
    elif sortby == "pval":
        tab.sort_values(by='pval', inplace=True, ascending=True)

    return tab[["i", "j", "cor", "pval"]]
