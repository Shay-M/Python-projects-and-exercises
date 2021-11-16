from tkinter import *

root = Tk()


def my_fun():
    my_label = Label(root, text="Hello")
    my_label.pack()


my_button = Button(root, text="Hii!", padx=50, pady=30, command=my_fun, fg='blue')  # not my_fun() bcz it will call

my_button.pack()

root.mainloop()
