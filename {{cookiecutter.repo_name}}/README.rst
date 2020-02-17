{{ cookiecutter.project_name }}
===============================

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Latest Version|  |Downloads|

{{ cookiecutter.short_description }}.

.. contents:: **Contents**


.. _setup-start:

:Code:          {{ cookiecutter.github_url }}#readme
:Docs:          https://{{ cookiecutter.repo_name }}.readthedocs.io/
:CI:            https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
:Issues:        {{ cookiecutter.github_url }}/issues


Introduction
------------

**TODO**


Usage
-----

**TODO**


Installation
------------

*{{ cookiecutter.project_name }}* can be installed via
``python3 -m pip install --user {{ cookiecutter.repo_name }}`` as usual,
see `releases`_ for an overview of available versions.

If you prefer an **isolated and easily removable venv installation**,
consider using `dephell jail install {{ cookiecutter.repo_name }}`_ instead.

To get a **bleeding-edge version from source**, use these commands
(ideally within an activated virtualenv):

.. code:: sh

    repo="{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

As a developer, to **create a working directory for this project**, call these commands:

.. code:: sh

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    command . .env --yes --develop  # add '--virtualenv /usr/bin/virtualenv' for Python2
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


.. _releases: {{ cookiecutter.github_url }}/releases
.. _`dephell jail install {{ cookiecutter.repo_name }}`: https://dephell.readthedocs.io/cmd-jail-install.html

.. |Travis CI| image:: https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |Coveralls| image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |GitHub Issues| image:: https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: {{ cookiecutter.github_url }}/issues
.. |License| image:: https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg
    :target: {{ cookiecutter.github_url }}/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/{{ cookiecutter.repo_name }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Latest Version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Download format| image:: https://pypip.in/format/{{ cookiecutter.repo_name }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Downloads| image:: https://img.shields.io/pypi/dw/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
