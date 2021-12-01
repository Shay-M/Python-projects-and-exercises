from tkinter import *

root = Tk()

# create text file
entry_widget = Entry(root, width=55)
entry_widget.pack()


def my_fun():
    my_label = Label(root, text="hgg, " + entry_widget.get())
    my_label.pack()


my_button = Button(root, text="Hii!", command=my_fun)
my_button.pack()

root.mainloop()
