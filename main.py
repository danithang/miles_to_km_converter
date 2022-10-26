from tkinter import *


def button_clicked():
    miles = int(user_input.get()) * float(1.609344)
    conversion_label.config(text=miles)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

user_input = Entry(width=6)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

conversion_label = Label(text=0, font=("Arial", 12))
conversion_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)


window.mainloop()
