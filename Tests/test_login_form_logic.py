import unittest
from unittest.mock import patch, mock_open
from PyQt5.QtWidgets import QApplication
from login_form import LoginForm

class TestLoginFormLogic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication instance for the tests."""
        cls.app = QApplication([])

    def setUp(self):
        """Set up the LoginForm instance for each test."""
        self.form = LoginForm()

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