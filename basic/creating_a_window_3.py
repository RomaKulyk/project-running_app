from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QPushButton
window = QMainWindow()
window.show()

# To start up the event loop
app.exec_()