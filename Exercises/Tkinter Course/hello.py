# https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()
# top title
root.title("hi")

# top icon
# root.iconbitmap('c:/')

# creating a label widget
my_label = Label(root, text="Hello, world")

# shoving it onto the screen
my_label.pack()

root.mainloop()
