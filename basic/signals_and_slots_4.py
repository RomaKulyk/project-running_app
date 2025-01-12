from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        # To connect the input to the label, both must be defined
        self.input.textChanged.connect(self.label.setText)

        # Adds to widgets to a layout, and sets that on wndow
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window
        self.setCentralWidget(container)


# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()
