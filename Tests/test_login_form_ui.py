import unittest
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
from login_form import LoginForm

class TestLoginFormUI(unittest.TestCase):
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
        signup_button = self.form.findChild(QPushButton, "Sign Up")
        self.assertIsNotNone(signup_button)
        self.assertEqual(signup_button.text(), 'Sign Up')
        self.assertEqual(signup_button.toolTip(), "Click to sign up")

if __name__ == '__main__':
    unittest.main()