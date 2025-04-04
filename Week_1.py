import tkinter as tk
from math import pi 
from PIL import Image, ImageTk


size = '800x600'   

root = tk.Tk()
root.title("area & perimeter calculator")   # set the title of the window

root.geometry(size)   # set the size of the window

display_ref = {}  

shape_label = tk.Label(root, text="Select a shape to calculate its area and perimeter:", font=("Arial", 16), anchor="w")
shape_label.place(x=10, y=10)



Shapes ={                                                         # create a list of shapes 
    "Triangle":
      r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\tri.jpeg" ,
    
    "Square":
     r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\sq.jpeg",

    "Rectangle":
     r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\rect.jpeg",

    "Parallelogram": 
    r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\llgm.jpeg",

    "Rhombus": 
    r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\rhom.jpeg",

    "Trapezium":
    r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\Trapezoid-90.jpg",

    "Circle": 
    r"C:\Users\gdlga\OneDrive\Desktop\python codes personal\100_weeks\Images\circle.jpeg"}   

selected_shape = tk.StringVar(root)  # create a variable to hold the selected shape

def update_gui(selected):
    # Clear existing widgets
    for widget in root.winfo_children():
          widget.place_forget()  # Forget the previous widgets

    if selected_shape.get() == "Triangle":   # if the selected shape is a triangle
        triangle_GUI(root)
    if selected_shape.get() == "Square":   # if the selected shape is a square
        square_GUI(root)
    if selected_shape.get() == "Rectangle":   # if the selected shape is a rectangle 
        rectangle_GUI(root)
    if selected_shape.get() == "Parallelogram":   # if the selected shape is a parallelogram
        parallelogram_GUI(root)
    if selected_shape.get() == "Rhombus":   # if the selected shape is a rhombus
        rhombus_GUI(root)
    if selected_shape.get() == "Trapezium":   # if the selected shape is a trapezium
        trapezium_GUI(root)
    if selected_shape.get() == "Circle":   # if the selected shape is a circle
        circle_GUI(root)
        


for shape in Shapes:   # loop through the shapes
    shape_radio = tk.Radiobutton(root, text=shape, value=shape, variable=selected_shape, command= lambda : update_gui(selected_shape.get()), font=("Arial", 14),)
    shape_radio.place(x=10, y=50 + 30 * list(Shapes.keys()).index(shape))              

area_label = None
perimeter_label = None 

def triangle_GUI(root):
    global area_label, perimeter_label
    
    triangle_label = tk.Label(root, text="Enter the base and height of the triangle:", font=("Arial", 16), anchor="w")
    triangle_label.place(x=10, y=10)
    
    base_label = tk.Label(root, text="Base:", font=("Arial", 14), anchor="w")
    base_label.place(x=10, y=50)
    
    base_entry: int = tk.Entry(root, font=("Arial", 14))
    base_entry.place(x=10, y=80)
    
    height_label = tk.Label(root, text="Height:", font=("Arial", 14), anchor="w")
    height_label.place(x=10, y=110)
    
    height_entry: int = tk.Entry(root, font=("Arial", 14))
    height_entry.place(x=10, y=140)
    
    calculate_button = tk.Button(root, text="Calculate",command=lambda: calculate(base_entry.get, height_entry.get), font=("Arial", 14))
    calculate_button.place(x=10, y=170)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=210)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w")
    perimeter_label.place(x=10, y=240)



def square_GUI(root):
    global area_label, perimeter_label
    square_label = tk.Label(root, text="Enter the side length of the square:", font=("Arial", 16), anchor="w")
    square_label.place(x=10, y=10)
    
    side_label = tk.Label(root, text="Side Length:", font=("Arial", 14), anchor="w")
    side_label.place(x=10, y=50)
    
    side_entry = tk.Entry(root, font=("Arial", 14))
    side_entry.place(x=10, y=80)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(side_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=110)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=150)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w")
    perimeter_label.place(x=10, y=180)
    
def rectangle_GUI(root):
    global area_label, perimeter_label
    rectangle_label = tk.Label(root, text="Enter the length and width of the rectangle:", font=("Arial", 16), anchor="w")
    rectangle_label.place(x=10, y=10)
    
    length_label = tk.Label(root, text="Length:", font=("Arial", 14), anchor="w")
    length_label.place(x=10, y=50)
    
    length_entry = tk.Entry(root, font=("Arial", 14))
    length_entry.place(x=10, y=80)
    
    width_label = tk.Label(root, text="Width:", font=("Arial", 14), anchor="w")
    width_label.place(x=10, y=110)
    
    width_entry = tk.Entry(root, font=("Arial", 14))
    width_entry.place(x=10, y=140)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(length_entry.get, width_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=170)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=210)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w")
    perimeter_label.place(x=10, y=240)

