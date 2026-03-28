from PyQt6.QtGui import QSyntaxHighlighter, QColor, QFont, QTextCharFormat


class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.rules = []

        def format(color, bold=False, italic=False):
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(color))
            if bold:
                fmt.setFontWeight(QFont.Weight.Bold)
            if italic:
                fmt.setFontItalic(True)
            return fmt

        keyword_format = format("#569CD6", bold=True)
        string_format = format("#CE9178")
        comment_format = format("#6A9955", italic=True)
        number_format = format("#B5CEA8")
        function_format = format("#DCDCAA")

        keywords = [
            "and", "as", "assert", "break", "class", "continue", "def",
            "del", "elif", "else", "except", "False", "finally", "for",
            "from", "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise", "return",
            "True", "try", "while", "with", "yield"
        ]

        self.rules += [(rf"\b{kw}\b", keyword_format) for kw in keywords]

        self.rules += [
            (r'"[^"\\]*(\\.[^"\\]*)*"', string_format),
            (r"'[^'\\]*(\\.[^'\\]*)*'", string_format),
        ]

        self.rules.append((r"#.*", comment_format))