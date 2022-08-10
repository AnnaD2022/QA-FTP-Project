# Class function descriptors
## Main.py
#### checkDate:
-	Iterating through all of the files which have been stored in the designated files folder in our repo
-	If the file has type '.csv', then it replaces the file name with “Med_DATA_”
-	Year, month and day are abstracted from the filename, formatted as a date by inserting '/',  the date and file name are then added to the respective arrays

#### dateLogic: 
-	Date.today is used to get todays date, the components of ‘todays’ date are then stored in arr1
-	arr2 contains the current date as determined by the calendar
-	The dates are compared using a for loop, if the ‘today date’ value is greater than the cal.getdate value then the date is valid. If y,which controls indexing, is 1 less then the length of arr1 and the today date values in array 1 are greater than or equal to the values at a set index position in array 2 then the date is again valid.
-	If the date is invalid an error message gets shown, current date is configured to be that from the calendar
-	Arrays storing files, etc are checked. If there are no files for that date then an error message is shown.

#### ‘_main’: 
-	Setting up the gui
-	Current date is set to the ‘today date’

## Server.py
-	Creating a user with log in credentials, server is created and run

## Update validate_file.py
#### Verify data:
-	Calls all the verification methods as detailed below.

#### Check_header:
-	Checks header line contains what it should, etc
-	If its not the right header name, the error is identified and then a description is added to diff_string in a certain format. Files log name is defined as the file name with a  ‘.csv’ extension.  A log.txt file is then created for the invalid csv file detailing the issues with the header as included in the ‘diff_string’. The header is then replaced with the correct header and the correctly formatted csv file created.

#### Remove_empty:
-	Checks the file data, locates any missing values citing their row and column position as x and y coordinates.
-	If there is a missing value then a list of the coordinates of these missing values are created, an error message for each one created in the ‘error_string’.
- A log is created for the invalid file – file name with a csv extension
- A log.txt file is created for this invalid file detailing the errors with the missing values

#### Check_num_rows:
-	Counts number of rows, if there are not 10 rows then a log is created for the invalid file – file name with a csv extension
-	A log.txt file is created for this invalid file detailing the fact the number of rows is wrong

#### Check_ids:
-	File batch id is acquired using the header value ‘batch_id’ as a reference
-	if the id has the type integer and is greater than 0, then the list of batch id's is checked, if this id already exists in the id list then an error message is defined and the ‘is_invalid’ Boolean value is set to True, else it gets added to the list.
-	If the Id is not an integer then a relevant error message is generated and the ‘is_invalid’ Boolean value is set to True
-	If neither of the above if statements are satisified, then it defaults to believing the id is negative and an error message is generated and the ‘is_invalid’ Boolean value is set to True
-	If ‘is_invalid’ Boolean value is set to True then a log with the file name but a .csv extension is created as is a log.txt file detailing the issue with the batch id.

#### Check_num_columns:
-	Counts number of columns in each row, if there are not 12 columns then A log file is created for the invalid file – file name with a csv extension
-	A log.txt file is created for this invalid file detailing the fact the number of columns is wrong

#### Check_timestamp:
-	Goes through all values in the ‘timestamp’ column and checks if the listed timestamp matches the pre-defined format, if not an error message is generated as is a log and log.txt file for this invalid file.

#### Main:
-	Each input file is checked to see if its empty, if it is then a log for that file is generated and populated with the relevant error data, if not then the file is read.

## Client.py
-	Calls the relevant server functions to create a client and connect to server
-	File names on server are iterated through and those which have type csv are read
