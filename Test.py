import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x400')
root.title("Unit Converter")

tab_control = ttk.Notebook(root)

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
        "kilometer^2": 0.000001,
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

# Dictionary to hold widgets per tab
tab_vars = {}

def convert(unit_type):
    from_unit = tab_vars[unit_type]["from_var"].get()
    to_unit = tab_vars[unit_type]["to_var"].get()
    entry_value = tab_vars[unit_type]["value_entry"].get()
    label = tab_vars[unit_type]["result_label"]

    try:
        value = float(entry_value)
        from_factor = conversion_factors[unit_type][from_unit]
        to_factor = conversion_factors[unit_type][to_unit]
        converted_value = value * ( to_factor/from_factor)
        label.config(text=f"Converted Value: {converted_value} {to_unit}")
    except ValueError:
        label.config(text="Error: Please enter a valid number.")
    except KeyError:
        label.config(text="Error: Invalid unit selected.")

# Build GUI for each unit type
for unit_type, units_dict in conversion_factors.items():
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=unit_type)

    units = list(units_dict.keys())

    # Per-tab variables
    from_var = tk.StringVar(value=units[0])
    to_var = tk.StringVar(value=units[1])

    ttk.Label(tab, text="From:", font=("Helvetica", 16)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    from_option = ttk.Combobox(tab, values=units, textvariable=from_var, state="readonly", width=18)
    from_option.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(tab, text="To:", font=("Helvetica", 16)).grid(row=0, column=2, padx=10, pady=10, sticky='w')
    to_option = ttk.Combobox(tab, values=units, textvariable=to_var, state="readonly", width=18)
    to_option.grid(row=0, column=3, padx=10, pady=10)

    ttk.Label(tab, text="Enter Value:", font=("Helvetica", 16)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    value_entry = ttk.Entry(tab, font=("Helvetica", 16), width=10)
    value_entry.grid(row=1, column=1, padx=10, pady=10)

    result_label = ttk.Label(tab, text="Converted Value:", font=("Helvetica", 16))
    result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=20, sticky='w')

    convert_btn = ttk.Button(tab, text="Convert", command=lambda u=unit_type: convert(u))
    convert_btn.grid(row=1, column=2, padx=10, pady=10)

    # Store variables and widgets for this tab
    tab_vars[unit_type] = {
        "from_var": from_var,
        "to_var": to_var,
        "value_entry": value_entry,
        "result_label": result_label
    }

tab_control.pack(expand=1, fill="both")
root.mainloop()
