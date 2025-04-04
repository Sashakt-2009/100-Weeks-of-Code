import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Area & Perimeter Calculator")
root.geometry("800x600")

# Dictionary to store image paths for each shape
Shapes = {
    "Triangle": "tri.jpeg",
    "Square": "sq.jpeg",
    "Rectangle": "rect.jpeg",
    "Parallelogram": "llgm.jpeg",
    "Rhombus": "rhom.jpeg",
    "Trapezium": "Trapezoid-90.jpg",
    "Circle": "circle.jpeg"
}

# Variable to hold the selected shape
selected_shape = tk.StringVar(root)

# Function to clear GUI before updating
def clear_gui():
    for widget in root.winfo_children():
        widget.place_forget()

# General function to create input fields dynamically
def create_shape_GUI(title, fields):
    clear_gui()
    
    tk.Label(root, text=title, font=("Arial", 16)).place(x=10, y=10)
    
    entries = {}
    y_pos = 50
    for field in fields:
        tk.Label(root, text=f"{field}:", font=("Arial", 14)).place(x=10, y=y_pos)
        entry = tk.Entry(root, font=("Arial", 14))
        entry.place(x=150, y=y_pos)
        entries[field] = entry
        y_pos += 40

    # Button to calculate
    tk.Button(root, text="Calculate", font=("Arial", 14)).place(x=10, y=y_pos)
    
    # Display area and perimeter
    tk.Label(root, text="Area:", font=("Arial", 14)).place(x=10, y=y_pos + 40)
    tk.Label(root, text="Perimeter:", font=("Arial", 14)).place(x=10, y=y_pos + 70)
    
    return entries

# Shape-specific GUI functions
def triangle_GUI(): return create_shape_GUI("Enter base and height of the triangle", ["Base", "Height"])
def square_GUI(): return create_shape_GUI("Enter the side length of the square", ["Side"])
def rectangle_GUI(): return create_shape_GUI("Enter the length and width of the rectangle", ["Length", "Width"])
def parallelogram_GUI(): return create_shape_GUI("Enter base and height of the parallelogram", ["Base", "Height"])
def rhombus_GUI(): return create_shape_GUI("Enter diagonal lengths", ["Diagonal 1", "Diagonal 2"])
def trapezium_GUI(): return create_shape_GUI("Enter bases and height of the trapezium", ["Base 1", "Base 2", "Height"])
def circle_GUI(): return create_shape_GUI("Enter the radius of the circle", ["Radius"])

# Dictionary mapping shape names to GUI functions
shape_functions = {
    "Triangle": triangle_GUI,
    "Square": square_GUI,
    "Rectangle": rectangle_GUI,
    "Parallelogram": parallelogram_GUI,
    "Rhombus": rhombus_GUI,
    "Trapezium": trapezium_GUI,
    "Circle": circle_GUI
}

# Function to update GUI when a shape is selected
def update_gui():
    shape_name = selected_shape.get()
    if shape_name in shape_functions:
        shape_functions[shape_name]()

# Create radio buttons dynamically
y_offset = 50
for shape in Shapes.keys():
    tk.Radiobutton(root, text=shape, value=shape, variable=selected_shape, command=update_gui, font=("Arial", 14)).place(x=10, y=y_offset)
    y_offset += 30

root.mainloop()
