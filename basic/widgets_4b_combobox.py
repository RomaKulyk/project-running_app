import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItem("Choose metric")
        widget.addItem("Time")
        widget.addItem("Distance")
        widget.addItem("Temp")
        widget.setEditable(True)
        widget.setMaxCount(10)
        widget.setInsertPolicy(QComboBox.InsertPolicy
                               .InsertAlphabetically)
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        # Disable the "By Default" item
        index = widget.findText("By Default")
        widget.setItemData(index, 0, Qt.UserRole - 1)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)


# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QMainWindow
window = MainWindow()
window.show()

# To start up the event loop
app.exec_()
