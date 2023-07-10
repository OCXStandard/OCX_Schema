# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

sys.path.insert(0, os.path.abspath(".././"))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_automodapi.automodapi',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinx.ext.graphviz',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'OCX_schema'
year = '2023'
author = '3Docx.org'
copyright = '{0}, {1}'.format(year, author)
version = '3.0.0'
release = 'alpha'


inheritance_graph_attrs = dict(rankdir="TB", size='""',
                               fontsize=14)
inheritance_node_attrs = dict(shape='ellipse', fontsize=14, height=1, width=2,
                              color='dodgerblue1', style='filled')


pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/OCXStandard/OCX_schema/issues/%s', '#'),
    'pr': ('https://github.com/OCXStandard/OCX_schema/pull/%s', 'PR #'),
}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'


html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
html_static_path = ["_static"]
napoleon_use_ivar = False
napoleon_use_rtype = False
napoleon_use_param = True

