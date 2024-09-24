from tkinter import *
from passwordgenerator import pwgenerator
root = Tk()
#Labels For Heading
heading =Label(root,text="Welcome to Password Genrator",font=("Arial Black",14)).place(x=1,y=1)
def passwordgenrate():
    global passwordis
    passwordis = pwgenerator.generate()
    passwordentry.insert(END,passwordis)
def save():
    passfile = open("password.txt","a")
    passfile.write(f"{Appvalue.get()}, -- {passwordis} \n")
    passfile.close()
    quit()
Appname = Label(root,text="Name of app",font=(14)).place(x=10,y=35)
password = Label(root,text="Password",font=(14)).place(x=10,y=65)
#App value and string value
Appvalue = StringVar()
passwordvalue = StringVar()
#App and password Entry
AppEntry = Entry(root,textvariable=Appvalue).place(x=115,y=35)
global passwordentry
passwordentry = Entry(root,textvariable=passwordvalue)
passwordentry.place(x=115,y=65)
#Buttons
passbutt = Button(root,text="Genrate Password",command=passwordgenrate).place(x=10,y=100)
saqui = Button(root,text="Save&Quit",command=save).place(x=10,y=130)

mainloop()