
def slice_yx(r, pval, ydim=1):
    """slice a correlation and p-value matrix of a (y,X) dataset
    into a (y,x_i) vector and (x_j, x_k) matrices

    Parameters
    ----------
    r : ndarray
        Correlation Matrix of a (y,X) dataset

    pval : ndarray
        p-values

    ydim : int
        Number of target variables y, i.e. the first ydim-th columns
        and rows are (y, x_i) correlations

    Returns
    -------
    y_r : ndarray
        1D vector or ydim-column array with (y,x) correlations

    y_pval : ndarray
        1D vector or ydim-column array with (y,x) p-values

    x_r : ndarray
        correlation matrix (x_j, x_k)

    x_pval : ndarar
        matrix with p-values

    Example
    -------
        import korr
        r, pval = korr.mcc(np.c_[y, X])
        y_r, y_pval, x_r, x_pval = slice_yx(r, pval, ydim=1)
        print(np.c_[y_r, y_pval])
        korr.corrgram(x_r, x_pval)
    """
    if ydim is 1:
        return (
            r[1:, :1].reshape(-1, ), pval[1:, :1].reshape(-1, ),
            r[1:, 1:], pval[1:, 1:])
    else:
        return (
            r[ydim:, :ydim], pval[ydim:, :ydim],
            r[ydim:, ydim:], pval[ydim:, ydim:])
