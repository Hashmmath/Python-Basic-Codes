'''Note: This code uses the Exchange Rates API to get the 
latest currency exchange rates. You can sign up for a free 
API key on their website. Also, please note that this code is 
for educational purposes only and should not be used for any 
commercial purposes.'''

import tkinter as tk
import requests

class CurrencyConverter:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]
 
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]
 
        # limiting the precision to 4 decimal places
        amount = round(amount * self.rates[to_currency], 4)
        return amount
 
# GUI code
class CurrencyConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")
        self.master.geometry("400x200")
 
        # create labels and entry boxes
        self.amount_label = tk.Label(self.master, text="Amount")
        self.amount_label.grid(row=0, column=0)
        self.from_currency_label = tk.Label(self.master, text="From Currency")
        self.from_currency_label.grid(row=1, column=0)
        self.to_currency_label = tk.Label(self.master, text="To Currency")
        self.to_currency_label.grid(row=2, column=0)
        self.converted_amount_label = tk.Label(self.master, text="")
        self.converted_amount_label.grid(row=3, column=0)
 
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=0, column=1)
 
        self.from_currency_entry = tk.Entry(self.master)
        self.from_currency_entry.grid(row=1, column=1)
 
        self.to_currency_entry = tk.Entry(self.master)
        self.to_currency_entry.grid(row=2, column=1)
 
        # create a button to initiate conversion
        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=1)
 
    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()
 
        converter = CurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')
        converted_amount = converter.convert(from_currency, to_currency, amount)
 
        self.converted_amount_label.configure(text=str(converted_amount))
 
# create the GUI window
root = tk.Tk()
currency_converter = CurrencyConverterGUI(root)
root.mainloop()
