# checkDate: removed main.py function

## Reason for removal:
The checkDate function implemented input file handling logic which has been implemented and integrated as part of the validate_data.py script thus has been rendered redundant.

## Function descriptor
-	Iterating through all of the files which have been stored in the designated files folder in our repo
-	If the file has type '.csv', then it replaces the file name with “Med_DATA_”
-	Year, month and day are abstracted from the filename, formatted as a date by inserting '/',  the date and file name are then added to the respective arrays

## The function:
def checkDate():
    filenames = []
    dates = []

    path = "./temp" #esj replaced: C:/Users/delegate119/Documents/GitHub/QA-FTP-Project/temp with thepath name seen. This is because the removed path name was specific to the mian.py creators device and was not recognised when run on other devices
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            filename = filename.replace("MED_DATA_", "")
            try:
                year = filename[0:4]
                month = int(filename[5:6])
                day = int(filename[6:8])
                temp_date = year + "/" + str(month) + "/" + str(day)
                dates.append(temp_date)
                print(temp_date)
                filenames.append(filename)
            except:
                continue
    checkDate.filenames = filenames
    checkDate.dates = dates
    checkDate.path = path
    # The above lines enable the filenames and dates arrays to be accessed in the checkDate test

## Test plan:
|Test|Inputs|Expected Outcome| pass/fail | links |
|----|------|----------------|-----------|-------|
|test_cd1 | Contents of the 'temp' repository folder | True - number of entries in filenames array should match the number of csv files in the temp folder | passes 13/08/2022| [Tested code](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br><br> [Folder containing all inputs](https://github.com/AnnaD2022/QA-FTP-Project/tree/main/temp) <br><br>  [Unit test file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_main_checkDate.py) |
|test_cd2 | Contents of the 'temp' repository folder | True - number of entries in dates array should match the number of csv files in the temp folder | passes 13/08/2022| [Tested code](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br><br> [Folder containing all inputs](https://github.com/AnnaD2022/QA-FTP-Project/tree/main/temp) <br><br>  [Unit test file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_main_checkDate.py) |

### Test
[Test created and passing before function removal](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/tests/redundant_tests/test_main_checkDate.py)