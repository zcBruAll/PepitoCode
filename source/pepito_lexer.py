from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Keyword, Name, String, Number, Operator, Punctuation

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
            (r'(\+|-|\*|/|\^|=)', Operator),
            (r'[{}()\[\],.;]', Punctuation),
            (r'\b(if|else|for|while|return|try|catch)\b', Keyword.Reserved),
            (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),
        ],
    }
