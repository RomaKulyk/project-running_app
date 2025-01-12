from PyQt5.QtWidgets import QApplication, QWidget
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of a QWidget
window = QWidget()
window.show()

# To start up the event loop
app.exec_()
