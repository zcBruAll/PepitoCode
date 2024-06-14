import sys
import os

# Ensure the path is correctly set to the directory where your custom theme is located
sys.path.insert(0, os.path.abspath('_themes'))

from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Keyword, Name, String, Number, Operator, Punctuation
from sphinx.highlighting import lexers

class PepitoCodeLexer(RegexLexer):
    name = 'PepitoCode'
    aliases = ['pepitoCode']
    filenames = ['*.pc']
    
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'#.*', Comment.Single),
            (r'\b(Int|Float|Double|Boolean|String|Char|List|Vector|Matrix|Complex|Function)\b', Keyword.Type),
            (r'\b(true|false)\b', Keyword.Constant),
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'(\\\\|\\'|[^'])*'", String.Char),
            (r'\b\d+\b', Number.Integer),
            (r'\b\d+\.\d+\b', Number.Float),  # Matches floating point numbers
            (r'(\d+)\+(\d+)i', Number),  # Matches complex numbers like 0+0i
            (r'\b[A-Za-z_][A-Za-z0-9_]*<\s*[A-Za-z_][A-Za-z0-9_]*\s*>\b', Name.Class),  # Matches generic types like List<T>
            (r'(\+|-|\*|/|\^|=)', Operator),
            (r'[{}()\[\],.;]', Punctuation),
            (r'\b(if|else|for|while|return|try|catch)\b', Keyword.Reserved),
            (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),
        ],
    }

# Register the custom lexer
lexers['pepitoCode'] = PepitoCodeLexer()

# -- Project information -----------------------------------------------------

project = 'PepitoCode'
copyright = '2024, Allan Brunner'
author = 'Allan Brunner'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_themes']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinxawesome_theme'  # Ensure this matches the theme directory name within _themes
#html_static_path = ['_static']
