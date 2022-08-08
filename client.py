from ftplib import FTP
import re

address = ""
port = 2121
user = ""
password = ""

##Create FTP client instance and connect/login
ftp = FTP()
ftp.connect(address, port)
ftp.login(user, password)

##List files, store in list
filenames = []
ftp.retrlines('NLST', filenames.append)
print(filenames)

##Iterate through filenames, read files that end in .csv
simple_csv_pattern = r'.*\.csv'
for filename in filenames:
    filename = filename.lower()
    if re.match(simple_csv_pattern, filename):
        ftp.retrbinary('RETR ' + filename, open('./downloads/for_checking/' + filename, 'wb+').write)
        f = open('./downloads/downloaded.txt', 'a')
        f.write(filename + "\n")
        f.close()

ftp.close()

##TODO:
#loop all filenames returned
##download all valid filenames into to_check
##download invalid filenames not in downloaded.txt into to_check
##log downloads

##TODO - regex .csv, regex full valid title.csv -> download into separate folders
##TODO - check filenames against existing list --> only download new files for the given day
##TODO - figure out downloaded protocol numbers to denote bad filename
##TODO - sort file hierarchy in downloads -> communicate this to file handler
##TODO - make function to call that auto downloads given day's files
##TODO - add error handling for ftp connections
##TODO - make engine.py to be called from GUI -- needs to accept CLI for cronjob

