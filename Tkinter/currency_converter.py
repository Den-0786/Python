import tkinter as Tk
from tkinter import ttk
from tkinter import messagebox
import requests
import time

# ------------------ API SETUP --------------------#
API_KEY = "00f1a1c62a6bd54f62686808"
API_URL = "https://v6.exchangerate-api.com/v6/00f1a1c62a6bd54f62686808/latest/"

#------------------------Functions-----------------------#
def get_exchange_rate(from_currency, to_currency):
    try:
        response = requests.get(API_URL + from_currency)
        response.raise_for_status()
        data = response.json()
        
        if data["result"] != "success":
            raise ValueError("Failed to fetch exchange rates. Please try again.")
    
        rates = data.get("conversion_rates", {})
        
        if to_currency not in rates:
            raise ValueError(f"Invalid currency:Conversion rate for {to_currency} is not available")
        return rates[to_currency]
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"unable to fetch exchange rates: {e}")
        return None

def fetch_supported_currencies():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        if data["result"]!= "success":
            raise ValueError("Failed to fetch supported currencies. Please try again.")
        
        if "supported-codes" in data:
            return [code[0] for code in data["supported_codes"]]
        else:
            messagebox.showerror("Failed to fetch supported currencies. Please try again.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to fetch supported currencies: {e}")
        return[]

def calculate():
    try:
        # Get the selected currency and the amount
        selected_currency = currency_chosen.get()
        converted_to_currency = converted_to_chosen_currency.get()
        amount_str = amount_input.get().strip()
        
        if not amount_str:
            messagebox.showerror(title="oops", message="Please enter an amount.")
            return
        
        # Convert the amount to float
        try:
            amount = float(amount_str)
            if amount < 0:
                messagebox.showerror(title="oops", message="Invalid amount: Please enter a positive number")
                clear_entries()
                return
            
        except ValueError:
            messagebox.showerror(title="oops", message="Please enter a valid number.")
            clear_entries()
            return
        
        # Convert the amount
        conversion_rate = get_exchange_rate(selected_currency, converted_to_currency)
        if conversion_rate is None:
            return
        
        # Format the converted amount
        converted_amount = amount * conversion_rate
        formatted_converted_amount = f"${converted_amount:.2f}"
    
        # Display the converted amount
        calculated_currency_entry.config(state="normal")
        calculated_currency_entry.delete(0, "end")
        calculated_currency_entry.insert(0,formatted_converted_amount)
        calculated_currency_entry.config(state="readonly")
    
    except ValueError as ve:
        messagebox.showerror(title="oops", message=f"Error: {ve}")
        clear_entries()
    except Exception as e:
        messagebox.showerror(title="soorry!!!", message=f"Error:{str(e)}")
        clear_entries()
        
# ---------------------- Clearing all entries ----------------------#

def clear_entries():
    selected_currency.set("")
    converted_to_currency.set("")
    amount_input.delete(0, "end")
    calculated_currency_entry.config(state="normal")
    calculated_currency_entry.delete(0, "end")
    calculated_currency_entry.config(state="readonly")
    time.sleep(0.9)
#-----------------------UI SETUP---------------------------#

window = Tk.Tk()
window.title("Currency Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)


canvas = Tk.Canvas(window, width=400, height=400)
canvas.grid()

# ----------------- Labels ------------------------#
title_label = Tk.Label(window, text="CURRENCY CONVERTER",
        background="green", foreground="white",
        font=("Arial", 10, "bold"))
canvas.create_window(200, 20, window=title_label)

currency_to_convert_label = Tk.Label(text="Currency to convert:", font=("Arial", 10, "italic"))
canvas.create_window(70, 50, window=currency_to_convert_label)

#Fetch supported currencies dynamically
currency_list = ["USD","AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT",
"BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY",
"COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP",
"GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR",
"IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK",
"LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN",
"MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR",
"RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SLL","SOS","SRD","SSP","STN",
"SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX","UYU","UZS","VES",
"VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"
]

selected_currency = Tk.StringVar()
currency_chosen = ttk.Combobox(window, textvariable =selected_currency, state="readonly", width=10 )
currency_chosen["values"] = currency_list
canvas.create_window(200, 50, window=currency_chosen)
currency_chosen.current(0)

amount_label = Tk.Label(text="Enter the amount:", font=("Arial", 10, "normal"))
canvas.create_window(65, 100, window=amount_label)

amount_input = Tk.Entry(width=13)
canvas.create_window(200, 100, window=amount_input)

converted_to_label = Tk.Label(text="Convert to:", font=("Arial",10, "italic"))
canvas.create_window(45, 150, window=converted_to_label)

converted_to_currency = Tk.StringVar()
converted_to_chosen_currency = ttk.Combobox(window, textvariable = converted_to_currency, state="readonly", width=10 )
converted_to_chosen_currency["values"] = currency_list
canvas.create_window(200, 150, window=converted_to_chosen_currency)
converted_to_chosen_currency.current(0)


converted_currency_label = Tk.Label(text="Calculated Amount:", font=("Arial", 10,"normal"))
canvas.create_window(50, 200, window=converted_currency_label)

calculated_currency_entry = Tk.Entry(width=15, state="readonly")
canvas.create_window(200, 200, window=calculated_currency_entry)


calculate_button = Tk.Button(text="Compute", font=("Arial", 10,"normal"), command=calculate)
canvas.create_window(200, 240, window=calculate_button)

window.mainloop()