def parallelogram_GUI(root):    
    global area_label, perimeter_label
    parallelogram_label = tk.Label(root, text="Enter the base and height of the parallelogram:", font=("Arial", 16), anchor="w")
    parallelogram_label.place(x=10, y=10)

    base_label = tk.Label(root, text="Base:", font=("Arial", 14), anchor="w")
    base_label.place(x=10, y=50)
    
    base_entry = tk.Entry(root, font=("Arial", 14))
    base_entry.place(x=10, y=80)
    
    height_label = tk.Label(root, text="Height:", font=("Arial", 14), anchor="w")
    height_label.place(x=10, y=110)
    
    height_entry = tk.Entry(root, font=("Arial", 14))
    height_entry.place(x=10, y=140)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(base_entry.get, height_entry.get), font=("Arial", 14))
    calculate_button.place(x=10, y=170)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=210)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w")
    perimeter_label.place(x=10, y=240)

def rhombus_GUI(root):
    global area_label, perimeter_label
    rhombus_label = tk.Label(root, text="Enter the base and height of the rhoumbus:", font=("Arial", 16), anchor="w")
    rhombus_label.place(x=10, y=10)

    height_label = tk.Label(root, text="Enter the height of the rhombus:", font=("Arial", 16), anchor="w")
    height_label.place(x=10, y=50)
    
    base_label = tk.Label(root, text="Base:", font=("Arial", 14), anchor="w")
    base_label.place(x=10, y=110)

    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(height_entry.get, base_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=170)

    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=210)

    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w") 
    perimeter_label.place(x=10, y=240)

    height_entry = tk.Entry(root, font=("Arial", 14))
    height_entry.place(x=10, y=80)

    base_entry = tk.Entry(root, font=("Arial", 14))
    base_entry.place(x=10, y=140)

def trapezium_GUI(root):
    global area_label, perimeter_label
    trapezium_label = tk.Label(root, text="Enter the lengths of the two parallel sides and the height:", font=("Arial", 16), anchor="w")
    trapezium_label.place(x=10, y=10)
    
    base1_label = tk.Label(root, text="Base 1:", font=("Arial", 14), anchor="w")
    base1_label.place(x=10, y=50)
    
    base1_entry = tk.Entry(root, font=("Arial", 14))
    base1_entry.place(x=10, y=80)
    
    base2_label = tk.Label(root, text="Base 2:", font=("Arial", 14), anchor="w")
    base2_label.place(x=10, y=110)
    
    base2_entry = tk.Entry(root, font=("Arial", 14))
    base2_entry.place(x=10, y=140)
    
    height_label = tk.Label(root, text="Height:", font=("Arial", 14), anchor="w")
    height_label.place(x=10, y=170)
    
    height_entry = tk.Entry(root, font=("Arial", 14))
    height_entry.place(x=10, y=200)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(base1_entry.get, base2_entry.get, height_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=230)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=270)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w")
    perimeter_label.place(x=10, y=300)

def circle_GUI(root):
    global area_label, perimeter_label
    circle_label = tk.Label(root, text="Enter the radius of the circle:", font=("Arial", 16), anchor="w")
    circle_label.place(x=10, y=10)
    
    radius_label = tk.Label(root, text="Radius:", font=("Arial", 14), anchor="w")
    radius_label.place(x=10, y=50)
    
    radius_entry = tk.Entry(root, font=("Arial", 14))
    radius_entry.place(x=10, y=80)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(radius_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=110)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w")
    area_label.place(x=10, y=150)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w")
    perimeter_label.place(x=10, y=180)

def calculate(*args):
    if selected_shape.get() == "Triangle":
        try:
            base = float(args[0]())
            height = float(args[1]())
            area = 0.5 * base * height
            perimeter = 3 * base + 2 * height
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"Perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")

    if selected_shape.get() == "Square":
        try:
            side = float(args[0]())
            area = side ** 2
            perimeter = 4 * side
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")

    if selected_shape.get() == "Rectangle":
        try:
            length = float(args[0]())
            width = float(args[1]())
            area = length * width
            perimeter = 2 * (length + width)
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"Perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")

    if selected_shape.get() == "Parallelogram":
        try:
            base = float(args[0]())
            height = float(args[1]())
            area = base * height
            perimeter = 2 * (base + height)
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"Perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")

    if selected_shape.get() == "Rhombus":
        try:
            height = float(args[0]())
            base = float(args[1]())
            area = base * height
            perimeter = 4 * base
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"Perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")
   
    if selected_shape.get() == "Trapezium":
        try:
            base1 = float(args[0]())
            base2 = float(args[1]())
            height = float(args[2]())
            area = 0.5 * (base1 + base2) * height
            perimeter = base1 + base2 + 2 * ((base1 - base2) ** 2 + height ** 2) ** 0.5
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"Perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")
  
    if selected_shape.get() == "Circle":
        try:
            radius = float(args[0]())
            area = pi * radius ** 2
            perimeter = 2 * pi * radius
            area_label.config(text=f"Area: {area}")
            perimeter_label.config(text=f"Perimeter: {perimeter}")
        except ValueError:
            area_label.config(text="Invalid input")
            perimeter_label.config(text="Invalid input")


root.mainloop()