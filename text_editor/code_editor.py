from PyQt6.QtWidgets import QPlainTextEdit, QTextEdit
from PyQt6.QtGui import QColor, QTextFormat

from text_editor.languages.code_highlight_python import PythonHighlighter


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        # Example placeholder text
        self.setPlainText("# Write your code here.\n")

        # Syntax
        self.highligher = PythonHighlighter(self)

        # Highlight current line
        self.cursorPositionChanged.connect(self.highlight_current_line)
        self.highlight_current_line()

    def highlight_current_line(self):
        # Initializing the extra selections.
        extra_selections = []

        #If the file isn't readonly...
        if not self.isReadOnly():
            #We make "selection" as an extra selection
            selection = QTextEdit.ExtraSelection()
            line_color = QColor("#2a2a2a")
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
            extra_selections.append(selection)
        self.setExtraSelections(extra_selections)