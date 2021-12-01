from tkinter import *

root = Tk()
root.title("Calculating Windows")
# root.geometry("300x400")

window_height = 40


def accountant_fun():
    try:
        total_size = float(entry_total_size.get())
        upper_margins = float(entry_upper_margins.get())
        lower_margins = float(entry_lower_margins.get())
        number_of_windows = int(entry_number_of_windows.get())

        working_area = float(total_size - (upper_margins + lower_margins))
        list_of_windows = []

        for i in range(number_of_windows):
            answer_Listbox.insert(i + 1,
                                  round(upper_margins + ((working_area - window_height) * i / (number_of_windows - 1)),
                                        3))
            list_of_windows.append(
                round(upper_margins + ((working_area - window_height) * i / (number_of_windows - 1)), 3))

        print(total_size - window_height - lower_margins)

        list_string = ' \n'.join(map(str, list_of_windows))
        # answer_label.config(text="Calculating:\n" + list_string)

    except ValueError:
        answer_label.config(text="Error!")


label_total_size = Label(root, text="Total size").grid(row=0, column=0, pady=5)
entry_total_size = Entry(root, width=20)
entry_total_size.grid(row=1, column=0, pady=0)

label_upper_margins = Label(root, text="Upper margins").grid(row=2, column=0, pady=5)
entry_upper_margins = Entry(root, width=20)
entry_upper_margins.grid(row=3, column=0, pady=5)

label_lower_margins = Label(root, text="Lower margins").grid(row=2, column=2, pady=5)
entry_lower_margins = Entry(root, width=20)
entry_lower_margins.grid(row=3, column=2, pady=5)

label_number_of_windows = Label(root, text="Number of windows").grid(row=4, column=0, pady=5)
entry_number_of_windows = Entry(root, width=20)
entry_number_of_windows.grid(row=5, column=0, pady=0)

answer_label = Label(root)
answer_label.grid(row=9, column=0, pady=2)

answer_Listbox = Listbox(root)
answer_Listbox.grid(row=10, column=1)

accountant_button = Button(root, text="Calculating", command=accountant_fun).grid(row=8, column=1, pady=20)

root.mainloop()
