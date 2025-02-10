from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAD Request Submission")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the CAD Request GUI"))
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    print("Hello World")
