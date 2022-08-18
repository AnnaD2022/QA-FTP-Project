import client

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import *
from ctypes import windll

##Function to check whether selected date is valid (i.e. not after current date)
def date_logic():
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
        dates.config(text="Current date selected: " + cal.get_date())
        downloaded_count = client.download_files(arr2[0], arr2[1], arr2[2])
        if downloaded_count >= 0:
            number_downloaded.config(text="Number of files successfully downloaded: " + str(downloaded_count))
        else:
            number_downloaded.config(text="Error occurred in file transfer process. Retry.")

##Main GUI script
if __name__ == '__main__':
    ##Initialise Tk
    root = Tk()
    root.title("Get Medical Files")
    root.resizable(False, False)
    root.geometry("1500x1000")
    root.configure(bg="#DFFEFF")
    windll.shcore.SetProcessDpiAwareness(1)

    root.tk.call('tk', 'scaling', 2.5)

    current_date = date.today()
    
    ##Initialise GUI components
    dt1 = date(2010, 12, 12)
    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month, day=current_date.day, date_pattern="yyyy/m/d",
                   mindate=dt1)

    Button(root, text="Get Files", command=date_logic).place(x=525, y=210)

    dates = Label(root, text="No date selected yet.")
    number_downloaded = Label(root, text="No transfer attempt yet.")
    show_txt = Label(root, text="Please select a date for the files you want to see: ", font=("Helvetica bold", 10),
                    bg="#DFFEFF")

    show_txt.place(x=35, y=35)
    cal.place(x=50, y=100)
    dates.place(x=750, y=400, anchor="center")
    number_downloaded.place(x=750, y=500, anchor="center")

    root.mainloop()
