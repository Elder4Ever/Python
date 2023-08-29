import os
import string
import json
import random
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from  tkinter import ttk
import sqlite3
from sqlite3 import Error
from datetime import date
from datetime import datetime
import webbrowser

global filename
filename = 'C:/Users/BrandonElder/Documents/GitHub/Python/Basic Gui/settings.json'
title = "Brandon's Password Generator"
version = "Version: Dev-Alpha-1.0"
lic = "This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license. This is a place holder until i get a license."

def about_screen():

    def about_on_closing():
        root.deiconify()
        about.destroy()
    root.withdraw()
    about = Tk()
    about.resizable(False,False)
    about.geometry('400x300')
    about.title("About")

    w = Label(about, text=title,font=("Arial", 18))
    w.pack()

    ver = Label(about, text=version, font=("Arial", 12))
    ver.pack()

    license = Label(about, text=lic, font=("Arial", 10), wraplength=350, justify="center")
    license.pack(padx=20, pady=40)
    about.protocol("WM_DELETE_WINDOW",about_on_closing)
    about.mainloop()

def local_data_screen():

    def destroy_data():
        if datatable.winfo_ismapped() == 1:
            datatable.destroy()


    def submit_entry():
        Email = eE.get()
        Password = eP.get()
        Name = eN.get()
        Url = eU.get()
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        entry = (None, Email, Password, Name, Url, now)
        conn = sqlite3.connect(dataf['settings']['data_file'])
        db_cursor = conn.cursor()
        sql = """INSERT INTO account_info(account_id, email, password, name, url, created_date) values(?, ?, ?, ?, ?, ?)"""
        db_cursor.execute(sql, entry)
        conn.commit()
        conn.close()
        print('entry added')
        destroy_data()
        dataset()
        

    def new_entry():
        global eE
        global eP
        global eN
        global eU
        global submitEntry
        eE = Entry(data_screen)
        eE.insert(0, 'Enter Email... ')
        eE.pack(pady=5)
        eP = Entry(data_screen)
        eP.insert(0, 'Enter Password... ')
        eP.pack(pady=5)
        eN = Entry(data_screen)
        eN.insert(0, 'Enter a Association Name... ')
        eN.pack(pady=5)
        eU = Entry(data_screen)
        eU.insert(0, 'Enter URL... ')
        eU.pack(pady=5)
        submitEntry = Button(data_screen, text='Submit Entry', fg='black', font=("Arial", 10), height = 1, width = 13, command=submit_entry)
        submitEntry.pack(pady=5, padx=20)
        cancelEntry = Button(data_screen, text='Cancel Entry', fg='black', font=("Arial", 10), height = 1, width = 13, command=None)
        cancelEntry.pack(pady=5, padx=20)
        
    
    def del_entry():
        selected=datatable.focus()
        values = datatable.item(selected,'values')
        cd = values[4]
        conn = sqlite3.connect(dataf['settings']['data_file'])
        db_cursor = conn.cursor()
        sql = """DELETE FROM account_info WHERE created_date='%s'""" % cd
        print(sql)
        db_cursor.execute(sql)
        conn.commit()
        conn.close()
        destroy_data()
        dataset()
        
    def dataset():
        global datatable
        datatable = ttk.Treeview(table_frame)
        datatable['columns'] = ('user_email', 'password', 'name', 'url', 'created_date')
        datatable.column("#0", width=0,  stretch=NO)
        datatable.column("user_email",anchor=CENTER,width=150)
        datatable.column("password",anchor=CENTER,width=150)
        datatable.column("name",anchor=CENTER,width=150)
        datatable.column("url",anchor=CENTER,width=150)
        datatable.column("created_date",anchor=CENTER,width=150)

        datatable.heading("#0",text="",anchor=CENTER)
        datatable.heading("user_email",text="Email",anchor=CENTER)
        datatable.heading("password",text="Password",anchor=CENTER)
        datatable.heading("name",text="Name",anchor=CENTER)
        datatable.heading("url",text="Url",anchor=CENTER)
        datatable.heading("created_date",text="Created Date",anchor=CENTER)
        global dataf
        df = open(filename,'r+')
        dataf = json.load(df)
        rows = sqlite3.connect(dataf['settings']['data_file']).execute("SELECT * FROM account_info").fetchall()
        for row in rows:
            #print()
            datatable.insert(parent='',index='end', text='', values=(row[1],row[2],row[3],row[4],row[5]))

        df.seek(0)
        df.truncate()
        df.write(json.dumps(dataf))
        df.close()
    
        datatable.pack()


        

    def copyPass():
        selected=datatable.focus()
        values = datatable.item(selected,'values')
        saved_pass = values[1]
        data_screen.clipboard_clear()
        data_screen.clipboard_append(saved_pass)

    def copyEmail():
        selected=datatable.focus()
        values = datatable.item(selected,'values')
        saved_email = values[0]
        data_screen.clipboard_clear()
        data_screen.clipboard_append(saved_email)

    def goToWeb():
        selected=datatable.focus()
        values = datatable.item(selected,'values')
        saved_url = values[3]
        webbrowser.open(saved_url)
    

    m = Menu(root, tearoff = 0)
    m.add_command(label ="Go To URL", command=goToWeb)
    m.add_command(label ="Copy Email", command=copyEmail)
    m.add_command(label ="Copy Password", command=copyPass)
    m.add_command(label ="Reload (DNW)")
    m.add_separator()
    m.add_command(label ="Rename (DNW)")

    def do_popup(event):
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()
    
    
    global datatable
    data_screen = Tk()
    data_screen['bg'] = 'white'
    data_screen.geometry("800x500")
    data_screen.title('Password Database')
    
    data_screen.bind("<Button-3>", do_popup)
    
    menubar = Menu(data_screen)
  
    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='Exit', command = data_screen.destroy)
    actions = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Actions', menu = actions)
    actions.add_command(label ='Create New Entry', command = new_entry)
    actions.add_separator()
    actions.add_command(label ='Delete Selected', command = del_entry)
    actions.add_command(label ='Edit Selected', command = None)
    actions.add_separator()
    actions.add_command(label ='Update Table', command = None)
    help = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help)
    help.add_command(label ='About', command = about_screen)
    data_screen.config(menu = menubar)

    global table_frame
    table_frame = Frame(data_screen)
    table_frame.pack()
    
    dataset()
    
    data_screen.mainloop()
        
