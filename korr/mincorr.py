import numpy as np


def mincorr_cost_func(tmp, cost_func):
    if cost_func in ['sum', 'avg']:
        # corr sum of each "available" k to the "selected" i
        sk = np.sum(tmp, axis=0)
    elif cost_func in ['sqrt', 'squared']:
        sk = np.sum(np.power(tmp, 2), axis=0)
    elif cost_func in ['mu_max']:
        sk = np.mean(tmp, axis=0) + np.max(tmp, axis=0)
    return sk


def mincorr(cmat, n_stop=5, max_rho=0.4, init_method='avg',
            cost_fn='sqrt', verbose=True):
    # declare list of indicies
    available = list(range(cmat.shape[0]))
    selected = []

    # prep: convert to abs correlations
    absrho = np.abs(cmat, order='C')

    # (1) Initial Condition
    # (1a) find "i" with the lowest correlations
    if init_method in ['sum', 'avg']:
        si = np.sum(absrho, axis=1)
    elif init_method in ['low', 'lowest', 'min']:
        si = np.min(absrho, axis=1)  # same as picking the lowest |r_ij|
    else:
        raise Exception(
            "unknown init_method='{:s}' value".format(str(init_method)))

    i = np.argmin(si)
    selected.append(i)
    available.remove(i)

    # (1b) find "j" with the lowest correlation |r_ij| given "i"
    j = np.argmin(absrho[i, :])
    selected.append(j)
    available.remove(j)

    # (2) Enforce max abs correlation
    if max_rho < 1.0:
        # (2a) reset all absrho>maxrho to np.inf
        absrho[absrho > max_rho] = np.inf

        # (2b) add features if corr to previously
        # selected features is below max_rho
        for _ in range(2, n_stop):
            # slice available
            tmp = absrho[selected, :]  # slice \r_ij| given i \in "selected"
            tmp = tmp[:, available]  # remove "selected" colums (with 1s)
            # find best
            # sk = np.sum(np.power(tmp,2), axis=0)
            sk = mincorr_cost_func(tmp, cost_fn)
            k = np.argmin(sk)   # find index with lowest cost func
            if sk[k] < np.inf:
                # store indicies
                j = available[k]  # get the index
                selected.append(j)
                available.remove(j)
            else:
                if verbose:
                    print(("Terminated: max_rho={:5.3f} works only "
                           "for {:d} features".format(max_rho, _)))
                break
        # (2c) Reset matrix
        absrho = np.abs(cmat, order='C')

    # (3) fill the remaining spots
    for _ in range(len(selected), n_stop):
        # slice available
        tmp = absrho[selected, :]  # slice \r_ij| given i \in "selected"
        tmp = tmp[:, available]  # remove "selected" colums (with 1s)
        # find best
        # sk = np.sum(np.power(tmp,2), axis=0)
        sk = mincorr_cost_func(tmp, cost_fn)
        k = np.argmin(sk)  # find index with lowest cost func
        # store indicies
        j = available[k]  # get the index
        selected.append(j)
        available.remove(j)

    # done
    return selected


def mincorr_result_check(cmat, selected):
    print("selected: ", selected)
    print("avg abs corr: {:7.4f}".format(
        np.sum(np.abs(np.tril(cmat[selected, :][:, selected], -1))) / (
            (len(selected) - 1) * len(selected) / 2)))
    print("selected corr matrix:\n", cmat[selected, :][:, selected].round(3))
    print("")
