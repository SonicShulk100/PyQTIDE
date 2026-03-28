import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from text_editor.code_editor import CodeEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt IDE - IDE made in Python")
        self.setGeometry(0, 0, 500, 500)

        self.editor = CodeEditor()
        self.setCentralWidget(self.editor)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()