import os
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
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


global filename

filename = 'C:/Users/BrandonElder/Documents/GitHub/Python/Basic Gui/settings.json'
title = "Brandon's Password Generator"
version = "Version: Dev-Alpha-2.0"
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

def license_screen():
    def handle_click(event):
        lk.delete(0, END)


    def apply_license():
        df = open(filename,'r+')
        dataf = json.load(df)
        if license_check(lk.get()) == True:
            dataf['settings']['license_key'] = lk.get()
            print('Good To Go')
            lb.destroy()
            lk.destroy()
            titleLabel.destroy()
            valitityLabel = Label(ls, text="License is Valid", fg='Green', font=("Arial", 14))
            valitityLabel.pack()
            df.seek(0)
            df.truncate()
            df.write(json.dumps(dataf))
            df.close()
        else:
            print('Not Valid')
    
    global lk

    
    #data['settings']['license_key'] = "0"
    ls = Tk()
    ls.resizable(False,False)
    ls.geometry('350x100')

    ls.title("License")

    titleLabel = Label(ls, text="Enter License Key", font=("Arial", 14))
    titleLabel.pack()
    
    lk = Entry(ls, width='30',font=("Arial", 12), fg="lightgray")
    lk.insert(0,'License Key')
    lk.bind("<1>", handle_click)
    lk.pack()

    

    lb = Button(ls, text='Apply License', width='15',font=("Arial", 9), fg="black", command=apply_license)
    lb.pack()
    df = open(filename,'r+')
    dataf = json.load(df)
    if license_check(dataf['settings']['license_key']):
        lb.destroy()
        lk.destroy()
        titleLabel.destroy()
        valitityLabel = Label(ls, text="License is Valid", fg='Green', font=("Arial", 14))
        valitityLabel.pack()
    df.seek(0)
    df.truncate()
    df.write(json.dumps(dataf))
    df.close()

    ls.mainloop()

def license_check(key):
    license_file = 'C:/Users/BrandonElder/Documents/GitHub/Python/Basic Gui/license.db'
    conn = sqlite3.connect(license_file)
    db_cursor = conn.cursor()
    sql = """SELECT * FROM licenses"""
    rows = db_cursor.execute(sql).fetchall()
    for row in rows:
        if key == row[1]:
            print("TRUE")
            return True

    conn.commit()
    conn.close()

