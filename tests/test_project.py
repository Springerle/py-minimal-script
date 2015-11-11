# *- coding: utf-8 -*-
# pylint: disable=missing-docstring, bad-continuation
""" Test the template.
"""
# Copyright (c) 2015 Jürgen Hermann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import absolute_import, unicode_literals

import io
import os


def test_project_basedir_was_created(project):
    assert os.path.exists(project), "Project was created"
    assert os.path.isdir(project), "Project base directory was created"


def test_module_py_was_created(project):
    """Test the created project package source."""
    module_name = os.path.basename(project).replace('-', '_')
    module_py = '{0}/{1}.py'.format(project, module_name)

    assert os.path.isfile(module_py), "Script module was created"


def test_readme_has_github_url_and_newline_at_end(project):
    with io.open(project + '/README.rst', encoding='utf-8') as handle:
        readme = handle.read()

    # TODO: cookiecutter needs a --no-rc option, so we'll always get 'jschmoe'
    assert any("https://github.com/{}/new-script".format(i) in readme
        for i in ('jschmoe', 'jhermann')), "README contains repo URL"
    assert readme.endswith('\n'), "README has the newline at end of file"
