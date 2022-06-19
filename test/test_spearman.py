import korr
import numpy as np


def test1():
    X = np.random.random((100, 3))
    rho, pval = korr.spearman(X)
    assert rho.shape == pval.shape
    assert rho.shape == (3, 3)
    assert (rho >= -1).all() and (rho <= 1.0).all()
