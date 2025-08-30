from tkinter import *

window = Tk()
window.title("Demo window")
window.geometry("300x200")

lbl = Label(text="Hey there!", font=("Arial", 14))
lbl.pack(pady=20)

button = Button(window, text="Click Me", command=lambda: lbl.config(text="You clicked!"))
button.pack()

window.mainloop()
