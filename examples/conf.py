

import sys
import os
import shlex	

this_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, this_path)
	
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

project = u'Simple Examples'
copyright = u'2018-2019, Azeez Adewale and the Simple community (MIT)'
author = u'Azeez Adewale'

version = '0.1'
release = '0.1'
	

import simple_lexer

html_theme = "nature" 
