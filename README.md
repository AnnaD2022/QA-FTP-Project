# QA File Transfer, Validation and Storage Project

This project seeks to fulfil the requirements, as laid out in the specification provided, in order to produce a system that downloads requested csv files containing medical research data from an external FTP server, validate the format and contents of the files, and stores them in a calendar-based directory system. To do this, we have used python to create:
1. A GUI, which is used to request files for a particular date and report any errors with those files to the user.
2. An FTP server to serve the files.
3. An FTP client script used by the main GUI script of the program to request files from a specified date that match a valid file name format.
4. A script that checks the contents of the file meet the requirements laid out in the specification and fixes errors where possible.  This script creates an "info" file which is stored alongside each csv file to report any errors encountered, and sorts the files into an archive system based on their validity and the date on which they were created.
5. A thorough testing suite, to ensure the robustness of our system.

## REQUIREMENTS

- pyftpdlib
- pandas
- tkcalendar
