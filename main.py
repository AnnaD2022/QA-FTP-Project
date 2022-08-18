import client
import validate_file

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import *
from ctypes import windll

##Function to check whether selected date is valid (i.e. not after current date), call functions to fetch and validate files, and display all information to the user
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
    ##Else update date on GUI to show selected, call into ftp client with required date, show number of files downloaded, validate files if needed
    else:
        dates.config(text="Current date selected: " + cal.get_date())
        downloaded_count = client.download_files(arr2[0], arr2[1], arr2[2])
        ##If any files were downloaded, update GUI and validate them
        if downloaded_count >= 0:
            number_downloaded.config(text="Number of files successfully downloaded: " + str(downloaded_count))
            files_written = validate_file.main()
            ##Handle displaying downloaded files and their info.txt files
            info_messages_text = ""
            for file in files_written:
                info_messages_text += "File downloaded: "
                info_messages_text += file
                info_messages_text += "\nValidation Code: "
                info_filepath = file.replace(".csv.","")
                info_filepath += "_info.txt"
                f = open(info_filepath, 'r')
                error_line = f.readline().strip()
                f.close()
                ##Split error_line into smaller sections to display better - max width of 120 - improves readability for user
                index = 0
                while index < len(error_line):
                    if index + 100 < len(error_line):
                        ##Code below starts at index + 100, searches forwards and backwards for closest " " character, uses this for line splits (if +-20 from start position)
                        new_index = index + 100
                        chosen_flag = False
                        ##Check fowards
                        forwards_index = new_index
                        backwards_index = new_index
                        ##Check next index is in range, check current is not space, check current is less than 20 ahead (max length limit -> could be long word)
                        while forwards_index + 1 < len(error_line) and error_line[forwards_index] != " " and forwards_index < new_index + 20:
                            forwards_index += 1
                        ##If string maxes out, use entire rest of string
                        if forwards_index == len(error_line):
                            new_index = len(error_line)
                            chosen_flag = True
                        ##Check backwards
                        while error_line[backwards_index] != " " and backwards_index > new_index - 20:
                            backwards_index -= 1
                        ##Choose either forwards or backwards index, whichever is less distance from new_index; if same, just use new_index with a "-" to denote split over lines
                        if not chosen_flag:
                            if (new_index - backwards_index < forwards_index - new_index):
                                new_index = backwards_index
                                chosen_flag = True
                            elif (forwards_index - new_index < new_index - backwards_index):
                                new_index = forwards_index
                                chosen_flag = True
                        ##Handle text and splicing
                        info_messages_text += error_line[index:new_index]
                        if not chosen_flag:
                            info_messages_text += "-"
                        info_messages_text += "\n"
                        index = new_index
                    else:
                        info_messages_text += error_line[index:]
                        index = len(error_line) 
                info_messages_text += "\n"
            ##Display correct message on GUI
            if len(info_messages_text) != 0:
                info_messages.config(text=info_messages_text.strip())
            else:
                info_messages.config(text="No files downloaded.")
        else:
            number_downloaded.config(text="Error occurred in file transfer process. Retry.")
            info_messages.config(text="No files downloaded.")

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
    
    ##Initialise GUI components, place them in appropriate positions
    dt1 = date(2010, 12, 12)
    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month, day=current_date.day, date_pattern="yyyy/m/d",
                   mindate=dt1)

    Button(root, text="Get Files", command=date_logic).place(x=525, y=210)

    dates = Label(root, text="No date selected yet.")
    number_downloaded = Label(root, text="No transfer attempt yet.")
    show_txt = Label(root, text="Please select a date for the files you want to see: ", font=("Helvetica bold", 10),
                    bg="#DFFEFF")
    info_messages = Label(root, text="No files downloaded.")

    show_txt.place(x=35, y=35)
    cal.place(x=50, y=100)
    dates.place(x=750, y=400, anchor="center")
    number_downloaded.place(x=750, y=500, anchor="n")
    info_messages.place(x=750, y=600, anchor="n")

    root.mainloop()
