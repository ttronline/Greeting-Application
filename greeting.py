from tkinter import *

root = Tk()

def greet():
    label_2.pack()

label_2 = Label(root, text="Happy Birthday!!!!",bg="Yellow",fg="Indigo")
label_2.config(font=("Cooper Black",24))


label = Label(root, text="Welcome, to the Greetings Application",bg="Lime",fg="Indigo")
label.config(font=("Comic Sans",23))
label.pack()

btn = Button(root, text="HEY, CLICK ME",bg="Pink",fg="Black", width = 13, height = 4,command=greet)
btn.config(font=("Raleway",17))
btn.pack()

root.mainloop()
