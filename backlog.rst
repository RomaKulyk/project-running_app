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


TO-DO_15 - in running_data.csv file entered data s/b alligned with 
the headers.
(using Rainbow CSV extendion in Visual Studio and "Align CSV Columns with 
whitespaces" option it breaks how the functions work.)

TO-DO_16 - create a shortcat to run the app.

TO-DO_17 - update input_data method for different users to have different 
running_data.csv file

TO-DO_18 - update existing functions:calculate_total_time, 
calculate_total_distance, calculate_average_temp to add possibility to 
calculate those parameters for the certain
run(invoke it by date)

TO-DO_19 - create unit test to cover all the functions.

TO-D0_20 - find the way to enhance app with Copilot and put it into
 backlog for V3.0.

TO-D0_21 - check with pycodestyle for coherence to PEP-8.


V3.0
----------
TO-DO_22 - add possibility to enter date while input running data.
TO-DO_23 - update input_data function to allow enter only reasonable data into 
the QLineEdit fields for password and login.

GIT-COMMANDS
-------------------------------------
git tag - to see all existing tag
git tag <tag-name> - create a new tag
git tag -d <tag-name> - delete tag
-------------------------------------
git branch -to see all existing branch
git branch <branch name> - create a new branch
git checkout <branch name> - switch to a branch
git merge <branch name> - merge <branch name> to the current branch
git push origin <branch name> - push the updated <branch name> to the remote repository
git branch --merged - list all merged branches
git branch --no-merged - list all no merged branches
git branch -d <branch name> - to delete a local branch named <branch name>
git push origin --delete <branch name> - to delete a remote branch named <branch name>


