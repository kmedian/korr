import numpy as np
import korr


def bootcorr(X, n_draws=30, subsample=0.7, replace=True,
             random_state=42, corr_fn=korr.pearson):
    """Estimate multiple correlation matrices based on
    bootstrapped samples.

    The produced correlation matrices can be used to
    check if certain correlation estimates are stable.

    Parameters
    ----------
    n_draws : int
        number of bootstraps.

    subsample : float
        percentage of samples to use in every estimation.

    replace: bool
        True (default) with replacement, i.e. samples can be used multiple
        times (bootstrapping).
        False is without replacement, i.e. samples are used once, sample are
        not reused (SRSWOR)

    corr_fn : function
        python function that returns a correlation matrix and matrix with
        corresponding p-values
    """
    # number of examples
    n_samples, n_features = X.shape

    # size
    if isinstance(subsample, int):
        n_size = subsample
    else:
        n_size = int(n_samples * subsample)

    # create empty tensors
    rho3 = np.zeros(shape=(n_draws, n_features, n_features))
    rho3[:] = np.nan

    pval3 = np.zeros(shape=(n_draws, n_features, n_features))
    pval3[:] = np.nan

    # set seed
    np.random.seed(random_state)

    for d in range(n_draws):
        idx = np.random.choice(range(n_samples), size=n_size, replace=replace)
        rho3[d], pval3[d] = corr_fn(X[idx, :])

    # done
    return rho3, pval3
