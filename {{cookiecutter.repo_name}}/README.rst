{{ cookiecutter.project_name }}
===============================

.. image:: https://pypip.in/v/{{ cookiecutter.repo_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png
   :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Latest Travis CI build status

{{ cookiecutter.short_description }}.

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
