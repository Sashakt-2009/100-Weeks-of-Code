# Setup

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x400')
root.title("Unit Converter")

tab_control = ttk.Notebook(root)

# Reference dictionaries

conversion_factors = {
    "Length": {
        "meters": 1,
        "kilometers": 0.001,
        "Inch": 39.3700787,
        "feet": 3.28084,
        "miles": 0.000621371
    },
    
    "Area": {
        "meter^2": 1,
        "kilometer^2":0.000001,
        "acre": 0.0002471,
        "Hectare": 0.0001,

    },
    
    "Weight": {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "Carat": 5
    }

}
tabs = {}

# Setting up tabs 

for factor in conversion_factors:
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=factor)
    tabs[factor] = tab

    # Create a container row frame at the top
    row = ttk.Frame(tab)
    row.pack(side="top", fill="x", pady=10)

    # From label on the left
    ttk.Label(row, text="From:", font=("Helvetica", 20)).pack(side="left", anchor="nw", padx=10)

    # To label on the right
    ttk.Label(row, text="To:", font=("Helvetica", 20)).pack(side="right", anchor="ne", padx=10)
    
tab_control.pack(expand=1, fill="both")


root.mainloop()
