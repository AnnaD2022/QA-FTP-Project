import tkinter 
import tkinter.messagebox
from tkinter import *
from tkcalendar import Calendar
from datetime import date


def getDates():
    dates.config(text="Current date " + cal.get_date())

if __name__ == '__main__':
    root = Tk()
    root.title("Hello!")

    current_date = date.today()

    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month, day=current_date.day)

    Button(root, text="Get Date", command=getDates).pack(pady=20)


    dates = Label(root, text="")
    cal.pack(pady=20)
    dates.pack(pady=5, padx=30)

    root.mainloop()
