# QAFTPProject

Repo to store project files for task set by QA regarding download + verification of CSV files

## REQUIREMENTS

- pyftpdlib
- pandas
- tkcalendar

## ERROR CODES

The system produces error codes denoting problems with invalid files, which are stored in their respective log files:
- 100 - Empty File
- 200 - Incorrect Header
- 300 - Missing Values
- 400 - Incorrect Number of Rows
- 500 - Invalid Batch ID
- 600 - Too Many Values