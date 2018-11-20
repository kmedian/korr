[![Build Status](https://travis-ci.org/kmedian/korr.svg?branch=master)](https://travis-ci.org/kmedian/korr)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/korr/master?urlpath=lab)

# korr
collection of utility functions for correlation analysis


## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `korr` [git repo](http://github.com/kmedian/korr) is available as [PyPi package](https://pypi.org/project/korr)

```
pip install korr
```


## Usage
Check the [examples](examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi: `python setup.py sdist upload -r pypi`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Debugging
* Notebooks to profile python code are in the [profile](profile) folder


## Support
Please [open an issue](https://github.com/kmedian/korr/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/korr/compare/).
