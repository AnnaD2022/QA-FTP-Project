import tkinter
import tkinter.messagebox
import pandas as pd
import os

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import *
from ctypes import windll


def checkDate():
    filenames = []
    dates = []

    path = "C:/Users/delegate119/Documents/GitHub/QA-FTP-Project/temp"
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


def dateLogic():
    today = date.today()
    arr1 = [today.year, today.month, today.day]
    arr2 = cal.get_date().split("/")
    is_valid_date = False

    print(cal.get_date())

    for y, x in enumerate(arr1):
        if x > int(arr2[y]):
            is_valid_date = True
            break

        elif y == len(arr1) - 1 and x >= int(arr2[y]):
            is_valid_date = True
            break

    if not is_valid_date:
        messagebox.showerror("Error", "You cannot select a date later than today!")
        return
    dates.config(text="Current date " + cal.get_date())

    if str(cal.get_date()) not in dates:
        messagebox.showerror("Error", "There is no file for that selected date!")


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
    showTxt = Label(root, text="Please select a date for the files you want to see: ", font=("Helvetica bold", 10),
                    bg="#DFFEFF")

    showTxt.place(x=35, y=35)
    cal.place(x=50, y=100)
    dates.place(x=600, y=400)

    checkDate()

    root.mainloop()