def local_data_screen():
    def toggle_hide_pass():
        f = open(filename,'r+')
        data = json.load(f)
        if data['settings']['pass_hidden'] == 1:
            data['settings']['pass_hidden'] = 0
        elif data['settings']['pass_hidden'] == 0:
            data['settings']['pass_hidden'] = 1
        f.seek(0)
        f.truncate()
        f.write(json.dumps(data))
        f.close()
        destroy_data()
        dataset()
            
    def encoded(passwd):
        letter1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']    
        letter6 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter7 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter8 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter9 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        letter10 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','#','$','%','^','&','*','(',')']
        salt1 = random.choice(letter1)
        salt2 = random.choice(letter2)
        salt3 = random.choice(letter3)
        salt4 = random.choice(letter4)
        salt5 = random.choice(letter5)
        salt6 = random.choice(letter6)
        salt7 = random.choice(letter7)
        salt8 = random.choice(letter8)
        salt9 = random.choice(letter9)
        salt10 = random.choice(letter10)
        true_salt_front = salt1+salt2+salt3+salt4+salt5
        true_salt_back = salt6+salt7+salt8+salt9+salt10
        salted_pass = true_salt_front+passwd+true_salt_back
        data = bytes(salted_pass, encoding='utf-8')
        encode = base64.b64encode(data)
        print(true_salt_front)
        print(true_salt_back)
        print(salted_pass)
        print(encode)
        return encode
    
    def decoded(passwd):
        decoded_bytes = base64.b64decode(passwd).decode()
        decode_pass = decoded_bytes[5:]
        decode_pass_back = decode_pass[:-5]
        return decode_pass_back
    
    def destroy_data():
        if datatable.winfo_ismapped() == 1:
            datatable.destroy()

    def submit_entry():
        Email = eE.get()
        Password = eP.get()
        Name = eN.get()
        Url = eU.get()
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        entry = (None, Email, encoded(Password), Name, Url, now)
        conn = sqlite3.connect(dataf['settings']['data_file'])
        db_cursor = conn.cursor()
        sql = """INSERT INTO account_info(account_id, email, password, name, url, created_date) values(?, ?, ?, ?, ?, ?)"""
        db_cursor.execute(sql, entry)
        conn.commit()
        conn.close()
        print('entry added')
        destroy_data()
        dataset()

    def cancel_entry():
        eE.destroy()
        eP.destroy()
        eN.destroy()
        eU.destroy()
        submitEntry.destroy()
        cancelEntry.destroy()

    def new_entry():
        global eE
        global eP
        global eN
        global eU
        global submitEntry
        global cancelEntry
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
        cancelEntry = Button(data_screen, text='Cancel Entry', fg='black', font=("Arial", 10), height = 1, width = 13, command=cancel_entry)
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
            if dataf['settings']['pass_hidden'] == 0:
                decode_pass = decoded(row[2])
                datatable.insert(parent='',index='end', text='', values=(row[1],decode_pass,row[3],row[4],row[5]))
            elif dataf['settings']['pass_hidden'] == 1:
                decode_pass = decoded(row[2])
                hidden_pass = '*'*(len(decode_pass) + int(4))
                datatable.insert(parent='',index='end', text='', values=(row[1],hidden_pass,row[3],row[4],row[5]))
        df.seek(0)
        df.truncate()
        df.write(json.dumps(dataf))
        df.close()
    
        datatable.pack()

    def copyPass():
        
        selected=datatable.focus()
        if selected != False:
            msgLabel.configure(text="Select A Row, Then Try Again")
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
    
    df = open(filename,'r+')
    dataf = json.load(df)
    m = Menu(root, tearoff = 0)
    m.add_command(label ="Go To URL", command=goToWeb)
    m.add_command(label ="Copy Email", command=copyEmail)
    m.add_command(label ="Copy Password", command=copyPass)
    m.add_separator()
    m.add_command(label ="Delete Selected", command=del_entry)

    def do_popup(event):
        try:
            m.tk_popup(event.x_root, event.y_root)

        finally:
            m.grab_release()
    df.seek(0)
    df.truncate()
    df.write(json.dumps(dataf))
    df.close()
    
    global datatable
    data_screen = Tk()
    data_screen.configure(background='lightgrey')
    data_screen.geometry("800x500")
    data_screen.title('Password Database')
    
    data_screen.bind("<Button-3>", do_popup)
    
    menubar = Menu(data_screen)
    
    df = open(filename,'r+')
    dataf = json.load(df)
    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='Exit', command = data_screen.destroy)
    actions = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Actions', menu = actions)
    actions.add_command(label ='Create New Entry', command = new_entry)
    actions.add_separator()
    actions.add_command(label ='Edit Selected', command = None)
    actions.add_separator()
    actions.add_command(label ="Show/Hide Passwords", command=toggle_hide_pass)
    help = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help)
    help.add_command(label ='About', command = about_screen)
    data_screen.config(menu = menubar)
    df.seek(0)
    df.truncate()
    df.write(json.dumps(dataf))
    df.close()


    global table_frame
    table_frame = Frame(data_screen)
    table_frame.pack()
    
    dataset()
    msgLabel = Label(data_screen, text='',bg="white", fg="red", font="Arial 12 bold")
    msgLabel.configure(background='lightgrey')
    msgLabel.pack(padx=10, anchor=N)
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
    try:
        eP
    except:
        root.clipboard_clear()
        root.clipboard_append(password)
        w.configure(text=password)
    else:
        if eP.winfo_ismapped() == 1:
            eP.delete(0, END)
            eP.insert(0, password)
            w.configure(text=password)
            root.clipboard_clear()
            root.clipboard_append(password)
            
    print(password)
    return password

def open_file():
    file = filedialog.askopenfilename(filetypes=[("CyberK9's Secured Local Database", ".sld")], defaultextension=".cksd")
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
    file = filedialog.asksaveasfilename(filetypes=[("CyberK9's Secured Local Database", ".sld")], defaultextension=".cksd")
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
root.configure(background='lightgrey')
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
help.add_command(label ='License', command = license_screen)
help.add_command(label ='About', command = about_screen)
root.config(menu = menubar)


p = securePass

w = Label(root, text="Click Generate to Start",font=("Arial", 30))
w.configure(background="lightgrey")
w.pack(pady=10)

s = Scale(root, length=400,width=15, from_=6, to=30,highlightthickness=0,troughcolor='#73B5FA', tickinterval=24,sliderrelief='flat',activebackground='#1065BF', orient=HORIZONTAL,command=print_value)
s.configure(background='lightgrey')
s.pack(pady=20)

redbutton = Button(root, text='Generate', fg='black', font=("Arial", 20), height = 1, width = 15, command=securePass)
redbutton.pack(pady=10)

warn = Label(root, text="**Generated Password Automatically Copies to Clipboard**", fg="darkred", font=("Arial", 9))
warn.configure(background="lightgrey")
warn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
