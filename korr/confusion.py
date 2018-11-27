import numpy as np


def confusion(a, p):
    """Confusion Matrix

    - confusion matrix, error matrix, matching matrix (unsupervised)
    - is a special case: 2x2 contingency table (xtab, RxC table)
    - both dimensions are variables with the same classes/labels,
      i.e. actual and predicted variables are binary [0,1]

    Parameters:
    -----------
    a : ndarray
        Actual values, binary [0,1]

    p : ndarray
        Predicted values, binary [0,1]

    Returns:
    --------
    cm : ndarray
        Confusion matrix

                       predicted=0   predicted=1
            actual=0        tn           fp
            actual=1        fn           tp

    Example:
    --------
        import korr
        cm = korr.confusion(a, p)
        tn, fp, fn, tp = cm.ravel()

    Alternatives:
    -------------
        import pandas as pd
        cm = pd.crosstab(a, p)

        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(a, p)
    """
    m = a == p  # matches (a=1, p=1) and (a=0, p=0)
    f = np.logical_not(m)  # xor (a=1, p=0) and (a=0, p=1)
    tp = np.sum(np.logical_and(m, a))  # 11
    tn = np.sum(np.logical_and(m, np.logical_not(a)))  # 00
    fn = np.sum(np.logical_and(f, a))  # 10
    fp = np.sum(np.logical_and(f, p))  # 01
    return np.array([[tn, fp], [fn, tp]])
