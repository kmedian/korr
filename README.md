[![PyPI version](https://badge.fury.io/py/korr.svg)](https://badge.fury.io/py/korr)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/kmedian/korr.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kmedian/korr/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/kmedian/korr.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kmedian/korr/context:python)

# korr
collection of utility functions for correlation analysis


## Usage
Check the [examples](https://github.com/kmedian/korr/tree/master/examples) folder for notebooks.

Compute correlation matrix and its p-values

* [pearson](https://github.com/kmedian/korr/blob/master/examples/pearson.ipynb) -- Pearson/Sample correlation (interval- and ratio-scale data)
* [kendall](https://github.com/kmedian/korr/blob/master/examples/kendall.ipynb) -- Kendall's tau rank correlation (ordinal data)
* [spearman](https://github.com/kmedian/korr/blob/master/examples/spearman.ipynb) -- Spearman rho rank correlation (ordinal data)
* [mcc](https://github.com/kmedian/korr/blob/master/examples/mcc%20(Matthews%20correlation).ipynb) -- Matthews correlation coefficient between binary variables 

EDA, Dig deeper into results

* [flatten](https://github.com/kmedian/korr/blob/master/examples/flatten.ipynb) -- A table (pandas) with one row for each correlation pairs with the variable indicies, corr., p-value. For example, try to find "good" cutoffs with `corr_vs_pval` and then look up the variable indicies with `flatten` afterwards.
* [slice_yx](https://github.com/kmedian/korr/blob/master/examples/slice_yx.ipynb) -- slice a correlation and p-value matrix of a (y,X) dataset into a (y,x_i) vector and (x_j, x_k) matrices
* [corr_vs_pval](https://github.com/kmedian/korr/blob/master/examples/corr_vs_pval.ipynb)  -- Histogram to find p-value cutoffs (alpha) for a) highly correlated pairs, b) unrelated pairs, c) the mixed results. 
* [bracket_pval](hhttps://github.com/kmedian/korr/blob/master/examples/bracket_pval.ipynb) -- Histogram with more fine-grained p-value brackets. 
* [corrgram](https://github.com/kmedian/korr/blob/master/examples/corrgram.ipynb) -- Correlogram, heatmap of correlations with p-values in brackets

Utility functions

* [confusion](https://github.com/kmedian/korr/blob/master/examples/confusion.ipynb) -- Confusion matrix. Required for Matthews correlation (mcc) and is a bitter faster than sklearn's 

Parameter Stability

* [bootcorr](https://github.com/kmedian/korr/blob/master/examples/bootcorr.ipynb) -- Estimate multiple correlation matrices based on bootstrapped samples. From there you can assess how stable correlation estimates are (how sensitive against in-sample variation). For example, stable estimates are good candidates for modeling, and unstable correlation pairs are good candidates for P-hacking and non-reproducibility.

Variable Selection, Search Functions

* [mincorr](https://github.com/kmedian/korr/blob/master/examples/mincorr.ipynb) -- From all estimated correlation pairs, pick a given `n=3,5,..` of variables with low and insignificant correlations among each other. (See [binsel](https://github.com/kmedian/binsel) package for an application.)
* `find_best` -- Find the N "best", i.e. high and most significant, correlations
* `find_worst` -- Find the N "worst", i.e. insignificant/random and low, correlations
* [find_unrelated](https://github.com/kmedian/korr/blob/master/examples/find_unrelated.ipynb) -- Return variable indicies of unrelated pairs (in terms of insignificant p-value)


## Appendix

### Installation
The `korr` [git repo](http://github.com/kmedian/korr) is available as [PyPi package](https://pypi.org/project/korr)

```
pip install korr
```

### Install a virtual environment

```
python3.7 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
pip install -r requirements-dev.txt --no-cache-dir
pip install -r requirements-demo.txt --no-cache-dir
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)


### Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```

### Support
Please [open an issue](https://github.com/kmedian/korr/issues/new) for support.


### Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/korr/compare/).
