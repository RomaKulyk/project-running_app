import sys
import time
import datetime
from datetime import date, timedelta
import csv
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,)
from PyQt5.QtGui import QPixmap, QPainter


today = str(date.today())
input_file = 'running_data.csv'

# Subclass QWidget to customize your application's main widget
class RunDataForm(QWidget):
    """
    init
        This is an inizialization method

    get_week_number
        This method allows to get week's number

    input_data
        This method input data to the input_file in the following format:
        week number, distance and time

    calculate_metrics
        This method calculates total time, total distance, and average pace for
        a given period (week, month, year) or a specific run
    """

    def __init__(self):
        super().__init__()
        # Load image
        self.image = QPixmap("image_2.png")
        # Set window title
        self.setWindowTitle('Running App')
        # Set window sizes
        self.resize(325, 475)
        self.setMinimumHeight(300)
        self.setMinimumWidth(250)

        layout = QGridLayout()

        label_distance = QLabel('<font size="4"> Distance </font>')
        self.lineEdit_distance = QLineEdit()
        self.lineEdit_distance.setPlaceholderText(
            'Please enter distance: KM:MM')
        # Set the maximum number of characters which can be entered to 5
        self.lineEdit_distance.setMaxLength(5)
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

        button_upload = QPushButton('Calculate total time')
        button_upload.clicked.connect(self.input_data)
        layout.addWidget(button_upload, 3, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
         
        button_upload = QPushButton('Calculate total distance')
        button_upload.clicked.connect(self.input_data)
        layout.addWidget(button_upload, 4, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        button_upload = QPushButton('Calculate averate temp')
        button_upload.clicked.connect(self.input_data)
        layout.addWidget(button_upload, 5, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def get_week_number(self):
        """This method allows to get week's number"""
        today = datetime.date.today()
        return today.isocalendar()[1]

    def input_data(self):
        """
        This method input data to the inpute_file in the following format:
        week number, distance and time
        """
        week_number = str(self.get_week_number())
        
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
            
def calculate_metrics(period_type, period_value, input_file, run_id=None):
    """Calculate total time, total distance, and average pace for
    a given period (week, month, year) or a specific run."""
    
    total_time = timedelta()
    total_distance = 0.0
    
    with open(input_file, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            date_str = row['date']
            date_parts = date_str.split('-')
            row_year = int(date_parts[0])
            row_month = int(date_parts[1])
            row_week = int(row['week']) if 'week' in row else None
            row_id = int(row['id'])
            
            distance = float(row['distance'])
            time_str = row['time']
            h, m, s = map(int, time_str.split(':'))
            duration = timedelta(hours=h, minutes=m, seconds=s)
            
            if run_id and row_id == run_id:
                total_time = duration
                total_distance = distance
                break
            elif period_type == 'week' and row_week == period_value:
                total_time += duration
                total_distance += distance
            elif period_type == 'month' and row_year == period_value[0] and row_month == period_value[1]:
                total_time += duration
                total_distance += distance
            elif period_type == 'year' and row_year == period_value:
                total_time += duration
                total_distance += distance
    
    average_pace = total_time / total_distance if total_distance > 0 else timedelta()
    
    total_seconds = int(average_pace.total_seconds())
    pace_minutes, pace_seconds = divmod(total_seconds, 60)
    
    if run_id:
        period_type = 'run ID'
        period_value = run_id
    
    print(f"Total time for {period_type} {period_value}: {str(total_time)}")
    print(f"Total distance for {period_type} {period_value}: {total_distance:.2f} units")
    print(f"Average pace for {period_type} {period_value}: {pace_minutes:02}:{pace_seconds:02} per unit distance")

    def paintEvent(self, event):
        """Override the paintEvent to handle custom painting for the widget"""
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def print_the_whole_file():
        with open(input_file, mode='r', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            data_list = []
            for row in reader:
                data_list.append(row)
        for row in data_list:
            print(row)
    # print_the_whole_file()

        # Usage examples
calculate_metrics('week', 4, 'running_data.csv')
print(50*'=')
calculate_metrics('month', (2025, 1), 'running_data.csv')
print(50*'=')
calculate_metrics('year', 2025, 'running_data.csv')
print(50*'=')
calculate_metrics(None, None, 'running_data.csv', run_id=1)
print(50*'=')

