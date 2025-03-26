import unittest
from PyQt5.QtWidgets import QApplication
from login_form import LoginForm
from unittest.mock import patch, mock_open
from PyQt5.QtWidgets import (QApplication,
                             QPushButton,
                             QLabel,
                             QLineEdit)
                             
class TestLoginForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication instance for the tests."""
        cls.app = QApplication([])

    def setUp(self):
        """Set up the LoginForm instance for each test."""
        self.form = LoginForm()

    def test_window_initialization(self):
        """Test the initialization of the LoginForm window."""
        self.assertEqual(self.form.windowTitle(), 'Running App')
        self.assertEqual(self.form.minimumWidth(), 250)
        self.assertEqual(self.form.minimumHeight(), 300)
        self.assertEqual(self.form.size().width(), 325)
        self.assertEqual(self.form.size().height(), 475)

    def test_username_label(self):
        """Test the username label properties."""
        username_label = self.form.findChild(QLabel, "Username")
        self.assertIsNotNone(username_label)
        self.assertEqual(username_label.text(), 
            '<font size="4" color="white"><b> Username </b></font>')

    def test_password_label(self):
        """Test the password label properties."""
        password_label = self.form.findChild(QLabel, "Password")
        self.assertIsNotNone(password_label)
        self.assertEqual(password_label.text(), 
            '<font size="4" color="white"><b> Password </b></font>')

    def test_username_input(self):
        """Test the username input field properties."""
        username_input = self.form.findChild(QLineEdit, "Username Input")
        self.assertIsNotNone(username_input)
        self.assertEqual(username_input.placeholderText(), 
            'Please enter your username')
        self.assertEqual(username_input.styleSheet(), "border-radius: 3px")

    def test_password_input(self):
        """Test the password input field properties."""
        password_input = self.form.findChild(QLineEdit, "Password Input")
        self.assertIsNotNone(password_input)
        self.assertEqual(password_input.placeholderText(), 
            'Please enter your password')
        self.assertEqual(password_input.echoMode(), QLineEdit.Password)
        self.assertEqual(password_input.maxLength(), 8)
        self.assertEqual(password_input.styleSheet(), "border-radius: 3px")

    def test_login_button(self):
        """Test the login button properties."""
        login_button = self.form.findChild(QPushButton, "Login")
        self.assertIsNotNone(login_button)
        self.assertEqual(login_button.text(), 'Login')
        self.assertEqual(login_button.toolTip(), "Click to login")

    def test_signup_button(self):
        """Test the sign-up button properties."""
        signup_button = self.form.findChild(QPushButton, "Sign up")
        self.assertIsNotNone(signup_button)
        self.assertEqual(signup_button.text(), 'Sign Up')
        self.assertEqual(signup_button.toolTip(), "Click to sign up")

    @patch('login_form.QMessageBox')
    @patch('builtins.open', new_callable=mock_open, read_data="testuser,testpass\n")
    def test_check_creds_valid_credentials(self, mock_file, mock_messagebox):
        """Test check_creds with valid credentials."""
        self.form.line_edit_username.setText("testuser")
        self.form.line_edit_password.setText("testpass")

        with patch.object(self.form, 'open_run_data_form') as mock_open_run_data_form:
            self.form.check_creds()
            mock_open_run_data_form.assert_called_once()
            self.assertTrue(self.form.isHidden())  # Ensure the form is closed

    @patch('login_form.QMessageBox')
    @patch('builtins.open', new_callable=mock_open, read_data="testuser,testpass\n")
    def test_check_creds_invalid_credentials(self, mock_file, mock_messagebox):
        """Test check_creds with invalid credentials."""
        self.form.line_edit_username.setText("wronguser")
        self.form.line_edit_password.setText("wrongpass")

        self.form.check_creds()
        mock_messagebox.return_value.setText.assert_called_once_with('Incorrect Username or Password')
        mock_messagebox.return_value.exec_.assert_called_once()

    @patch('login_form.QMessageBox')
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_check_creds_file_not_found(self, mock_file, mock_messagebox):
        """Test check_creds when credentials file is not found."""
        self.form.line_edit_username.setText("testuser")
        self.form.line_edit_password.setText("testpass")

        self.form.check_creds()
        mock_messagebox.return_value.setText.assert_called_once_with('No users found. Please sign up first.')
        mock_messagebox.return_value.exec_.assert_called_once()

if __name__ == '__main__':
    unittest.main()