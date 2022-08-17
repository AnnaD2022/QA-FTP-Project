import tkinter
import tkinter.messagebox
import pandas as pd
import os
import client

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import *
from ctypes import windll

#def checkDate():
#    filenames = []
#    dates = []
#
#    path = "./temp" #esj replaced: C:/Users/delegate119/Documents/GitHub/QA-FTP-Project/temp with thepath name seen. This is because the removed path name was specific to the mian.py creators device and was not recognised when run on other devices
#    for filename in os.listdir(path):
#        if filename.endswith('.csv'):
#            filename = filename.replace("MED_DATA_", "")
#            try:
#                year = filename[0:4]
#                month = int(filename[5:6])
#                day = int(filename[6:8])
#                temp_date = year + "/" + str(month) + "/" + str(day)
#                dates.append(temp_date)
#                print(temp_date)
#                filenames.append(filename)
#            except:
#                continue
#    checkDate.filenames = filenames
#    checkDate.dates = dates
#    checkDate.path = path
#    # The above lines enable the filenames and dates arrays to be accessed in the checkDate test

##Function to check whether selected date is valid (i.e. not after current date)
def dateLogic():
    today = date.today()
    arr1 = [today.year, today.month, today.day]
    arr2 = cal.get_date().split("/")
    is_valid_date = False

    ##Check date logic
    for y, x in enumerate(arr1):
        if x > int(arr2[y]):
            is_valid_date = True
            break
        elif y == len(arr1) - 1 and x >= int(arr2[y]):
            is_valid_date = True
            break

    ##If not valid date, show error messagebox
    if not is_valid_date:
        messagebox.showerror("Error", "You cannot select a date later than today!")
        return
    ##Else update date on GUI to show selected, call into ftp client with required date
    else:
        dates.config(text="Current date " + cal.get_date())
        downloaded_count = client.download_files(arr2[0], arr2[1], arr2[2])
        if downloaded_count >= 0:
            number_downloaded.config(text="Number of files successfully downloaded: " + str(downloaded_count))
        else:
            number_downloaded.config(text="Error occurred in file transfer process. Retry.")


if __name__ == '__main__':
    root = Tk()
    root.title("Get Medical Files")
    root.resizable(False, False)
    root.geometry("1500x1000")
    root.configure(bg="#DFFEFF")
    windll.shcore.SetProcessDpiAwareness(1)

    root.tk.call('tk', 'scaling', 2.5)

    current_date = date.today()

    dt1 = date(2010, 12, 12)
    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month, day=current_date.day, date_pattern="yyyy/m/d",
                   mindate=dt1)

    Button(root, text="Get Files", command=dateLogic).place(x=525, y=210)

    dates = Label(root, text="")
    number_downloaded = Label(root, text="")
    showTxt = Label(root, text="Please select a date for the files you want to see: ", font=("Helvetica bold", 10),
                    bg="#DFFEFF")

    showTxt.place(x=35, y=35)
    cal.place(x=50, y=100)
    dates.place(x=600, y=400)
    number_downloaded.place(x=500, y=500)

    #checkDate()

    root.mainloop()
