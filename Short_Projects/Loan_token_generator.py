from tkinter import *
import os
from datetime import datetime
import csv
import getpass
from tkinter import messagebox
from tkcalendar import Calendar

system_user = getpass.getuser()
today_month = datetime.today().strftime("%d_%b_%y")    # Sting Date for CSV File Name

# Read Values from Config Text File and create File*
try:

    f = open("tk_config.txt", "r")
    config_input_list = f.read().splitlines()       # Read File Line by Line
    print(config_input_list[0])                     # First Line
    print(config_input_list[1])                     # Second Line

    data_Folder_path = config_input_list[0]         # Store Value of first line to variable
    list_of_banks = str(config_input_list[1]).split(",")            # second line to variable


    # crate a complete file path with data_folder_path varibale *
    conso_file_path = data_Folder_path+'\\'+'HH_BANKIN_'+today_month+'.csv'
    print(conso_file_path+"----output")

    # Create Local on the created path with headers if does not exist
    if not os.path.exists(conso_file_path):
        print("No File") # Create CSV File With Header
        header = ['Name of Analyst', 'Loan Number','Bank Name', 'Account Number (Last 4 Digit)', 'Loan Start Date','Loan End Date','Get Token','Remarks','Submissiontime']
        with open(conso_file_path, 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

except FileNotFoundError as e:          # Handle File Not Found error
    print('File not Found Error ')
    messagebox.showinfo("config error1","Error Config File Not Found--"+str(e))
    exit()
except Exception as e:                  # Handle all other errors
    messagebox.showinfo("config error2","Config File Reading Error--"+str(e))
    exit()

# Functions to set focus on the next element (cursor), each function one element *
def focus1(event):
    txt_loan_number.focus_set()
def focus2(event):
    # set focus on the sem_field box
    opt.focus_set()
def focus3(event):
    txt_account_num.focus_set()
def focus4(event):
    btn_start_date.focus_set()
def focus5(event):
    btn_end_date.focus_set()
def focus6(event):
    txt_remarks.focus_set()
def focus7(event):
    btn_out_put.focus_set()

def focus8(event):
    btn_confirm.focus_set()

# Function for clearing the existing values from all elements on the page *
def clear():
    # clear the content of text entry box
    txt_loan_number.delete(0, END)
    txt_bank_name.delete(0, END)
    txt_account_num.delete(0, END)
    txt_start_date.delete(0, END)
    txt_end_date.delete(0, END)
    txt_out_put.delete(0, END)
    txt_remarks.delete(0, END)

# handle calenders to get the date from external popup to main window **
def start_calender_start_date():                       # 2 Functions
    def print_sel():
        print(cal.selection_get())
        txt_start_date.delete(0, END)                  # Clear Text Box
        txt_start_date.insert(END, cal.selection_get().strftime("%m/%d")) # Insert New Value
        top.destroy()

    top = Toplevel()
    top.lift()
    cal = Calendar(top, font="Arial 14", selectmode='day', year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)

    # Call Print Function on Calender
    Button(top, text="CONFIRM",font="Arial 18", command=print_sel).pack()

def start_calender_end_date():          # Upper Function would be called in main execution**
    def print_sel():
        print(cal2.selection_get())
        txt_end_date.delete(0, END)
        # Set New date to the text box in before destroying
        txt_end_date.insert(END, cal2.selection_get().strftime("%m/%d"))
        top.destroy()

    top = Toplevel()
    top.lift()
    cal2 = Calendar(top,font="Arial 14", selectmode='day', year=2018, month=2, day=5)
    cal2.pack(fill="both", expand=True)
    Button(top, text="CONFIRM", font="Arial 18", command=print_sel).pack()

# Assign all the text box values to variable to generate token and write file **
def insert():
    v_user_name = getpass.getuser()
    v_order_num = txt_loan_number.get()
    v_bank_name = txt_bank_name.get()
    v_account_number = txt_account_num.get()
    v_start_date = txt_start_date.get()
    v_ent_date = txt_end_date.get()
    v_out_put = txt_out_put.get()
    v_remarks = txt_remarks.get()
    v_time = datetime.now()
    output_value = txt_bank_name.get() + " " + "#" + txt_account_num.get() + " " + txt_start_date.get() + "-" + txt_end_date.get()
    print(variable.get())

    # In Insert Function Let See The Validation Conditions **
    if txt_bank_name.get() != variable.get():  # Selected Bank is Not as textbox data
        messagebox.showinfo("Miss Match", "Selected Value for Bank is Not Matching Please Try Again")
        exit()
    if txt_out_put.get() != output_value:  # Selected Bank is Not as textbox data
        messagebox.showinfo("Miss Match", "Out Put Value Generated and Being Submit is Not Matching")
        exit()
    row_to_write = [v_user_name,v_order_num,v_bank_name,v_account_number,v_start_date,v_ent_date,v_out_put,v_remarks,v_time]

    # Insert the code in the csv file
    with open(conso_file_path, 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row_to_write)
    messagebox.showinfo("Success","Successfully Submmited")

    # Clear The Data
    clear()

# MAIN CODE AREA EXECUTION *****

if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("HH - BANKING CHECK LIST")

    # set the configuration of GUI window
    root.geometry("700x400")

    # create a Form label and text boxes **
    lbl_heading = Label(root, text="Form", bg="light green",font=("calibri ", 12))
    lbl_loan_number = Label(root, text="Loan Number", bg="light green",font=("calibri ", 12))
    lbl_bank_name = Label(root, text="Bank Name", bg="light green",font=("calibri ", 12))
    lbl_account_number = Label(root, text="Account Num (4 Digit)", bg="light green",font=("calibri ", 12))
    lbl_start_date = Label(root, text="Loan Start Date", bg="light green",font=("calibri ", 12))
    lbl_end_date = Label(root, text="Loan End Date", bg="light green",font=("calibri ", 12))
    lbl_out_put = Label(root, text="Check Token", bg="light green",font=("calibri ", 12))
    lbl_remarks = Label(root, text="Any Remarks..?", bg="light green",font=("calibri ", 12))

    lbl_heading.grid(row=0, column=1)
    lbl_loan_number.grid(row=1, column=0)
    lbl_bank_name.grid(row=2, column=0)
    lbl_account_number.grid(row=4, column=0)
    lbl_start_date.grid(row=5, column=0)
    lbl_end_date.grid(row=6, column=0)
    lbl_out_put.grid(row=7, column=0)
    lbl_remarks.grid(row=8, column=0)

    # Create Text Boxes or Entry widget and set properties **
    txt_loan_number = Entry(root,font=("calibri ", 12))

    eText = StringVar()
    txt_bank_name = Entry(root,state="readonly", textvariable=eText,font=("calibri ", 12))

    def option_changed(*args):              # Drop Down Option Change Text - Delete Old Set New
        txt_start_date.delete(0, END)
        eText.set(variable.get())

    # Bank Name Selection
    variable = StringVar(root)
    variable.set(list_of_banks[0])
    variable.trace("w", option_changed)
    opt = OptionMenu(root, variable, *list_of_banks)
    opt.config(width=18,font=('Helvetica', 12))
    opt.grid(row=3, column=1)

    # Account Number  entry set the control to accept only 4 digits **
    entry_text = StringVar(root)
    txt_account_num = Entry(root,font=("calibri ", 12),textvariable = entry_text)

    def character_limit(entry_text):
        if len(entry_text.get()) > 4 or  entry_text.get().isalpha():
            entry_text.set(entry_text.get()[-1])

    entry_text.trace("w", lambda *args: character_limit(entry_text))

    # Start Date and End Date - When we will call function on command 2 functions get executed
    # We had seen above there was a inner function in start date and end date which destroy calender
    # Line 82 Line 87

    txt_start_date = Entry(root,font=("calibri ", 12))
    btn_start_date = Button(root, text="Get Date", fg="Black",bg="gray75", command=start_calender_start_date,font=("calibri ", 8))
    btn_start_date.grid(row=5, column=2,ipadx="1",padx=(15,15),pady=(5,5))

    # End Date
    txt_end_date = Entry(root,font=("calibri ", 12))
    btn_end_date = Button(root, text="Get Date", fg="Black",bg="gray75", command=start_calender_end_date,font=("calibri ", 8))
    btn_end_date.grid(row=6, column=2,ipadx="1",padx=(15,15),pady=(5,5))

    txt_out_put = Entry(root,font=("calibri ", 12))
    txt_remarks = Entry(root,font=("calibri ", 12))

    # whenever the enter key is pressed on a entry widget
    txt_loan_number.bind("<Return>", focus1)
    txt_bank_name.bind("<Return>", focus2)
    txt_account_num.bind("<Return>", focus3)
    txt_start_date.bind("<Return>", focus4)
    txt_end_date.bind("<Return>", focus5)
    txt_out_put.bind("<Return>", focus6)

    # grid method is used for placing the widgets at respective positions
    # in table like structure .
    txt_loan_number.grid(row=1, column=1, ipadx="10",pady=(5,5))
    txt_bank_name.grid(row=2, column=1, ipadx="10",pady=(5,5))
    txt_account_num.grid(row=4, column=1, ipadx="10",pady=(5,5))
    txt_start_date.grid(row=5, column=1, ipadx="10",pady=(5,5))
    txt_end_date.grid(row=6, column=1, ipadx="10",pady=(5,5))
    txt_out_put.grid(row=7, column=1, ipadx="15",pady=(5,5))
    txt_remarks.grid(row=8, column=1, ipadx="10",pady=(5,5))

    # [BANK NAME][SPACE][HASH SYMBOL][LAST FOUR DIGIT OF ACCOUNT NUMBER][SPACE]MM/DD[HYPHEN]MM/DD

    def create_output():
        txt_out_put.delete(0, END)
        output_value = txt_bank_name.get() + " " + "#" + txt_account_num.get() + " " + txt_start_date.get() + "-" + txt_end_date.get()
        txt_out_put.insert(END,output_value) # Token is the text output

    # Function Create Output is used to crate token
    btn_out_put = Button(root, text="Create Token", fg="Black",bg="gray75", command=create_output,font=("calibri ", 12))
    btn_out_put.grid(row=9, column=0,ipadx="10",pady=(25,25))

    btn_confirm = Button(root, text="Submit Data", fg="Black",bg="gray75", command=insert,font=("calibri ", 12))
    btn_confirm.grid(row=9, column=1,ipadx="10",pady=(25,25))

    # start the GUI
    root.mainloop()
