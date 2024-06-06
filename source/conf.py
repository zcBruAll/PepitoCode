import sys
import os

# Ensure the path is correctly set to the directory where pepito_lexer.py is located
sys.path.insert(0, os.path.abspath('.'))

from pygments.lexers import get_lexer_by_name
from sphinx.highlighting import lexers
from pepito_lexer import PepitoCodeLexer

# -- Project information -----------------------------------------------------

project = 'PepitoCode'
copyright = '2024, Allan Brunner'
author = 'Allan Brunner'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

# Register the custom lexer
lexers['pepitoCode'] = PepitoCodeLexer()
