import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import *
from ctypes import windll


def getDates():
    today = date.today()
    arr1 = [today.year, today.month, today.day]
    arr2 = cal.get_date().split("/")
    is_valid_date = False

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


if __name__ == '__main__':
    root = Tk()
    root.title("Get Medical Files")
    root.resizable(False, False)
    root.geometry("1500x1000")
    windll.shcore.SetProcessDpiAwareness(1)

    current_date = date.today()

    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month, day=current_date.day, date_pattern="yyyy/m/d")

    Button(root, text="Get Date", command=getDates).place(x=700, y=300)

    #https://stackoverflow.com/questions/72670026/calendar-size-too-small-in-tkcalendar

    dates = Label(root, text="")
    showTxt = Label(root, text="Please select a date for the files you want to see: ", font=("Helvetica bold", 18))

    showTxt.place(x=50, y=20)
    cal.place(x=50, y=80)
    dates.place(x=600, y=400)

    root.mainloop()
