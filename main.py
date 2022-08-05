import tkinter 
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import *


def getDates():
    dates.config(text="Current date " + cal.get_date())
    today = date.today()
    arr1 = [today.year, today.month, today.day]
    arr2 = cal.get_date().split("/")
    is_valid_date = False

    for y,x in enumerate(arr1):
        if x > int(arr2[y]):
            is_valid_date = True
            break

        elif y == len(arr1) - 1 and x >= int(arr2[y]):
            is_valid_date = True
            break

    if not is_valid_date:
        messagebox.showerror("Error", "You cannot select a date later than today!")



if __name__ == '__main__':
    root = Tk()
    root.title("Hello!")

    current_date = date.today()

    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month, day=current_date.day, date_pattern="yyyy/m/d")

    Button(root, text="Get Date", command=getDates).pack(pady=20)


    dates = Label(root, text="")
    cal.pack(pady=20)
    dates.pack(pady=5, padx=30)

    root.mainloop()
