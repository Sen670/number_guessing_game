from tkinter import *
import tkinter.messagebox
import random
root = Tk()
root.geometry("600x600")
root.configure(bg="lightblue")

label1 = Label(root,text="Number guessing game",font=("Ariel",30,"bold"))
label1.place(x=70,y=50)

def random_number():
    ran_number = random.randint(1,10)

def button_confirm():
    name = (entry1.get())
    tkinter.messagebox.showinfo("Weclome!","Hello " + name + " Guess a number between 1 and 10")


label2 = Label(root,text="Please enter your name")
label2.place(x=75,y=150)
entry1 = Entry(root,width=30)
entry1.place(x=250,y=150)

label3 = Label(root,text="Please guess a number from 1-10")
label3.place(x=50,y=250)
entry2= Entry(root,width=30)
entry2.place(x=250,y=250)

label3 = (root)

button1 = Button(root,text="Confirm",command=button_confirm)
button1.place(x=250,y=350)

root.mainloop()