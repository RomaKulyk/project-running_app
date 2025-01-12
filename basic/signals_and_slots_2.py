from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Keeps a reference to the button on self so it can accessible in slot
        self.button = QPushButton("Press Me")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        # Change the text of a button by passing a str to .setText()
        self.button.setText("You already clicked me.")
        # Disable a button call .setEnabled() with False
        self.button.setEnabled(False)


# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()
