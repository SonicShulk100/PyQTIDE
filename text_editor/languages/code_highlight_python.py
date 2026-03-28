from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
import re


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

        # 🎯 Styles
        keyword_format = format("#569CD6", bold=True)
        string_format = format("#CE9178")
        comment_format = format("#6A9955", italic=True)
        number_format = format("#B5CEA8")
        function_format = format("#DCDCAA")

        # 🧠 Python keywords
        keywords = [
            "and", "as", "assert", "break", "class", "continue", "def",
            "del", "elif", "else", "except", "False", "finally", "for",
            "from", "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise", "return",
            "True", "try", "while", "with", "yield"
        ]

        # 📌 Rules
        self.rules += [(rf"\b{kw}\b", keyword_format) for kw in keywords]

        # Strings
        self.rules += [
            (r'"[^"\\]*(\\.[^"\\]*)*"', string_format),
            (r"'[^'\\]*(\\.[^'\\]*)*'", string_format),
        ]

        # Comments
        self.rules.append((r"#.*", comment_format))

        # Numbers
        self.rules.append((r"\b[0-9]+\b", number_format))

        # Function names
        self.rules.append((r"\bdef\s+([a-zA-Z_][a-zA-Z0-9_]*)", function_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            for match in re.finditer(pattern, text):
                if "def" in pattern:
                    # Highlight only function name group
                    start = match.start(1)
                    length = len(match.group(1))
                else:
                    start = match.start()
                    length = match.end() - match.start()

                self.setFormat(start, length, fmt)