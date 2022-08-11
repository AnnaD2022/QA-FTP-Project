# Test Plan

## main

#### checkDate:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| | | | | https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py|
| | | | | https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py |

#### dateLogic:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| | | | | https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py |
| | | | | https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py|


## validate_file:

#### check_header:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
|ch1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return without producing a log file as header values are valid | | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| ch2 | file_data: pandas.read_csv(testDoc2invalid.csv)<br>file_name: testDoc2invalid.csv | A log file with the title 'testDoc2invalid_log.txt' will be created containing the message "Error 200 - Incorrect Header - Errors: replaced reading1 with wrong1, replaced reading7 with wrong7. Header was repaired.", testDoc2invalid.csv will now contain the correct headers| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document:  https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc2Invalid.csv|
| ch3 | file_data: pandas.read_csv(testDoc2.1invalid.csv)<br>file_name: testDoc2.1invalid.csv | A log file with the title 'testDoc2.1invalid_log.txt' will be created containing the message "Error 200 - Incorrect Header - Errors: inserted added. Header was repaired.", testDoc2.1invalid.csv will now contain the correct headers| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc2.1Invalid.csv |
| ch4 | file_data: pandas.read_csv(testDoc3InvalidRC.csv)<br>file_name: testDoc3InvalidRC.csv | A log file with the title 'testDoc3InvalidRC_log.txt' will be created containing the message "Error 200 - Incorrect Header - Errors: deleted reading6. Header was repaired.", testDoc3InvalidRC.csv will now contain the correct headers| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc3InvalidRC.csv |

#### remove_empty:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
|re1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| re2 | file_data: pandas.read_csv(testDoc2invalid.csv)<br>file_name: testDoc2invalid.csv |  A log file with the title 'testDoc2invalid_log.txt' will be created containing the message "Error 300 - Missing Values - Column 2 Row 7. Column 5 Row 5. Column 8 Row 10.", True will be returned.| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc2Invalid.csv |

#### check_num_rows:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| cnr1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| cnr2 | file_data: pandas.read_csv(testDoc3InvalidRC.csv)<br>file_name: testDoc3InvalidRC.csv |A log file with the title 'testDoc3InvalidRC_log.txt' will be created containing the message "Error 400 - Incorrect Number of Rows - 9 rather than 10", True will be returned| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc3InvalidRC.csv |

#### check_ids:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| cid1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| cid2| file_data: pandas.read_csv(testDoc4DupBID.csv)<br>file_name: testDoc4DupBID.csv | A log file with the title 'testDoc4DupBID_log.txt' will be created containing the message "Error 500 - Invalid Batch ID - Duplicate ID 107", True will be returned | | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc4DupBID.csv |
| cid3| file_data: pandas.read_csv(testDoc4NegBID.csv)<br>file_name: testDoc4NegBID.csv | A log file with the title 'testDoc4NegBID_log.txt' will be created containing the message "Error 500 - Invalid Batch ID - Negative ID -9", True will be returned | | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc4NegBID.csv|
| cid3| file_data: pandas.read_csv(testStr4DupBID.csv)<br>file_name: testDoc4StrBID.csv | A log file with the title 'testDoc4StrBID_log.txt' will be created containing the message "Error 500 - Invalid data type 'string'", True will be returned | | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc4StrBID.csv|

#### check_num_columns:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| cnc1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| cnc2 | file_data: pandas.read_csv(testDoc2.1Invalid.csv)<br>file_name: testDoc2.1InvalidRC.csv |A log file with the title 'testDoc2.1Invalid_log.txt' will be created containing the message "Error 600 - Too Many values - 11 columns instead of 10 on line 2", True will be returned| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc2.1Invalid.csv  |

#### check_timestamp:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| cts1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| cts2| file_data: pandas.read_csv(testDoc5InvalidTS.csv)<br>file_name: testDoc5InvalidTS.csv| A log file with the name: testDoc5InvalidTS_log.txt will be created containing the message "Error 700 - Incorrect Timestamp -\ 20-20-20 \ on line 11" | | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc5InvalidTS.csv |

#### check_readings:

|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
| cr1 |file_data: pandas.read_csv(testDoc1Valid.csv)<br>file_name: testDoc1Valid.csv | function will return False without producing a log file| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc1Valid.csv |
| cr2 | file_data: pandas.read_csv(testDoc6.1notfloar.csv)<br>file_name: testDoc6.1notfloar.csv | A log file with the name: 'testDoc6.1notfloar_log.txt' will be created containing the message: "Error 800 -Int, Not Float, row 3 column 5. Cast as float, Error 801 - Incorrect Data Type row 4 column 5" True will then we returned| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc6.1notfloar.csv|
| cr3 | file_data: pandas.read_csv(testDoc6.2RangeDP.csv)<br>file_name: testDoc6.2RangeDP.csv.csv | A log file with the name: 'testDoc6.2RangeDPr_log.txt' will be created containing the message: "Error 802 - Incorrect Rounding: 6.162783
 row 5 Column 5, Error 803 - Value Out of Range - 90.341 row 11 column 3" True will then we returned| | tested code: https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py <br> tested document:https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/testDoc6.2RangeDP.csv |