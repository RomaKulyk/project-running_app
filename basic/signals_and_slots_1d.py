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

        # Keeps a reference to the button on self so it can accessible in slot   
        self.button = QPushButton("Press Me")
        self.button.setCheckable(True)
        self.button.released.connect(
            # The released signal fires when the button is realeased, but does
            # not send the check state
            self.the_button_was_released
        )
        self.button.setChecked(self.button_is_checked)

        # Set the central widget of the Window
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        # .isChecked() returns the check state of the button
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()
