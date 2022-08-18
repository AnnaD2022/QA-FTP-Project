# checkDate: removed main.py function

## Reason for removal:
The checkDate function implemented input file handling logic which has been implemented and integrated as part of the validate_data.py script thus has been rendered redundant.

## Function descriptor
-	Iterating through all of the files which have been stored in the designated files folder in our repo
-	If the file has type '.csv', then it replaces the file name with “Med_DATA_”
-	Year, month and day are abstracted from the filename, formatted as a date by inserting '/',  the date and file name are then added to the respective arrays

## Test plan:
|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
|test_cd1 | Contents of the 'temp' repository folder | True - number of entries in filenames array should match the number of csv files in the temp folder | passes 13/08/2022| [Tested code](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br><br> [Folder containing all inputs](https://github.com/AnnaD2022/QA-FTP-Project/tree/main/temp) <br><br>  [Unit test file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_main_checkDate.py) |
|test_cd2 | Contents of the 'temp' repository folder | True - number of entries in dates array should match the number of csv files in the temp folder | passes 13/08/2022| [Tested code](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br><br> [Folder containing all inputs](https://github.com/AnnaD2022/QA-FTP-Project/tree/main/temp) <br><br>  [Unit test file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_main_checkDate.py) |

### Test
[Test created and passing before function removal](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_main_checkDate.py)