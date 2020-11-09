# Time_Table_Assist_Tool
## Team  Members
* A.Dilshaad B18041
* Rahul Anand B18078
* Mohd Asim Ansari B18177
* Mohib Qureshi B18070
* Abhinav Kumar B18099

## Time Table assistance app version 1
It is a web based application to automatically generate time table. For version 1 we are taking input from csv files located on the local file system, however in future we are aiming to link it with the database.

## Design 
* Takes two course-slot data and classroom-capacity data files as input from the user.
* Checks if there is any clash.
* If all constraints are satisfied,then generates time table.
* If any constraint is violated shows the error.

## Requirements

* Python3
* Django setup

## How to run?

* Clone this repo using git clone https://github.com/Dilshaad21/Time_Table_Assist_Tool
* Go to the folder Time_Table_Assist_Tool
* Start the server using the command python manage.py runserver 
* Go to the browser and type http://localhost:8000/home/upload/
* Choose course-slot and classroom-capacity data files by clicking choose file button.
* Click submit.
* If no clash time table will be shown, otherwise error will be displayed.
