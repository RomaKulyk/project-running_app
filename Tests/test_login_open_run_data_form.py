import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication
from login_form import LoginForm
from data_form import RunDataForm

class TestLoginFormOpenRunDataForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication instance for the tests."""
        cls.app = QApplication([])

    def setUp(self):
        """Set up the LoginForm instance for each test."""
        self.form = LoginForm()

    @patch('login_form.RunDataForm')
    def test_open_run_data_form(self, mock_run_data_form):
        """Test open_run_data_form opens the RunDataForm window."""
        self.form.open_run_data_form()

        # Assert that RunDataForm was instantiated
        mock_run_data_form.assert_called_once()

        # Assert that the show method of RunDataForm was called
        mock_run_data_form.return_value.show.assert_called_once()

if __name__ == '__main__':
    unittest.main()