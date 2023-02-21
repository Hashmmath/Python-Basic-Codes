'''This code creates a window with labels and entries for the 
day, month, and year of birth, as well as a button to 
calculate the age and a label to display the calculated age. 
When the "Calculate Age" button is clicked, the calculate_age() 
function is called, which calculates the age based on the 
input values and updates the age label.'''


import tkinter as tk
from datetime import date

def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_label.config(text=f"You are {age} years old.")

# create the main window
window = tk.Tk()
window.title("Age Calculator")

# create labels and entries for day, month, and year of birth
day_label = tk.Label(window, text="Day:")
day_label.grid(column=0, row=0)
day_entry = tk.Entry(window, width=5)
day_entry.grid(column=1, row=0)

month_label = tk.Label(window, text="Month:")
month_label.grid(column=2, row=0)
month_entry = tk.Entry(window, width=5)
month_entry.grid(column=3, row=0)

year_label = tk.Label(window, text="Year:")
year_label.grid(column=4, row=0)
year_entry = tk.Entry(window, width=8)
year_entry.grid(column=5, row=0)

# create a button to calculate the age
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.grid(column=3, row=1)

# create a label to display the calculated age
age_label = tk.Label(window, text="")
age_label.grid(column=3, row=2)

# start the event loop
window.mainloop()
