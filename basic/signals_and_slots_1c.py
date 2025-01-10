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
        
        # Set the default value for variable
        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toogled)

        # Use the default value to set the initial state of the widget
        button.setChecked(self.button_is_checked)

        # Set the central widget of the Window
        self.setCentralWidget(button)

    def the_button_was_toogled(self, is_checked):
        # When the widget state changes, update the variable to match.
        self.button_is_checked = is_checked

        print(self.button_is_checked)

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()
