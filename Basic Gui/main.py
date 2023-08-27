import os
import string
import json
import random
from tkinter import *
#from tkinter.ttk import *
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

def settings():
    if os.path.exists('C:/Users/Brandon/Desktop/Python/Basic Gui/settings.json'):
        f = open('C:/Users/Brandon/Desktop/Python/Basic Gui/settings.json','r')
        data = json.load(f)
        print(data)
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
    while len(password) != passlen:
        strength = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*"]
        letters = random.choice(strength)
        password = password + letters
    root.clipboard_clear()
    root.clipboard_append(password)
    w.configure(text=password)
    print(password)
    return password


root = Tk()

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
file.add_command(label ='New Database', command = None)
file.add_command(label ='Open Database', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Settings', command = settings)
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help)
help.add_command(label ='About', command = about_screen)
root.config(menu = menubar)


p = securePass

w = Label(root, text="Click Generate to Start",font=("Arial", 35))
w.pack()

s = Scale(root, length=200,width=15, from_=0, to=30, orient=HORIZONTAL,command=print_value)
s.pack()

redbutton = Button(root, text='Generate', fg='black', font=("Arial", 20), height = 1, width = 15, command=securePass)
redbutton.pack()

warn = Label(root, text="Automaticlly Copies to Clipboard", fg="red", font=("Arial", 9))
warn.pack( side = BOTTOM)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()



