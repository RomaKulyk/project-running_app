from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def show():
    print(line.text())

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("RunningApp")
 
line = QtWidgets.QLineEdit(win)
line.setEchoMode(QtWidgets.QLineEdit.Password)
line.move(100,80)
 
button = QtWidgets.QPushButton(win)
button.setText("Submit")
button.clicked.connect(show)
button.move(100,150)
 
button = QtWidgets.QPushButton(win)
button.setText("Clear")
button.clicked.connect(line.clear)
button.move(100,220)
 
win.show()
sys.exit(app.exec_())