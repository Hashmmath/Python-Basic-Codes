'''This code creates a window with a Label widget that displays 
the current time in the format "HH:MM:SS". The update_clock function
updates the text in the label every second using the after method of the root window. 
The time.strftime function is used to format the current time as a string.'''

import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_clock)

label = tk.Label(root, font=("times", 50, "bold"), bg="white")
label.pack(fill="both", expand=1)

update_clock()
root.mainloop()
