import unittest
from PyQt5.QtWidgets import QApplication
from data_form import RunDataForm

class TestRunDataFormInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication instance for the tests."""
        cls.app = QApplication([])

    def setUp(self):
        """Set up the RunDataForm instance for each test."""
        self.form = RunDataForm()

    def test_window_title(self):
        """Test if the window title is set correctly."""
        self.assertEqual(self.form.windowTitle(), 'Running App')

    def test_window_size(self):
        """Test if the window size is set correctly."""
        self.assertEqual(self.form.size().width(), 360)
        self.assertEqual(self.form.size().height(), 475)

    def test_minimum_size(self):
        """Test if the minimum size is set correctly."""
        self.assertEqual(self.form.minimumWidth(), 250)
        self.assertEqual(self.form.minimumHeight(), 300)

    def test_image_loaded(self):
        """Test if the image is loaded correctly."""
        self.assertFalse(self.form.image.isNull())

    def test_line_edit_distance_placeholder(self):
        """Test if the distance input placeholder is set correctly."""
        self.assertEqual(self.form.line_edit_distance.placeholderText(), 'Please enter distance: KM:MM')

    def test_line_edit_time_placeholder(self):
        """Test if the time input placeholder is set correctly."""
        self.assertEqual(self.form.line_edit_time.placeholderText(), 'Please enter time: HH:MM:SS')

    def test_text_edit_placeholder(self):
        """Test if the text edit placeholder is set correctly."""
        expected_placeholder = (
            "You will see your results here SOON!\n"
            "period type, period value\nrun, 2025-02-28\nweek, 7\n"
            "month, 2025-02\nyear, 2025"
        )
        self.assertEqual(self.form.text_edit.placeholderText(), expected_placeholder)

if __name__ == '__main__':
    unittest.main()