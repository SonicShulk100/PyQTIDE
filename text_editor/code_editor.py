from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QColor, QTextFormat, QPainter
from PyQt6.QtWidgets import QPlainTextEdit, QTextEdit

from .line_number_area import LineNumberArea


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setPlainText("# Welcome to your PyQt IDE\n")

        # Line Number Area
        self.line_number_area = LineNumberArea(self)

        # Signals
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        # Init
        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def line_number_area_size(self):
        digits = len(str(max(1, self.blockCount())))
        space = 10 + self.fontMetrics().horizontalAdvance('9') * digits
        return self.viewport().rect().adjusted(0, 0, space, 0).size()

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_size().width(), 0, 0, 0)

    # 🔄 Sync scrolling
    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

    # 📐 Resize
    def resizeEvent(self, event):
        super().resizeEvent(event)

        cr = self.contentsRect()
        self.line_number_area.setGeometry(
            QRect(cr.left(), cr.top(),
                  self.line_number_area_size().width(), cr.height())
        )

    # 🎨 Draw numbers
    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor("#1e1e1e"))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)

                painter.setPen(QColor("#888888"))
                painter.drawText(
                    0,
                    top,
                    self.line_number_area.width() - 5,
                    self.fontMetrics().height(),
                    Qt.AlignmentFlag.AlignRight,
                    number
                )

            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            block_number += 1

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