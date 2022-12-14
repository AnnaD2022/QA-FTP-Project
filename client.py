#from ftplib import FTP
import ftplib
import re

address = "127.0.0.1" ##Local machine by default
port = 2121
user = "user"
password = "verysecure123"

##Function to be called to download all files from requested date; returns -1 if an error occurred, otherwise the integer returned
##indicates the number of new files downloaded
def download_files(year, month, day):
    ##Try-except loop to handle errors
    try:
        ##Create FTP client instance and connect/login
        ftp = ftplib.FTP()
        ftp.connect(address, port)
        ftp.login(user, password)

        ##List files, store in list
        filenames = []
        ftp.retrlines('NLST', filenames.append)

        ##Check whether each filename is valid; if it is valid, check if it is for the requested day and whether it has already been downloaded
        ##if not valid, add to log of files not to download if not already there
        downloaded_count = 0
        valid_csv_pattern = r'MED_DATA_[0-9]{14}.CSV'
        for filename in filenames:
            filename = filename.upper()
            ##Check if filename matches expected pattern
            if re.match(valid_csv_pattern, filename):
                ##Check if file is from requested date
                splitname = filename.split('_')
                if (int(splitname[2][0:4]) == int(year)) and (int(splitname[2][4:6]) == int(month)) and (int(splitname[2][6:8]) == int(day)):
                    ##Check if already downloaded
                    downloaded_flag = False
                    f = open('./files/downloaded_log.txt', 'r')
                    for line in f:
                       if line.strip() == filename:
                            downloaded_flag = True
                    f.close()
                    ##If not already downloaded, download into "to_check" area and log
                    if not downloaded_flag:
                        ftp.retrbinary('RETR ' + filename, open('./files/to_check/' + filename, 'wb+').write)
                        f = open('./files/downloaded_log.txt', 'a')
                        f.write(filename + "\n")
                        f.close()
                        downloaded_count += 1
            else:
                ##Add to log of files to not download if not already in log
                logged_flag = False
                f = open('./files/ignored_log.txt', 'r')
                for line in f:
                    if line.strip() == filename:
                            logged_flag = True
                f.close()
                if not logged_flag:
                    f = open('./files/ignored_log.txt', 'a')
                    f.write(filename + "\n")
                    f.close()
        ftp.close()
        return downloaded_count
    ##Handle FTP-specific errors
    except ftplib.all_errors as e:
        print("Error occurred in authenticating. " + str(e))
        return -1
    ##Handle all other errors
    except Exception:
        print("Error occurred.")
        return -1

