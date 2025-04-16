# Unit Converter Application
# This script creates a GUI-based unit converter using the `tkinter` library. 
# It allows users to convert between different units of measurement for Length, Area, and Weight.
# Modules:
#     - tkinter: Provides the GUI framework.
#     - tkinter.ttk: Provides themed widgets for the GUI.
# Features:
#     - Tabbed interface for different unit types (Length, Area, Weight). (scalable: can add more tabs easily by adding to the dictionary)
#     - Dropdown menus to select "From" and "To" units.
#     - Input field to enter the value to be converted.
#     - Button to perform the conversion.
#     - Displays the converted value in the selected unit.
# Global Variables:
#     - conversion_factors (dict): A dictionary containing conversion factors for each unit type.
#     - result (dict): A dictionary to store widgets and variables for each tab.
# Functions:
#     - convert(unit_type): 
#         Converts the input value from one unit to another based on the selected unit type.
#         Parameters:
#             unit_type (str): The type of unit to convert (e.g., "Length", "Area", "Weight").
#         Exceptions:
#             - ValueError: Raised if the input value is not a valid number.
#             - KeyError: Raised if an invalid unit is selected.
# GUI Components:
#     - Root window: The main application window.
#     - Tab control: A notebook widget to organize tabs for each unit type.
#     - Tabs: Separate tabs for Length, Area, and Weight conversions.
#     - Labels, Comboboxes, Entry fields, and Buttons: Widgets for user interaction and displaying results.
# Usage:
#     Run the script to launch the Unit Converter application. Select the desired unit type, 
#     choose the "From" and "To" units, enter a value, and click "Convert" to see the result.
# Filepath:
#     /c:/Users/gdlga/OneDrive/Desktop/python codes personal/100_weeks/Week2/Week2.py


import tkinter as tk
from tkinter import ttk

# Create the root window and set its size and title
root = tk.Tk()
root.geometry('600x200')
root.title("Unit Converter")

# Create a tab control (notebook) for category tabs (Length, Area, Weight)
tab_control = ttk.Notebook(root)

# Define conversion factors for different units
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

# Dictionary to store widgets and variables for each tab
result = {}

# Function to perform conversion based on selected tab (unit_type)
def convert(unit_type):
    # Retrieve widgets and variables for the selected tab
    from_unit = result[unit_type]["from_var"].get()
    to_unit = result[unit_type]["to_var"].get()
    entry_value = result[unit_type]["value_entry"].get()
    label = result[unit_type]["result_label"]

    try:
        # Convert string input to float
        value = float(entry_value)

        # Retrieve conversion factors for selected units
        from_factor = conversion_factors[unit_type][from_unit]
        to_factor = conversion_factors[unit_type][to_unit]

        # Perform the unit conversion using your model: (value × to/from)
        converted_value = value * (to_factor / from_factor)

        # Display the result
        label.config(text=f"Converted Value: {converted_value} {to_unit}")

    except ValueError:
        # Handle non-numeric input
        label.config(text="Error: Please enter a valid number.")
    except KeyError:
        # Handle incorrect unit keys (unlikely due to dropdowns)
        label.config(text="Error: Invalid unit selected.")

# Dynamically generate a tab for each unit type
for factor, units_dict in conversion_factors.items():
    # Create a new frame for each tab and add it to the notebook
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=factor)

    # List of unit options for the dropdowns
    units = list(units_dict.keys())

    # Variables to track selected units in dropdowns
    selected_from = tk.StringVar(value=units[0])
    selected_to = tk.StringVar(value=units[1])

    # "From" label and dropdown
    ttk.Label(tab, text="From:", font=("Helvetica", 16)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    from_option = ttk.Combobox(tab, values=units, textvariable=selected_from, state="readonly", width=18)
    from_option.grid(row=0, column=1, padx=10, pady=10)

    # "To" label and dropdown
    ttk.Label(tab, text="To:", font=("Helvetica", 16)).grid(row=0, column=2, padx=10, pady=10, sticky='w')
    to_option = ttk.Combobox(tab, values=units, textvariable=selected_to, state="readonly", width=18)
    to_option.grid(row=0, column=3, padx=10, pady=10)

    # Input label and entry field
    ttk.Label(tab, text="Enter Value:", font=("Helvetica", 16)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    input_entry = ttk.Entry(tab, font=("Helvetica", 16), width=10)
    input_entry.grid(row=1, column=1, padx=10, pady=10)

    # Convert button that triggers the convert function
    convert_btn = ttk.Button(tab, text="Convert", command=lambda u=factor: convert(unit_type=u))
    convert_btn.grid(row=1, column=2, padx=10, pady=10)

    # Label to display the result of conversion
    result_label = ttk.Label(tab, text="Converted Value:", font=("Helvetica", 16))
    result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=20, sticky='w')

    # Store all necessary variables and widgets for each tab in result dict
    result[factor] = {
        "from_var": selected_from,
        "to_var": selected_to,
        "value_entry": input_entry,
        "result_label": result_label
    }

# Pack and display the tab control
tab_control.pack(expand=1, fill="both")

# Start the Tkinter event loop
root.mainloop()