def settings():
    if os.path.exists(filename):
        
        root.withdraw()

        def settings_on_closing():
            root.deiconify()
            settings.destroy() 

        def save_settings():
            f = open(filename,'r+')
            data = json.load(f)
            data['settings']['encrypted'] = False
            data['settings']['count'] = 0
            data['settings']['lowercase'] = val1.get()
            data['settings']['uppercase'] = val2.get()
            data['settings']['numbers'] = val3.get()
            data['settings']['special'] = val4.get()
            f.seek(0)
            f.truncate()
            f.write(json.dumps(data))
            savedLabel.configure(text="Saved")
        
        settings = Toplevel()
        settings.resizable(False,False)
        settings.geometry('500x300')
        settings.title("Settings")

        global lowerbox
        global upperbox
        global numberbox
        global specialbox
        global Strength
        Strength = []

        f = open(filename,'r+')
        data = json.load(f)
        lower = data['settings']['lowercase']
        upper = data['settings']['uppercase']
        num = data['settings']['numbers']
        spec = data['settings']['special']
        
        if lower == 1:
            val1 = IntVar(value=1)
            lowerbox = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            Strength = Strength + lowerbox
        else:
            val1 = IntVar(value=0)

        if upper == 1:
            val2 = IntVar(value=1)
            upperbox = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            Strength = Strength + upperbox
        else:
            val2 = IntVar(value=0)

        if num == 1:
            val3 = IntVar(value=1)
            numberbox = ['1','2','3','4','5','6','7','8','9','0']
            Strength = Strength + numberbox
        else:
            val3 = IntVar(value=0)
        
        if spec == 1:
            val4 = IntVar(value=1)
            specialbox = ['!','@','#','#','$','%','^','&','*','(',')']
            Strength = Strength + specialbox
        else:
            val4 = IntVar(value=0)

        global lowercase
        global uppercase
        global number
        global special
        StrengthLabel = Label(settings, text='Strength', fg="Black", font="Arial 12 bold")
        StrengthLabel.pack(padx=10, anchor=NW)
        lowercase = Checkbutton(settings, text = "Lower Case", variable = val1, onvalue = 1, offvalue = 0, height = 1, width = 10)
        uppercase = Checkbutton(settings, text = "Upper Case", variable = val2, onvalue = 1, offvalue = 0, height = 1, width = 10)
        number = Checkbutton(settings, text = "Numbers", variable = val3, onvalue = 1, offvalue = 0, height = 1, width = 8)
        special = Checkbutton(settings, text = "Special Characters", variable = val4, onvalue = 1, offvalue = 0, height = 1, width = 15)
        
        lowercase.pack(anchor=NW) 
        uppercase.pack(anchor=NW) 
        number.pack(anchor=NW) 
        special.pack(anchor=NW)
        
        savedLabel = Label(settings, fg="Green", font=("Arial", 12))
        savedLabel.pack(side = BOTTOM)
        
        savebutton = Button(settings, text='Save', fg='black', font=("Arial", 20), height = 1, width = 10, command=save_settings)
        savebutton.pack(side = BOTTOM)

        settings.protocol("WM_DELETE_WINDOW",settings_on_closing)
        settings.mainloop()
    else:
        print('File does not exist')

