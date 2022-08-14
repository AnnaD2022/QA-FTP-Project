# QAFTPProject

Repo to store project files for task set by QA regarding download + verification of CSV files

## REQUIREMENTS

- pyftpdlib
- pandas
- tkcalendar

## ERROR CODES

The system produces error codes denoting problems with invalid files, which are stored in their respective log files:
- 000 - Valid File (Logged without preceding "Error")
- 100 - Empty File
- 200 - Incorrect Header
- 201 - Fatal Incorrect Header
- 300 - Missing Values
- 400 - Incorrect Number of Rows
- 500 - Invalid Batch ID
- 600 - Too Many Values
- 700 - Incorrect Timestamp
- 800 - Int, Not Float
- 801 - Incorrect Data Type
- 802 - Incorrect Rounding
- 803 - Value Out of Range