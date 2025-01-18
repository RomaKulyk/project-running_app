import sys
from data_form import RunDataForm
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,
                             QMessageBox)
from PyQt5.QtGui import QPixmap, QPainter


# Subclass QWidget to customize your application's main widget
class LoginForm(QWidget):
    """
    init
        This is an inizialization method
    check_creds
        This is a method to check if user has a permission to use app
    open_run_data_form
        This is a method which opens another window after authorisation
    """
    def __init__(self):
        super().__init__()
        # Load image 
        self.image = QPixmap("running_man.jpg")
        # Set window title
        self.setWindowTitle('Running App')
        # Set window sizes
        self.resize(350, 500)
        self.setMinimumHeight(300)
        self.setMinimumWidth(250)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        # Hide the characters entered by user
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        # Set the maximum number of characters which can be entered to 8
        self.lineEdit_password.setMaxLength(8)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_creds)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_creds(self):
        """This is a method to check if user has a permission to use app"""
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'R2D2'\
        and self.lineEdit_password.text() == '1234':
            # It opens the second app's window if password and login is correct
            self.open_run_data_form()
            # It closes login window
            self.close()

        else:
            msg.setText('Incorrect Password')
            msg.exec_()

    def open_run_data_form(self):
        """This is a method which opens another window after authorisation"""
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
