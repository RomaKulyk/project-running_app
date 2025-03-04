V1.0
----------
TO-DO_1 - create calculate_average_temp... week, month, year methods - DONE

TO-DO_2 - create calculate_total_time... week, month, year methods - DONE

TO-DO_3 - create calculate_total_distance... week, month, year methods - DONE

TO-DO_4 - if hew year has started should be created new files for storing 
results -> there is NO sense to do it since: Excel has a CSV row limit 
of 1,048,576 rows and Google Sheets has a similar CSV max row limit.
It is easily allows to cover or athlet life - NO NEED

TO-D0_5 - Create a display which will show the calculation result in app
instead of just printing it to terminal - DONE

TO-D0_6 - Make possibility to enter the time's period in 'calculate_total_time',
'calculate_total_distance', and 'calculate_average_temp' functions - DONE


V2.0
-----------
TO-DO_7 - Make hint in display visible after clearing result 
from previous request - DONE

TO-DO_8 - After clicking on "Calculate ..." button appropriate QLineEdit 
field s/b cleared - DONE

TO-DO_9 - make prompts "Please enter distance: KM:MM, Please enter time: 
HH:MM:SS" visible within the QLineEdit fields - DONE

TO-DO_10 - make prompts "period type, period value" visible within 
the QLineEdit fields - DONE

TO-DO_11 - allow to another user to login and use the app - DONE

TO-DO_12 - Make design more attracktive and labels texts more readable:- DONE
        - labels s/b bold - DONE
        - all fields and buttons s/b in the same style, fields borders 
        s/b rounded - DONE
        - make labels in white color to see the difference - DONE
        - find another image - DONE

TO-DO_13 - create a write_requests_to_file function which will write all 
requests' results into the log file - DONE

TO-DO_14 - update input_data function to allow enter only reasonable data into 
the QLineEdit fields - DONE (by updating QLineEdit fields for entering running
data with regular expression validator).

TO-DO_16 - create a shortcut to run the app - DONE 

TO-DO_18 - update existing functions:calculate_total_time, 
calculate_total_distance, calculate_average_temp to add possibility to 
calculate those parameters for the certain
run(invoke it by date) - DONE

TO-D0_20 - find the way to enhance app with Copilot and put it into
backlog for V3.0 - DONE

TO-D0_21 - check with pycodestyle for coherence to PEP-8 -DONE


V2.1_testsing
-----------
TO-DO_19 - create unit test to cover all the functions.



V3.0(SQLite)
----------
TO-DO_17 - As a developer, I want to update the input_data method
so that different users have a different running_data.csv file.
SQLite is an in-process library that implements a self-contained, serverless,
zero-configuration, transactional SQL database engine.

TO-DO_22 - As a user, I want to have the possibility to enter running data for
a certain date.

TO-DO_23 - As a developer, I want to update the input_data function to allow
entering only reasonable data into the QLineEdit fields for password and login.

TO-DO_24 -  As a user, I want to have the possibility to see the
running data from the last five runs.

TO-DO_25 - As a developer, I want to have the possibility to see the
backlog in markdown format.

TO-D0_26 - As a developer, I want to have the data_form.py file to be split
into several smaller files.

TO-DO_27 - As a user, I want to enter data into "QLineEdits" fields by clicking
the "Enter" button.


NEVER RELEASED
--------------
TO-DO_15 - in running_data.csv file entered data s/b alligned with 
the headers.
(using Rainbow CSV extendion in Visual Studio and "Align CSV Columns with 
whitespaces" option it breaks how the functions work.)

