# py-minimal-script

A cookiecutter template that creates a minimalistic template for one-module Python scripts,
but with full project automation via Invoke and setuptools.

 [![Logo](https://raw.github.com/Springerle/py-generic-project/master/docs/_static/img/springerle-logo.png)](http://springerle.github.io/)
 [![Groups](https://img.shields.io/badge/Google_groups-springerle--users-orange.svg)](https://groups.google.com/forum/#!forum/springerle-users)
 ![MIT+CC0 licensed](http://img.shields.io/badge/license-MIT+CC0-red.svg)
 [![Travis CI](https://api.travis-ci.org/Springerle/py-minimal-script.svg)](https://travis-ci.org/Springerle/py-minimal-script)
 [![GitHub Issues](https://img.shields.io/github/issues/Springerle/py-minimal-script.svg)](https://github.com/Springerle/py-minimal-script/issues)
 [![GitHub Release](https://img.shields.io/github/release/Springerle/py-minimal-script.svg)](https://github.com/Springerle/py-minimal-script/releases)


## Features

The resulting project uses
[rituals](https://github.com/jhermann/rituals)
and [invoke](https://github.com/pyinvoke/invoke/)
for task automation, and
[setuptools](https://bitbucket.org/pypa/setuptools)
for building and distributing the script.
A provided [autoenv](https://github.com/kennethreitz/autoenv) script takes care
of creating a fully boot-strapped `virtualenv` – it can also be used manually
if you don't want to install `autoenv`.

Documentation for the script can be provided via the ``README.rst`` of the project,
which is also used for the PyPI entry. Having no full Sphinx documentation is a
concious decision, use the [py-generic-project](https://github.com/Springerle/py-generic-project)
template for more complex tools that aren't a good fit for this reduced project setup.

To distribute your tool as a Debian package, especially when it has outside dependencies
(i.e. a non-empty ``requirements.txt``), consider adding the
[dh-virtualenv](https://github.com/Springerle/dh-virtualenv-mold) template.


## Split Licensing

Since the files contained in the ``{{cookiecutter.repo_name}}`` archetype itself
will comprise the foundation of your project, they're unlicensed using the
“Creative Commons Zero v1.0 Universal” license.
All other files outside the ``{{cookiecutter.repo_name}}`` directory are
MIT-licensed – this effectively means you only have to attribute this project
if you re-use all or parts of the contained templating mechanics and documentation.

To make the confusion complete, the template as-is gives the created project an
Apache 2.0 license by default – you have to change the ``LICENSE`` file, ``setup.py``
and the script module to change that, after you materialized the template.

* [![Project License](http://img.shields.io/badge/license-MIT-red.svg)](https://github.com/Springerle/py-minimal-script/blob/master/LICENSE_MIT) for the project.
* [![Template License](http://img.shields.io/badge/license-CC0-blue.svg)](https://github.com/Springerle/py-minimal-script/blob/master/LICENSE_CC0) for the template proper (everything in `{{cookiecutter.repo_name}}`), unless specified otherwise within the file itself.
