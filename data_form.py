import sys
import datetime
import csv
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,)


class RunDataForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Run Data Form')
        self.resize(250, 120)

        layout = QGridLayout()

        label_distance = QLabel('<font size="4"> Distance </font>')
        self.lineEdit_distance = QLineEdit()
        self.lineEdit_distance.setPlaceholderText('Please enter distance: KK:MMM')
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
        """This method allows to get week's number."""
        today = datetime.date.today()            
        return today.isocalendar()[1]
        

    def input_data(self):
        """
        This method input data to the output.csv file in the following format:
        week number, distance and time.
        """
        week_number = str(self.get_week_number())
        text = (week_number + " " +self.lineEdit_distance.text() + 
                " " + self.lineEdit_time.text())

        with open('output.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([text])
        
        print("Data saved to output.csv")
       
    
    

    
    

    