project
=======

CPSC 491 FileMaker Assistant Project - Clemson

BobaFett Calendar Visualization App

-Application can be run by icon double-click
-Once run, the application will read in and show data from the required XML file, here:

	/Volumes/FileMaker/BobaFettCalendarInterface/FMxml.xml

-There is another XML file that holds Employee and Status information which is read upon loading the program and clicking the update button.  It is located here:

	/Volumes/FileMaker/BobaFettCalendarInterface/EmployeesAndStatuses.xml

-Once loaded, a user may access any day in a Daily, Weekly, or Bi-Weekly view by clicking on the date and selecting the desired day.

	Each list will contain at least:
		-FileMaker number
		-Description (Title)
		-Artist / Editor information
		-Project Status

-Checkboxes on the left pane of the program default to 'Checked' and may be checked or unchecked as desired to filter data that appears in the main viewing fields.
 
The 'Add Employee' button may be used to add a new employee.  Employees must be added in order to view records where they are listed as the active employee in FileMaker.  Editor information works the exact same way, also through 'Add Employee.'  Adding a new employee requires a color associated with the employee to be added which may be chosen by the color dialogue box.

* NOTE * The employee's name is type-sensitive.  Take care to add the employee with the exact same set of characters (including the location of spaces) as it is entered in FileMaker.

The 'Add Status' button may be used to add a new status.  It works exactly the same way as Add Employee with the exception that no color is required.

	* NOTE * The status name is also type-sensitive with respect to it's entry in FileMaker.

The 'Remove Status' and 'Remove Employee' options are accessible through the FILE drop-down menu, and require typing in the name of the employee or status of which removal is desired.  'Remove Employee' and 'Remove Status' are type-sensitive also.


Required Date Format

BobaFett will only recognize dates entered into FileMaker with an acceptable date format for both the date the job was created (the Job Start Date field in FileMaker) and the date the job is due (the Due to Client field in FileMaker).  If no due date is entered, BobaFett will add one calendar year to the job's timeline in order to display the record.  Acceptable date formats are on the next page:
Acceptable Date Formats

These are the only date formats BobaFett will recognize:

	-m/d/yyyy
	-m/dd/yyyy
	-mm/d/yyyy
	-mm/dd/yyyy

* NOTE * The locations and use of the slash characters as well as the lack of spacing is important.
