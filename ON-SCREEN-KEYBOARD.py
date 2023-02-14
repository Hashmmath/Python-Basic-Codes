'''This code creates a window with all the letters, numbers, 
and special characters of a standard keyboard. When a button 
is clicked, the function button_click is executed, which 
prints the clicked key to the console. You can replace this 
function with your own code to implement the desired functionality.'''

import tkinter as tk

def button_click(key):
    # Function to be executed when a button is clicked
    print(key)

root = tk.Tk()
root.title("On-Screen Keyboard")

# Create the buttons
button_list = [
    '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace',
    'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
    'Caps Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter',
    'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift',
    'Ctrl', 'Fn', 'Win', 'Alt', 'Space', 'Alt', 'Ctrl', 'Left', 'Up', 'Down', 'Right'
]

# Create a grid of buttons
row = 1
col = 0
for button_text in button_list:
    button = tk.Button(root, text=button_text, width=5, height=2, command=lambda key=button_text: button_click(key))
    button.grid(row=row, column=col)
    col += 1
    if col > 12:
        row += 1
        col = 0

root.mainloop()
