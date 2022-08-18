# check_num_columns: removed validate_file function

## Reason for removal:
-   This function has now been removed as it was made redundant by check_header

## Function descriptor
-	Gets the number of columns in each row of the file, if there are not 12 columns then an info.txt file is created for this invalid file detailing the fact the number of columns is wrong, and is_invalid is set to True (it is instantiated as False)
-   If one row has an invalid number of columns, the other rows are not checked
-   is_invalid is returned to verify_data

## Test plans
#### check_num_columns:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| test_cnc1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| Passes 12/08/2022 | [Tested code](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py) <br><br>  [Tested document](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/testDoc1Valid.csv) <br><br>  [Unit test file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_num_columns.py)|
| test_cnc2 | file_data: pandas.read_csv(testDoc2.1Invalid.csv)<br>file_name: testDoc2.1InvalidRC.csv |A log file with the title 'testDoc2.1Invalid_log.txt' will be created containing the message "Error 600 - Too Many values - 11 columns instead of 10 on line 2", True will be returned| Passes 12/08/2022 | [Tested code](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py) <br><br>  [Tested document](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/testDoc2.1Invalid.csv) <br><br> [Unit test file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_num_columns.py)|

### Test
[Test created and passing before function removal](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_num_columns.py)