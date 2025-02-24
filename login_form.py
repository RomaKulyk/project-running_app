import sys
import csv
from data_form import RunDataForm
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,
                             QMessageBox)
from PyQt5.QtGui import QPixmap, QPainter

credentials_file = 'user_credentials.csv'

# Subclass QWidget to customize your application's main widget
class LoginForm(QWidget):
    """
    init
        This is an initialization method
    check_creds
        This is a method to check if user has a permission to use app
    open_run_data_form
        This is a method which opens another window after authorization
    paint_event
        Override the paintEvent to handle custom painting for the widget
    sign_up
        This is a method to sign up a new user
    """
    def __init__(self):
        super().__init__()
        # Load image
        self.image = QPixmap("image_4.jpg")
        # Set window title
        self.setWindowTitle('Running App')
        # Set window sizes
        self.resize(325, 475)
        self.setMinimumHeight(300)
        self.setMinimumWidth(250)

        layout = QGridLayout()

        label_name = QLabel(
            '<font size="4" color="white"><b> Username </b></font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        # Apply stylesheet for rounded corners
        self.lineEdit_username.setStyleSheet("border-radius: 3px")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel(
            '<font size="4" color="white"><b> Password </b></font>')
        self.line_edit_password = QLineEdit()
        self.line_edit_password.setPlaceholderText('Please enter your password')
        # Hide the characters entered by user
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        # Set the maximum number of characters which can be entered to 8
        self.line_edit_password.setMaxLength(8)
        # Apply stylesheet for rounded corners
        self.line_edit_password.setStyleSheet("border-radius: 3px")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.line_edit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_creds)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        button_signup = QPushButton('Sign Up')
        button_signup.clicked.connect(self.sign_up)
        layout.addWidget(button_signup, 3, 0, 1, 2)
        layout.setRowMinimumHeight(3, 75)

        self.setLayout(layout)

    def check_creds(self):
        """This is a method to check if user has a permission to use app"""
        msg = QMessageBox()
        username = self.lineEdit_username.text()
        password = self.line_edit_password.text()

        try:
            with open(credentials_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[1] == password:
                        self.open_run_data_form()
                        self.close()
                        return
            msg.setText('Incorrect Username or Password')
            msg.exec_()
        except FileNotFoundError:
            msg.setText('No users found. Please sign up first.')
            msg.exec_()

    def sign_up(self):
        """This is a method to sign up a new user"""
        msg = QMessageBox()
        username = self.lineEdit_username.text()
        password = self.line_edit_password.text()

        if not username or not password:
            msg.setText('Username and Password cannot be empty')
            msg.exec_()
            return

        try:
            with open(credentials_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password])
            msg.setText('Sign Up Successful! You can now log in.')
            msg.exec_()
        except Exception as e:
            msg.setText(f'An error occurred: {e}')
            msg.exec_()

    def open_run_data_form(self):
        """This is a method which opens another window after authorization"""
        self.secondWindow = RunDataForm()
        self.secondWindow.show()

    def paintEvent(self, event):
        """Override the paintEvent to handle custom painting for the widget"""
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)


if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of a QLoginForm
    form = LoginForm()
    form.show()

    # To start up the event loop
    sys.exit(app.exec_())
