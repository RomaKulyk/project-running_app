from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

import sys
from random import choice


# select window's title from list using random.choice()
window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on Earth",
    "What on Earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        # Keeps a reference to the button on self so it can accessible in slot
        self.button = QPushButton("Press Me")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Hook up the_window_title_was_changed method to
        # the windows .windowTitleChanged signal
        self.windowTitleChanged.connect(
            self.the_window_title_was_changed)

        # Set the central widget of the Window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        # Sets the new window title to the new title
        self.setWindowTitle(new_window_title)

    def the_window_title_was_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        # If new window title equals to "Something went wrong"
        # disable the button.
        if window_title == "Something went wrong":
            self.button.setDisabled(True)


# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()
