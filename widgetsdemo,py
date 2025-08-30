from tkinter import *
from datetime import date 

window = Tk()
window.title('Demo Window')
window.geometry('400x300')

lbl = Label(text="Sample text", fg="white", bg="green", height=2, width=20)
name_lbl = Label(text="Full Name", bg="#000000", fg="white")
name_entry = Entry()

def display():
    name = name_entry.get()
    message = "Welcome to the Application\nToday's date is: "
    greet = "Hello " + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))

text_box = Text(height=5, width=40)
btn = Button(text="Begin", command=display, height=1, bg="#FFFFFF", fg="black")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()
