{{ cookiecutter.project_name }}
===============================

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Development Status|  |Latest Version|  |Download format|  |Downloads|


{{ cookiecutter.short_description }}.

.. contents:: **Contents**

.. _setup-start:

Introduction
------------

Usage
-----

Installation
------------

*{{ cookiecutter.project_name }}* can be installed via ``pip install {{ cookiecutter.repo_name }}`` as usual,
see `releases <{{ cookiecutter.github_url }}/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

As a developer, to create a working directory for this project, call these commands::

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    . .env --yes --develop
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.org/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


.. |Travis CI| image:: https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |Coveralls| image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |GitHub Issues| image:: https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: {{ cookiecutter.github_url }}/issues
.. |License| image:: https://img.shields.io/pypi/l/{{ cookiecutter.repos_name }}.svg
    :target: {{ cookiecutter.github_url }}/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/{{ cookiecutter.repo_name }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Latest Version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Download format| image:: https://pypip.in/format/{{ cookiecutter.repo_name }}/badge.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
.. |Downloads| image:: https://img.shields.io/pypi/dw/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
