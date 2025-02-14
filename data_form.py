import sys
import datetime
from datetime import date, timedelta
import csv
from PyQt5.QtWidgets import (QWidget, 
                             QPushButton, 
                             QLabel, 
                             QLineEdit, 
                             QGridLayout, 
                             QTextEdit, 
                             QApplication)
from PyQt5.QtGui import QPixmap, QPainter

today = str(date.today())
input_file = 'running_data.csv'

class RunDataForm(QWidget):
    """
    init
        This is an initialization method

    get_week_number
        This method allows to get week's number

    input_data
        This method input data to the input_file in the following format:
        week number, distance and time

    calculate_average_temp
        This method calculates average temp for a given period
        (week, month, year)
    
    calculate_total_time
        This method calculates total time for a given period
        (week, month, year)

    calculate_total_distance
        This method calculates total distance for a given period
        (week, month, year)
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

        text = "You will see your results here SOON!"
       
        layout = QGridLayout()

        label_distance = QLabel('<font size="4"> Distance </font>')
        self.lineEdit_distance = QLineEdit()
        self.lineEdit_distance.setPlaceholderText(
            'Please enter distance: KM:MM')
        self.lineEdit_distance.setMaxLength(5)
        layout.addWidget(label_distance, 0, 0)
        layout.addWidget(self.lineEdit_distance, 0, 1)

        label_time = QLabel('<font size="4"> Time </font>')
        self.lineEdit_time = QLineEdit()
        self.lineEdit_time.setPlaceholderText('Please enter time: HH:MM:SS')
        self.lineEdit_time.setMaxLength(8)
        layout.addWidget(label_time, 1, 0)
        layout.addWidget(self.lineEdit_time, 1, 1)

        button_upload = QPushButton('Input Data')
        button_upload.clicked.connect(self.input_data)
        layout.addWidget(button_upload, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        label_total_time = QLabel(
            '<font size="4"> Calculate total time </font>')
        self.lineEdit_total_time = QLineEdit()
        self.lineEdit_total_time.setPlaceholderText(
            'period type, period value')
        layout.addWidget(label_total_time, 3, 0)
        layout.addWidget(self.lineEdit_total_time, 3, 1)

        button_upload_tt = QPushButton('Calculate total time')
        button_upload_tt.clicked.connect(self.calculate_total_time_from_input)
        layout.addWidget(button_upload_tt, 3, 2, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        label_total_distance = QLabel(
            '<font size="4"> Calculate total distance </font>')
        self.lineEdit_total_distance = QLineEdit()
        self.lineEdit_total_distance.setPlaceholderText(
            'period type, period value')
        layout.addWidget(label_total_distance, 4, 0)
        layout.addWidget(self.lineEdit_total_distance, 4, 1)

        button_upload_td = QPushButton('Calculate total distance')
        button_upload_td.clicked.connect(
            self.calculate_total_distance_from_input)
        layout.addWidget(button_upload_td, 4, 2, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        label_average_temp = QLabel(
            '<font size="4"> Calculate average temp </font>')
        self.lineEdit_average_temp = QLineEdit()
        self.lineEdit_average_temp.setPlaceholderText(
            'period type, period value')
        layout.addWidget(label_average_temp, 5, 0)
        layout.addWidget(self.lineEdit_average_temp, 5, 1)

        button_upload_at = QPushButton(
            'Calculate average temp')
        button_upload_at.clicked.connect(
            self.calculate_average_temp_from_input)
        layout.addWidget(button_upload_at, 5, 2, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlainText(text)
        self.text_edit.setMaximumHeight(100)
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.text_edit.clear)
        
        layout.addWidget(self.text_edit, 6, 0, 1, 2)
        layout.addWidget(ok_button)

        self.setLayout(layout)
    
    def get_week_number(self):
        """This method allows to get week's number"""
        today = datetime.date.today()
        return today.isocalendar()[1]

    def input_data(self):
        """
        This method input data to the input_file in the following format:
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
                            print("The first column is not a valid integer." 
                                  "Make sure the CSV file is properly"
                                   " formatted.")

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

    def calculate_total_time_from_input(self):
        """Extracts data from lineEdit_total_time and calls 
           calculate_total_time"""
        input_text = self.lineEdit_total_time.text()
        try:
            period_type, period_value = input_text.split(',')
            period_type = period_type.strip()
            if period_type == 'month':
                period_value = tuple(map(int, period_value.strip().split('-')))
            else:
                period_value = int(period_value.strip())
            self.calculate_total_time(period_type, period_value)
        except ValueError:
            self.text_edit.setPlainText("Invalid input format."
                                " Please enter 'period type, period value'.")
    
    def calculate_total_distance_from_input(self):
        """Extracts data from lineEdit_total_distance and calls 
        calculate_total_distance"""
        input_text = self.lineEdit_total_distance.text()
        try:
            period_type, period_value = input_text.split(',')
            period_type = period_type.strip()
            if period_type == 'month':
                period_value = tuple(map(int, period_value.strip().split('-')))
            else:
                period_value = int(period_value.strip())
            self.calculate_total_distance(period_type, period_value)
        except ValueError:
            self.text_edit.setPlainText("Invalid input format."
                                " Please enter 'period type, period value'.")

    def calculate_average_temp_from_input(self):
        """Extracts data from lineEdit_average_temp and calls
        calculate_average_temp"""
        input_text = self.lineEdit_average_temp.text()
        try:
            period_type, period_value = input_text.split(',')
            period_type = period_type.strip()
            if period_type == 'month':
                period_value = tuple(map(int, period_value.strip().split('-')))
            else:
                period_value = int(period_value.strip())
            self.calculate_average_temp(period_type, period_value)
        except ValueError:
            self.text_edit.setPlainText("Invalid input format."
                                " Please enter 'period type, period value'.")


    def calculate_total_time(self, period_type, period_value):
        """This method calculates total time for a given period 
           (week, month, year)"""
        total_time = timedelta()

        try:
            with open(input_file, mode='r', newline='') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    date_str = row['date']
                    date_parts = date_str.split('-')
                    row_year = int(date_parts[0])
                    row_month = int(date_parts[1])
                    row_week = int(row['week']) if 'week' in row else None
                    
                    time_str = row['time']
                    h, m, s = map(int, time_str.split(':'))
                    duration = timedelta(hours=h, minutes=m, seconds=s)
                    
                    if period_type == 'week' and row_week == period_value:
                        total_time += duration
                    elif (period_type == 'month' 
                          and row_year == period_value[0] 
                          and row_month == period_value[1]):
                        total_time += duration
                    elif period_type == 'year' and row_year == period_value:
                        total_time += duration

            total_seconds = int(total_time.total_seconds())
            total_hours, remainder = divmod(total_seconds, 3600)
            total_minutes, total_seconds = divmod(remainder, 60)
            total_time_str = (f"{total_hours:02}:{total_minutes:02}:"
                              f"{total_seconds:02}")

            result = (f"Total time for {period_type} {period_value} is:" 
                      f" {total_time_str}")
            print(result)
            self.text_edit.setPlainText(result)
        except FileNotFoundError:
            print(f"File {input_file} not found.")
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")

    def calculate_total_distance(self, period_type, period_value):
        """This method calculates total distance for a given period
           (week, month, year)"""
        total_distance = 0.0
    
        try:
            with open(input_file, mode='r', newline='') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    date_str = row['date']
                    date_parts = date_str.split('-')
                    row_year = int(date_parts[0])
                    row_month = int(date_parts[1])
                    row_week = int(row['week']) if 'week' in row else None
                    distance = float(row['distance'])
                    
                    if period_type == 'week' and row_week == period_value:
                        total_distance += distance
                    elif (period_type == 'month' 
                          and row_year == period_value[0] 
                          and row_month == period_value[1]):
                        total_distance += distance
                    elif period_type == 'year' and row_year == period_value:
                        total_distance += distance

            result = (f"Total distance for {period_type} {period_value}:"
                      f" {total_distance:.2f} kms")
            print(result)
            self.text_edit.setPlainText(result)
        except FileNotFoundError:
            print(f"File {input_file} not found.")
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")

    def calculate_average_temp(self, period_type, period_value):
        """This method calculates the average temp (time per km) for a given 
        period (week, month, year)"""
        total_time = timedelta()
        total_distance = 0.0
    
        try:
            with open(input_file, mode='r', newline='') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    date_str = row['date']
                    date_parts = date_str.split('-')
                    row_year = int(date_parts[0])
                    row_month = int(date_parts[1])
                    row_week = int(row['week']) if 'week' in row else None
                    
                    time_str = row['time']
                    h, m, s = map(int, time_str.split(':'))
                    duration = timedelta(hours=h, minutes=m, seconds=s)
                    
                    distance = float(row['distance'])
                    
                    if period_type == 'week' and row_week == period_value:
                        total_time += duration
                        total_distance += distance
                    elif (period_type == 'month' 
                          and row_year == period_value[0] 
                          and row_month == period_value[1]):
                        total_time += duration
                        total_distance += distance
                    elif period_type == 'year' and row_year == period_value:
                        total_time += duration
                        total_distance += distance

            if total_distance > 0:
                total_seconds = int(total_time.total_seconds())
                average_temp_seconds = total_seconds / total_distance
                average_minutes, average_seconds = divmod(
                    average_temp_seconds, 60)
                average_temp = (f"{int(average_minutes):02}:"
                                f" {int(average_seconds):02}")
            else:
                average_temp = "00:00"

            result = (f"Average temp for {period_type} {period_value} is:"
                      f" {average_temp} per km")
            print(result)
            self.text_edit.setPlainText(result)
        except FileNotFoundError:
            print(f"File {input_file} not found.")
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")

    def paintEvent(self, event):
        """Override the paintEvent to handle custom painting for the widget"""
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def print_the_whole_file(self):
        with open(input_file, mode='r', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            data_list = []
            for row in reader:
                data_list.append(row)
        for row in data_list:
            print(row)
