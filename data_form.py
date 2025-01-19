import sys
import time
import datetime
from datetime import date
import csv
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,)
from PyQt5.QtGui import QPixmap, QPainter


today = str(date.today())


# Subclass QWidget to customize your application's main widget
class RunDataForm(QWidget):
    """
    init
        This is an inizialization method
    get_week_number
        This method allows to get week's number
    input_data
        This method input data to the output.csv file in the following format:
        week number, distance and time
    calculate_average_temp_for_week
        This method allows to calculate an average temp for certain week
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

        label_distance = QLabel('<font size="4"> Distance </font>')
        self.lineEdit_distance = QLineEdit()
        self.lineEdit_distance.setPlaceholderText(
            'Please enter distance: KK:MMM')
        layout.addWidget(label_distance, 0, 0)
        layout.addWidget(self.lineEdit_distance, 0, 1)

        label_time = QLabel('<font size="4"> Time </font>')
        self.lineEdit_time = QLineEdit()
        self.lineEdit_time.setPlaceholderText('Please enter time: HH:MM:SS')
        # Set the maximum number of characters which can be entered to 8
        self.lineEdit_time.setMaxLength(8)

        layout.addWidget(label_time, 1, 0)
        layout.addWidget(self.lineEdit_time, 1, 1)

        button_upload = QPushButton('Input Data')
        button_upload.clicked.connect(self.input_data)
        layout.addWidget(button_upload, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def get_week_number(self):
        """This method allows to get week's number"""
        today = datetime.date.today()
        return today.isocalendar()[1]

    def input_data(self):
        """
        This method input data to the output.csv file in the following format:
        week number, distance and time
        """
        week_number = str(self.get_week_number())

        input_file = 'running_data.csv'
        new_row = [week_number, today, self.lineEdit_distance.text(),
                   self.lineEdit_time.text()]

        try:
            # Open the input file in read mode to determine
            # the current maximum unique ID
            with open(input_file, mode='r', newline='') as infile:
                reader = csv.reader(infile, delimiter='\t')
                try:
                    header = next(reader)  # Read the header
                except StopIteration:
                    header = []  # Handle case where file is empty

                max_id = 0
                for row in reader:
                    if row:
                        try:
                            max_id = max(max_id, int(row[0]))
                        except ValueError:
                            print("The first column is not a valid integer.\
                                Make sure the CSV file is properly formatted.")

            new_unique_id = max_id + 1

            # Open the input file in append mode to add the new row
            with open(input_file, mode='a', newline='') as outfile:
                writer = csv.writer(outfile, delimiter='\t')
                # If the file was empty, write the header first
                if not header:
                    # Replace with your actual header names
                    header = ['id', 'week', 'date', 'distance', 'time']
                    writer.writerow(header)
                # Insert the unique ID at the beginning of the row
                new_row.insert(0, new_unique_id)
                writer.writerow(new_row)

            print("New row with unique ID has been added successfully!")
        except FileNotFoundError:
            print("The file wasn't found. Please check file path and name.")
        except Exception as e:
            print(f"An error occurred: {e}")

        self.lineEdit_distance.clear()
        self.lineEdit_time.clear()

    def calculate_average_temp_for_week(self):
        """This method allows to calculate an average temp for certain week"""
        pass

    def paintEvent(self, event):
        """Override the paintEvent to handle custom painting for the widget"""
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
