# importing required libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QMainWindow):

	# constructor
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# width of window
		self.w_width = 400

		# height of window
		self.w_height = 500

		# setting geometry
		self.setGeometry(100, 100, self.w_width, self.w_height)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for adding components
	def UiComponents(self):
		# creating head label
		head = QLabel("Run Calculator", self)

		# setting geometry to the head
		head.setGeometry(0, 10, 400, 60)

		# font
		font = QFont('Times', 15)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		# setting font to the head
		head.setFont(font)

		# setting alignment of the head
		head.setAlignment(Qt.AlignCenter)

		# setting color effect to the head
		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.darkCyan)
		head.setGraphicsEffect(color)

		# creating a interest label
		i_label = QLabel("Distance", self)

		# setting properties to the interest label
		i_label.setAlignment(Qt.AlignCenter)
		i_label.setGeometry(20, 100, 170, 40)
		i_label.setStyleSheet("QLabel"
							"{"
							"border : 2px solid black;"
							"background : rgba(70, 70, 70, 35);"
							"}")
		i_label.setFont(QFont('Times', 9))

		# creating a QLineEdit object to get the interest
		self.rate = QLineEdit(self)

		# setting properties to the rate line edit
		self.rate.setGeometry(200, 100, 180, 40)
		self.rate.setAlignment(Qt.AlignCenter)
		self.rate.setFont(QFont('Times', 9))


		# creating a number of years label
		n_label = QLabel("Time ", self)

		# setting properties to the years label
		n_label.setAlignment(Qt.AlignCenter)
		n_label.setGeometry(20, 150, 170, 40)
		n_label.setStyleSheet("QLabel"
							"{"
							"border : 2px solid black;"
							"background : rgba(70, 70, 70, 35);"
							"}")
		n_label.setFont(QFont('Times', 9))

		# creating a QLineEdit object to get the years
		self.years = QLineEdit(self)

		# setting properties to the rate line edit
		self.years.setGeometry(200, 150, 180, 40)
		self.years.setAlignment(Qt.AlignCenter)
		self.years.setFont(QFont('Times', 9))

		# creating a loan amount label
		a_label = QLabel("Temp", self)

		# setting properties to the amount label
		a_label.setAlignment(Qt.AlignCenter)
		a_label.setGeometry(20, 200, 170, 40)
		a_label.setStyleSheet("QLabel"
							"{"
							"border : 2px solid black;"
							"background : rgba(70, 70, 70, 35);"
							"}")
		a_label.setFont(QFont('Times', 9))

		# creating a QLineEdit object to get the amount
		self.amount = QLineEdit(self)

		# setting properties to the rate line edit
		self.amount.setGeometry(200, 200, 180, 40)
		self.amount.setAlignment(Qt.AlignCenter)
		self.amount.setFont(QFont('Times', 9))


		# creating a push button
		calculate = QPushButton("Download data", self)

		# setting geometry to the push button
		calculate.setGeometry(125, 270, 150, 40)

App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
