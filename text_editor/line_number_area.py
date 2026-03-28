from PyQt6.QtWidgets import QWidget

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        return self.code_editor.line_number_area_size()

    def paintEvent(self, event):
        self.code_editor.line_number_area_paint_event(event)