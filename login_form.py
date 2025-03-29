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


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap("images/image_4.jpg")
        self.setWindowTitle('Running App')
        self.resize(325, 475)
        self.setMinimumSize(250, 300)

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.line_edit_username = self.add_input_field(
            layout, "Username", "Please enter your username", 0)
        self.line_edit_password = self.add_input_field(
            layout, "Password", "Please enter your password", 1, 
            is_password=True)

        self.add_button(layout, "Login", self.check_creds, 2)
        self.add_button(layout, "Sign Up", self.sign_up, 3)

        self.setLayout(layout)

    def add_input_field(
            self, layout, label_text, placeholder, row, is_password=False):
        label = QLabel(
            f'<font size="4" color="white"><b> {label_text} </b></font>')
        label.setObjectName(label_text)
        layout.addWidget(label, row, 0)

        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        line_edit.setStyleSheet("border-radius: 3px")
        line_edit.setObjectName(f"{label_text} Input")
        if is_password:
            line_edit.setEchoMode(QLineEdit.Password)
            line_edit.setMaxLength(8)
        layout.addWidget(line_edit, row, 1)

        return line_edit

    def add_button(self, layout, text, callback, row):
        button = QPushButton(text)
        button.clicked.connect(callback)
        button.setObjectName(text)
        button.setToolTip(f"Click to {text.lower()}")
        layout.addWidget(button, row, 0, 1, 2)
        layout.setRowMinimumHeight(row, 75)

    def check_creds(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        try:
            with open(credentials_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                if any(
                    row[0] == username and row[1] == password for row in reader
                ):
                    self.open_run_data_form()
                    self.close()
                    return
            self.show_message('Incorrect Username or Password')
        except FileNotFoundError:
            self.show_message('No users found. Please sign up first.')

    def sign_up(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        if not username or not password:
            self.show_message('Username and Password cannot be empty')
            return

        try:
            with open(credentials_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password])
            self.show_message('Sign Up Successful! You can now log in.')
        except Exception as e:
            self.show_message(f'An error occurred: {e}')

    def open_run_data_form(self):
        self.secondWindow = RunDataForm()
        self.secondWindow.show()

    def show_message(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.exec_()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    sys.exit(app.exec_())
