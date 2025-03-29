import datetime
from datetime import date, timedelta
import csv
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,
                             QTextEdit
                             )
from PyQt5.QtGui import QPixmap, QPainter, QRegExpValidator
from PyQt5.QtCore import QRegExp

today = str(date.today())
input_file = 'running_data.csv'
log_file = 'requests_log.txt'

class RunDataForm(QWidget):
    """
    RunDataForm is a PyQt5-based QWidget class that provides a graphical user
    interface for a running app. It allows users to input and calculate various
    metrics related to running, such as distance, time, total time, total
    distance, and average pace.

    Attributes:
        image (QPixmap):
            Background image for the widget.
        text_edit (QTextEdit):
            A text area for displaying results and messages.
        line_edit_distance (QLineEdit):
            Input field for entering the running distance.
        line_edit_time (QLineEdit):
            Input field for entering the running time.
        line_edit_total_time (QLineEdit):
            Input field for calculating total time.
        line_edit_total_distance (QLineEdit):
            Input field for calculating total distance.
        line_edit_average_temp (QLineEdit):
            Input field for calculating average pace.

    Methods:
        __init__():
            Initializes the RunDataForm widget.
        init_ui():
            Sets up the user interface layout and components.
        add_input_field(layout, label_text, placeholder, regex, max_len, row):
            Adds a labeled input field to the layout.
        add_button(layout, text, callback, row, col):
            Adds a button to the layout.
        get_week_number():
            Returns the current week number of the year.
        input_data():
            Handles the input of distance and time data and appends it to a 
            file.
        calculate_total_time_from_input():
            Processes input and calculates total time.
        calculate_total_distance_from_input():
            Processes input and calculates total distance.
        calculate_average_temp_from_input():
            Processes input and calculates average pace.
        process_input(line_edit, callback):
            Parses and validates input text, then calls the callback.
        calculate_total_time(period_type, period_value):
            Calculates total time for a given period.
        calculate_total_distance(period_type, period_value):
            Calculates total distance for a given period.
        calculate_average_temp(period_type, period_value):
            Calculates average pace for a given period.
        calculate_metric(period_type, period_value, field, formatter):
            Generic method to calculate a metric.
        aggregate_data(period_type, period_value, field=None):
            Aggregates data for a given period and field.
        match_period(row, period_type, period_value):
            Checks if a data row matches the specified period.
        format_time(total_time):
            Formats a timedelta object into a string (HH:MM:SS).
        display_result(result):
            Displays a result in the text area and logs it to a file.
        append_to_file(file_path, new_row, header):
            Appends a new row of data to a file.
        write_requests_to_file(result):
            Logs a result to a file with a timestamp.
        paintEvent(event):
            Paints the background image on the widget.
    """

    def __init__(self):
        super().__init__()
        self.image = QPixmap("images/image_3_running_man.jpg")
        self.setWindowTitle('Running App')
        self.resize(360, 475)
        self.setMinimumSize(250, 300)

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.add_input_field(layout, "Distance", "Please enter distance: KM.MM",
                             r"^(?:[0-9]|[1-9][0-9])\.[0-9][0-9]$", 5, 0)
        self.add_input_field(layout, "Time", "Please enter time: HH:MM:SS",
                             r"^(?:[01]?\d|2[0-3]):[0-5]?\d:[0-5]?\d$", 8, 1)

        self.add_button(layout, "Input Data", self.input_data, 2, 1)

        self.add_input_field(layout, "Total time", "period type, period value",
                             None, None, 3)
        self.add_button(layout, "Calculate total time",
                        self.calculate_total_time_from_input, 3, 2)

        self.add_input_field(layout, "Total distance",
                             "period type, period value", None, None, 4)
        self.add_button(layout, "Calculate total distance",
                        self.calculate_total_distance_from_input, 4, 2)

        self.add_input_field(layout, "Average temp",
                             "period type, period value", None, None, 5)
        self.add_button(layout, "Calculate average temp",
                        self.calculate_average_temp_from_input, 5, 2)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText(
            "You will see your results here SOON!\n"
            "period type, period value\nrun, 2025-02-28\nweek, 7\n"
            "month, 2025-02\nyear, 2025"
        )
        self.text_edit.setMaximumHeight(100)
        layout.addWidget(self.text_edit, 6, 0, 1, 2)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.text_edit.clear)
        layout.addWidget(ok_button, 6, 2)

        self.setLayout(layout)

    def add_input_field(
            self, layout, label_text, placeholder, regex, max_len, row):
        label = QLabel(f'<font size="4"><b> {label_text} </b></font>')
        label.setAccessibleName(label_text)
        layout.addWidget(label, row, 0)

        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        line_edit.setStyleSheet("border-radius: 3px")
        line_edit.setAccessibleName(f"{label_text} Input")
        if regex:
            validator = QRegExpValidator(QRegExp(regex))
            line_edit.setValidator(validator)
        if max_len:
            line_edit.setMaxLength(max_len)
        layout.addWidget(line_edit, row, 1)

        setattr(self, f"line_edit_{label_text.lower().replace(' ', '_')}",
                line_edit)

    def add_button(self, layout, text, callback, row, col):
        button = QPushButton(text)
        button.setMinimumWidth(150)
        button.clicked.connect(callback)
        button.setAccessibleName(text)
        button.setToolTip(f"Click to {text.lower()}")
        layout.addWidget(button, row, col, 1, 2)

    def get_week_number(self):
        return datetime.date.today().isocalendar()[1]

    def input_data(self):
        week_number = str(self.get_week_number())
        new_row = [week_number, today, self.line_edit_distance.text(),
                   self.line_edit_time.text()]
        self.append_to_file(
            input_file, new_row, ['id', 'week', 'date', 'distance', 'time'])
        self.line_edit_distance.clear()
        self.line_edit_time.clear()

    def calculate_total_time_from_input(self):
        self.process_input(
            self.line_edit_total_time, self.calculate_total_time)

    def calculate_total_distance_from_input(self):
        self.process_input(
            self.line_edit_total_distance, self.calculate_total_distance)

    def calculate_average_temp_from_input(self):
        self.process_input(
            self.line_edit_average_temp, self.calculate_average_temp)

    def process_input(self, line_edit, callback):
        input_text = line_edit.text()
        try:
            period_type, period_value = input_text.split(',')
            period_type = period_type.strip()
            if period_type in ['month', 'run']:
                period_value = tuple(map(int, period_value.strip().split('-')))
            else:
                period_value = int(period_value.strip())
            callback(period_type, period_value)
        except ValueError:
            self.text_edit.setPlainText(
                "Invalid input format."
                "Please enter 'period type, period value'."
            )

    def calculate_total_time(self, period_type, period_value):
        self.calculate_metric(
            period_type, period_value, 'time', self.format_time)

    def calculate_total_distance(self, period_type, period_value):
        self.calculate_metric(
            period_type, period_value, 'distance', lambda x: f"{x:.2f} kms")

    def calculate_average_temp(self, period_type, period_value):
        total_time, total_distance = self.aggregate_data(
            period_type, period_value)
        if total_distance > 0:
            avg_seconds = int(total_time.total_seconds() / total_distance)
            avg_temp = f"{avg_seconds // 60:02}:{avg_seconds % 60:02}"
        else:
            avg_temp = "00:00"
        self.display_result(
            f"Average temp for {period_type} {period_value} is: "
            f"{avg_temp} per km")

    def calculate_metric(self, period_type, period_value, field, formatter):
        total = self.aggregate_data(period_type, period_value, field)
        self.display_result(
            f"Total {field} for {period_type} {period_value} is: "
            f"{formatter(total)}")

    def aggregate_data(self, period_type, period_value, field=None):
        total_time = timedelta()
        total_distance = 0.0
        try:
            with open(input_file, mode='r', newline='') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    if self.match_period(row, period_type, period_value):
                        if field == 'time' or field is None:
                            h, m, s = map(int, row['time'].split(':'))
                            total_time += timedelta(
                                hours=h, minutes=m, seconds=s)
                        if field == 'distance' or field is None:
                            total_distance += float(row['distance'])
            return (total_time, total_distance) if field is None else \
                total_time if field == 'time' else total_distance
        except FileNotFoundError:
            print(f"File {input_file} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def match_period(self, row, period_type, period_value):
        date_parts = list(map(int, row['date'].split('-')))
        row_week = int(row['week']) if 'week' in row else None
        if period_type == 'week' and row_week == period_value:
            return True
        elif period_type == 'month' and date_parts[:2] == list(period_value):
            return True
        elif period_type == 'year' and date_parts[0] == period_value:
            return True
        elif period_type == 'run' and date_parts == list(period_value):
            return True
        return False

    def format_time(self, total_time):
        total_seconds = int(total_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def display_result(self, result):
        print(result)
        self.text_edit.setPlainText(result)
        self.write_requests_to_file(result)

    def append_to_file(self, file_path, new_row, header):
        try:
            max_id = 0
            try:
                with open(file_path, mode='r', newline='') as infile:
                    reader = csv.reader(infile, delimiter='\t')
                    header = next(reader, [])
                    max_id = max(
                        (int(row[0]) for row in reader if row), default=0)
            except FileNotFoundError:
                pass

            new_row.insert(0, max_id + 1)
            with open(file_path, mode='a', newline='') as outfile:
                writer = csv.writer(outfile, delimiter='\t')
                if not header:
                    writer.writerow(header)
                writer.writerow(new_row)
        except Exception as e:
            print(f"An error occurred: {e}")

    def write_requests_to_file(self, result):
        self.append_to_file(
            log_file, 
            [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result], 
            []
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
