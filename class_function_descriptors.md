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
-	Calls all the verification methods as detailed below. Returns a boolean representing whether a file is valid or not.

#### Check_header:
-	Checks header line is correct
-	If it is incorrect, the error is identified and a description is stored in the variable diff_string in a certain format. The info file name for the file being processed is created by removing the ".csv" extension from the file name and adding "_info.txt".  The info file is then created for the invalid csv file detailing the issues with the header as included in the ‘diff_string’. 
-   If possible, the header is then replaced with the correct header and the correctly formatted csv file created, with the error reported in the info file without the file being marked as invalid.  Otherwise, the file is marked as invalid.
-   If there are no issues with the header, the file is not marked as invalid
-   Finally, the value representing whether or not the header tests have passed is returned to verify_data

#### Remove_empty:
-	Checks the file data, locates any missing values citing their row and column position as x and y coordinates.
-	If there is a missing value then a list of the coordinates of these missing values are created, an error message for each one created in the ‘error_string’.
-   An info.txt file is created for this invalid file detailing the errors with the missing values
-   The value representing whether or not the tests have passed is returned to verify_data

#### Check_num_rows:
-	Gets the number of rows int the file
-   If there are not 10 rows then an info.txt file is created for this invalid file detailing the fact the number of rows is wrong
-   The value representing whether or not the tests have passed is returned to verify_data
-   It is assumed that 10 rows is correct for each file as this is the case for the test data, but this can easily be changed

#### Check_ids:
-	All of the batch ids in the file are acquired using the header value ‘batch_id’ as a reference
-   For each id in the file, the following test are performed:
-	If the id has the type integer and is greater than 0, then the set of batch ids that have already been processed is checked, and if the current id already exists in the set then an error message is created and the ‘is_invalid’ Boolean value is set to True, otherwise, the id is considered valid and it is added to the set.
-	If the id is not an integer then a relevant error message is generated and the ‘is_invalid’ Boolean value is set to True
-	If neither of the above if statements are satisified, then it is assumed that the id is negative (out of range). An error message is generated and the ‘is_invalid’ Boolean value is set to True
-   If one batch id fails these tests, the rest of the ids in the file are not checked
-	If ‘is_invalid’ Boolean value is set to True then an info.txt file detailing the issue with the batch id is created.
- is_invalid is returned to verify_data

#### Check_num_columns (removed):
-	Gets the number of columns in each row of the file, if there are not 12 columns then an info.txt file is created for this invalid file detailing the fact the number of columns is wrong, and is_invalid is set to True (it is instantiated as False)
-   If one row has an invalid number of columns, the other rows are not checked
-   is_invalid is returned to verify_data
-   This function has now been removed as it was made redundant by check_header

#### Check_timestamp:
-	Goes through all values in the ‘timestamp’ column and checks if each listed timestamp matches the regex for the pre-defined format, if not an error message is generated and stored in an info.txt file for this invalid file.  is_invalid is set to True (it is instantiated as False)
-   If one timestamp is incorrect, the rest are not checked
-   is_invalid is returned to verify data

### Check_readings:
-   For each reading in each row, the following tests are performed:
-   If the reading is not a float, it is checked it see if it is an int.  If it is, it is cast as a float, and the updated value is saved to the csv file.  An info.txt file is still created reporting the error, but the file is not marked as invalid.
-   If the reading is not a float or an int, the error cannot be fixed, so the file is marked as invalid and the error is reported in the file's info.txt file.
-   The number of decimal places of the reading is checked. If it is greater than 3, the reading is rounded to 3 d.p. and the updated value is saved to the csv file.  The file is not marked as invalid as the error has been fixed, but a message describing the error is still added to the file's info.txt file.
-   Finally, it is checked that the reading is between 0 and 10 (in range).  If it is not, the file is marked as invalid and the error is recorded in the info.txt file.
-   If one reading is incorrect, the rest are not checked.
-   If all the readings pass all the texts, it is returned that the file is not invalid (by this function)

#### Main:
-   Each csv is loaded into the program from the directory that they are downloaded from the server to.
-	Each input file is checked to see if its empty, if it is then an info.txt file for that file is generated and populated with the relevant error data, and the file is marked as invalid
-    If it is not empty, then the contents of the file are read into a dataframe, which is passed along with the file name into verify_data so that further tests can be performed on it.
-  Once all of the tests have been completed, the year, month and day of the file are taken from the file name
-   If the file is invalid, it is moved along with its info.txt file to the "rejected" folder and sorted into a calendar-based directory structure based on the date of the csv file.
-   If the file is valid, a message denoting this is added to its info.txt file.  They are both then moved to the "successful" folder and sorted into a calendar-based directory structure based on the date of the csv file.
-   In both cases, if the desired directory does not already exist, then it is created before the files are moved.


## Client.py
-	Calls the relevant server functions to create a client and connect to server
-	File names on server are iterated through and those which have type csv are read
