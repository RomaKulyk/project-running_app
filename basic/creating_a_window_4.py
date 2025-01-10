import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QPushButton,
                             )

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me")
        
        # Set the central widget of the Window
        self.setCentralWidget(button)

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()