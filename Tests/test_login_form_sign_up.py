import unittest
from unittest.mock import patch, mock_open
from PyQt5.QtWidgets import QApplication
from login_form import LoginForm

class TestLoginFormSignUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication instance for the tests."""
        cls.app = QApplication([])

    def setUp(self):
        """Set up the LoginForm instance for each test."""
        self.form = LoginForm()

    @patch('login_form.QMessageBox')
    @patch('builtins.open', new_callable=mock_open)
    def test_sign_up_successful(self, mock_file, mock_messagebox):
        """Test sign_up with valid username and password."""
        self.form.line_edit_username.setText("newuser")
        self.form.line_edit_password.setText("newpass")

        self.form.sign_up()

        mock_file.assert_called_once_with(
            'user_credentials.csv', mode='a', newline='')
        mock_messagebox.return_value.setText.assert_called_once_with(
            'Sign Up Successful! You can now log in.')
        mock_messagebox.return_value.exec_.assert_called_once()

    @patch('login_form.QMessageBox')
    def test_sign_up_empty_fields(self, mock_messagebox):
        """Test sign_up with empty username and password."""
        self.form.line_edit_username.setText("")
        self.form.line_edit_password.setText("")

        self.form.sign_up()

        mock_messagebox.return_value.setText.assert_called_once_with(
            'Username and Password cannot be empty')
        mock_messagebox.return_value.exec_.assert_called_once()

    @patch('login_form.QMessageBox')
    @patch('builtins.open', side_effect=Exception("File write error"))
    def test_sign_up_file_write_error(self, mock_file, mock_messagebox):
        """Test sign_up when file write operation fails."""
        self.form.line_edit_username.setText("newuser")
        self.form.line_edit_password.setText("newpass")

        self.form.sign_up()

        mock_messagebox.return_value.setText.assert_called_once_with(
            'An error occurred: File write error')
        mock_messagebox.return_value.exec_.assert_called_once()

if __name__ == '__main__':
    unittest.main()