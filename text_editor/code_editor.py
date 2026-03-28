from PyQt6.QtWidgets import QPlainTextEdit, QTextEdit
from PyQt6.QtGui import QColor, QTextFormat


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        # Example placeholder text
        self.setPlainText("# Welcome to your PyQt IDE\n")

        # Highlight current line
        self.cursorPositionChanged.connect(self.highlight_current_line)
        self.highlight_current_line()

    def highlight_current_line(self):
        extra_selections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor("#2a2a2a")
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
            extra_selections.append(selection)
        self.setExtraSelections(extra_selections)