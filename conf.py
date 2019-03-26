

import sys
import os
import shlex	

this_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, this_path + './resources/')
import simple_lexer

# Pygments (syntax highlighting) style to use
pygments_style = 'sphinx'
highlight_language = 'simple'
	
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Simple Modules'
copyright = u'2018-2019, Azeez Adewale and the Simple community (MIT)'
author = u'Azeez Adewale'

version = '0.2'
release = 'latest'

language = 'en'

exclude_patterns = ['build']

html_theme = "nature" 
html_sidebars = { '**': ['localtoc.html', 'globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }
html_theme_options = {
		#"relbarbgcolor": "red",
		#'rightsidebar': True
}

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "simple-lang", # Username
    "github_repo": "simple-docs", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/", # Path in the checkout to the docs root
}

#html_logo = 'img/docs_logo.png'

# Output file base name for HTML help builder
htmlhelp_basename = 'Simpledoc'

# Enable directives that insert the contents of external files
file_insertion_enabled = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'Simple.tex', 'Simple Documentation',
   'Azeez Adewale and the Simple community', 'manual'),
]

# -- Options for linkcheck builder ----------------------------------------

# disable checking urls with about.html#this_part_of_page anchors
linkcheck_anchors = False

linkcheck_timeout = 10

