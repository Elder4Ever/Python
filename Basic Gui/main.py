import string
import random
from tkinter import *
#from tkinter.ttk import *
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
#passwd = securePass()
root = Tk()

root.title("Brandon's Password Generator")
root.geometry('700x150')
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
edit.add_command(label ='Settings', command = None)
root.config(menu = menubar)


p = securePass

w = Label(root, text="Click Generate to Start",font=("Arial", 35))
w.pack()
s = Scale(root, length=150,width=10, from_=0, to=30, orient=HORIZONTAL,command=print_value)
s.pack()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text='Generate', fg='black', font=("Arial", 20), height = 1, width = 15, command=securePass)
redbutton.pack( side = BOTTOM)

warn = Label(root, text="Automaticlly Copies to Clipboard", fg="red", font=("Arial", 9)).place(x=150, y=120)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()