def print_value(value):
    return value

def on_closing():
     root.clipboard_clear()
     root.destroy()

def securePass():

    password = ""
    passlen = s.get()
    Strength = []
    while len(password) != passlen:
        f = open(filename,'r+')
        data = json.load(f)
        lower = data['settings']['lowercase']
        upper = data['settings']['uppercase']
        num = data['settings']['numbers']
        spec = data['settings']['special']
        
        if lower == 1:
            lowerbox = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            Strength = Strength + lowerbox
        else:
            lowerbox = []

        if upper == 1:
            upperbox = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            Strength = Strength + upperbox
        else:
            upperbox = []

        if num == 1:
            numberbox = ['1','2','3','4','5','6','7','8','9','0']
            Strength = Strength + numberbox
        else:
            numberbox = []

        if spec == 1:
            specialbox = ['!','@','#','#','$','%','^','&','*','(',')']
            Strength = Strength + specialbox
        else:
            specialbox = []

        strength = Strength
        letters = random.choice(strength)
        password = password + letters
    root.clipboard_clear()
    root.clipboard_append(password)
    w.configure(text=password)
    print(password)
    return password

def open_file():
    file = filedialog.askopenfilename()
    fob=open(file,'r+')
    f = open(filename,'r+')
    data = json.load(f)
    data['settings']['data_file'] = fob.name
    f.seek(0)
    f.truncate()
    f.write(json.dumps(data))
    #file = filedialog.askopenfile()
    #print(file.read())

def file_save():
    file = filedialog.asksaveasfilename(filetypes=[("SQLite3 Database File", ".db")], defaultextension=".db")
    fob=open(file,'w')
    fob.write("")
    fob.close()
    def sql_connection():
        try:
            con = sqlite3.connect(fob.name)
            return con
        except Error:
            print(Error)
    def sql_table(con):
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE account_info(account_id integer PRIMARY KEY, email text, password text, name text, url text, created_date text)")
        con.commit()
    con = sql_connection()
    sql_table(con)

root = Tk()
root.configure(background='grey')
sw = int(root.winfo_screenwidth() / 2)
sh = int(root.winfo_screenheight() / 3)
screen_resolution = str(sw)+'x'+str(sh)
print(screen_resolution)
root.title(title)
root.geometry(screen_resolution)
#root.resizable(False,False)#

menubar = Menu(root)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New Local Database', command = file_save)
file.add_command(label ='Open Local Database', command = open_file)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Settings', command = settings)
view = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='View', menu = view)
view.add_command(label ='Local Database', command = local_data_screen)
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help)
help.add_command(label ='About', command = about_screen)
root.config(menu = menubar)


p = securePass

w = Label(root, text="Click Generate to Start",font=("Arial", 30))
w.configure(background="grey")
w.pack(pady=10)

s = Scale(root, length=400,width=15, from_=6, to=30,highlightthickness=0,troughcolor='#73B5FA', tickinterval=24,sliderrelief='flat',activebackground='#1065BF', orient=HORIZONTAL,command=print_value)
s.configure(background='grey')
s.pack(pady=20)

redbutton = Button(root, text='Generate', fg='black', font=("Arial", 20), height = 1, width = 15, command=securePass)
redbutton.pack(pady=10)

warn = Label(root, text="**Generated Password Automatically Copies to Clipboard**", fg="pink", font=("Arial", 9))
warn.configure(background="grey")
warn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
