from PyQt5.QtWidgets import QApplication, QPushButton
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QPushButton
window = QPushButton("Push Me")
window.show()

# To start up the event loop
app.exec_()