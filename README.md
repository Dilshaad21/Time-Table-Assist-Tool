# Time_Table_Assist_Tool
## Team  Members
* A.Dilshaad B18041
* Rahul Anand B18078
* Mohd Asim Ansari B18177
* Mohib Qureshi B18070
* Abhinav Kumar B18099

## Time Table assistance app version 1
It is a web based application to automatically generate time table. Just for version 1, we are taking input from csv files located on the local file system, however in future we are aiming to link it with the database.

## Design 
* Takes two course-slot data and classroom-capacity data files as input from the user.
* Checks if there is any clash.
* If all constraints are satisfied, the time table is generated.
* If any constraint is violated, error message is shown.

## Requirements

* Python3
* Django setup

## How to run?

* Clone this repo using git clone https://github.com/Dilshaad21/Time_Table_Assist_Tool
* Navigate to the directory, Time_Table_Assist_Tool
* Start the server using the command python manage.py runserver 
* Go to the browser and type http://localhost:8000/home/upload/
* Click the choose file button to choose course-slot and classroom-capacity data files simultaneaously. Click on choose file button, press ctrl and select both the files in one go. Don't select the files separately. 
* After the files are selected, Click on submit button.
* If there is no clash, time table will be shown, otherwise an error message will be displayed.
