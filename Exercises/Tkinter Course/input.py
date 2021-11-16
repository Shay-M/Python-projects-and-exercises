from tkinter import *

root = Tk()

e = Entry(root, width=55)
e.pack()


def my_fun():
    my_label = Label(root, text="hii, " + e.get())
    my_label.pack()


my_button = Button(root, text="Hii!", command=my_fun)
my_button.pack()

root.mainloop()
