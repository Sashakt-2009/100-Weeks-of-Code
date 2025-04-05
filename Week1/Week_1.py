import tkinter as tk, os, sys

from math import pi 
from PIL import Image, ImageTk


size = '800x400'   

area_label = None
perimeter_label = None 

root = tk.Tk()
root.title("area & perimeter calculator")   # set the title of the window
root.configure(bg="white")   # set the background color of the window
root.geometry(size)   # set the size of the window

Shapes ={                                                         # create a list of shapes 
    "Triangle": "tri.jpeg" ,
    
    "Square": "sq.jpeg",

    "Rectangle": "llgm.jpeg",

    "Parallelogram": "llgm.jpeg",

    "Rhombus": "rhom.jpeg",

    "Trapezium": "Trapezoid-90.jpg",

    "Circle": "circle.jpeg"}

selected_shape = tk.StringVar(root)  # create a variable to hold the selected shape

def get_asset_path(filename):
    base_path = os.path.dirname(__file__)  # gets the directory where the .py file is
    return os.path.join(base_path, "Images", filename)

display_ref = {}  
for shape in Shapes:
    pil_img = Image.open(get_asset_path(Shapes[shape]))
    pil_img = pil_img.resize((300, 300))
    img = ImageTk.PhotoImage(pil_img)
    display_ref[shape] = img


def main_window():
        # Clear existing widgets
    for widget in root.winfo_children():
          widget.place_forget()  # Forget the previous widgets

    shape_label = tk.Label(root, text="Select a shape to calculate its area and perimeter:", font=("Arial", 16), anchor="w", bg="white")
    shape_label.place(x=10, y=10)

    for shape in Shapes:   # loop through the shapes
        shape_radio = tk.Radiobutton(root, text=shape, value=shape, variable=selected_shape, command= lambda : update_gui(selected_shape.get()), font=("Arial", 14), bg="white")
        shape_radio.place(x=10, y=50 + 30 * list(Shapes.keys()).index(shape))              

main_window()


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
    
    return_button = tk.Button(root, text="Back", command= lambda: main_window(), font=("Arial", 14),)
    return_button.place(x=10, y=350)
        


def triangle_GUI(root):
    global area_label, perimeter_label
    
    triangle_label = tk.Label(root, text="Enter the base and height of the triangle:", font=("Arial", 16), anchor="w", bg="white")
    triangle_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Triangle"])
    img_label.place(x=500, y=0)  # Adjust the position as needed
    
    base_label = tk.Label(root, text="Base:", font=("Arial", 14), anchor="w", bg="white")
    base_label.place(x=10, y=50)
    
    base_entry: int = tk.Entry(root, font=("Arial", 14), bg="gray")
    base_entry.place(x=10, y=80)
    
    height_label = tk.Label(root, text="Height:", font=("Arial", 14), anchor="w", bg="white")
    height_label.place(x=10, y=110)
    
    height_entry: int = tk.Entry(root, font=("Arial", 14), bg="gray")
    height_entry.place(x=10, y=140)
    
    calculate_button = tk.Button(root, text="Calculate",command=lambda: calculate(base_entry.get, height_entry.get), font=("Arial", 14))
    calculate_button.place(x=10, y=170)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=210)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white")
    perimeter_label.place(x=10, y=240)



def square_GUI(root):
    global area_label, perimeter_label
    square_label = tk.Label(root, text="Enter the side length of the square:", font=("Arial", 16), anchor="w", bg="white")
    square_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Square"])
    img_label.place(x=500, y=0)  
    
    side_label = tk.Label(root, text="Side Length:", font=("Arial", 14), anchor="w",bg="white")
    side_label.place(x=10, y=50)
    
    side_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    side_entry.place(x=10, y=80)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(side_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=110)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=150)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white")
    perimeter_label.place(x=10, y=180)
    
def rectangle_GUI(root):
    global area_label, perimeter_label
    rectangle_label = tk.Label(root, text="Enter the length and width of the rectangle:", font=("Arial", 16), anchor="w", bg="white")
    rectangle_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Rectangle"])
    img_label.place(x=500, y=0)
    
    length_label = tk.Label(root, text="Length:", font=("Arial", 14), anchor="w", bg="white")
    length_label.place(x=10, y=50)
    
    length_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    length_entry.place(x=10, y=80)
    
    width_label = tk.Label(root, text="Width:", font=("Arial", 14), anchor="w", bg="white")
    width_label.place(x=10, y=110)
    
    width_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    width_entry.place(x=10, y=140)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(length_entry.get, width_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=170)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=210)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white")
    perimeter_label.place(x=10, y=240)

def parallelogram_GUI(root):    
    global area_label, perimeter_label
    parallelogram_label = tk.Label(root, text="Enter the base and height of the parallelogram:", font=("Arial", 16), anchor="w", bg="white")
    parallelogram_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Parallelogram"])
    img_label.place(x=500, y=0)

    base_label = tk.Label(root, text="Base:", font=("Arial", 14), anchor="w", bg="white")
    base_label.place(x=10, y=50)
    
    base_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    base_entry.place(x=10, y=80)
    
    height_label = tk.Label(root, text="Height:", font=("Arial", 14), anchor="w", bg="white")
    height_label.place(x=10, y=110)
    
    height_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    height_entry.place(x=10, y=140)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(base_entry.get, height_entry.get), font=("Arial", 14))
    calculate_button.place(x=10, y=170)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=210)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white")
    perimeter_label.place(x=10, y=240)

def rhombus_GUI(root):
    global area_label, perimeter_label
    rhombus_label = tk.Label(root, text="Enter the base and height of the rhoumbus:", font=("Arial", 16), anchor="w", bg="white")
    rhombus_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Rhombus"])
    img_label.place(x=500, y=0)

    height_label = tk.Label(root, text="Enter the height of the rhombus:", font=("Arial", 16), anchor="w", bg="white")
    height_label.place(x=10, y=50)
    
    base_label = tk.Label(root, text="Base:", font=("Arial", 14), anchor="w", bg="white")
    base_label.place(x=10, y=110)

    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(height_entry.get, base_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=170)

    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=210)

    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white") 
    perimeter_label.place(x=10, y=240)

    height_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    height_entry.place(x=10, y=80)

    base_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    base_entry.place(x=10, y=140)

def trapezium_GUI(root):
    global area_label, perimeter_label
    trapezium_label = tk.Label(root, text="Enter the lengths of the two parallel sides and the height:", font=("Arial", 16), anchor="w", bg="white")
    trapezium_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Trapezium"])
    img_label.place(x=500, y=0)
    
    base1_label = tk.Label(root, text="Base 1:", font=("Arial", 14), anchor="w", bg="white")
    base1_label.place(x=10, y=50)
    
    base1_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    base1_entry.place(x=10, y=80)
    
    base2_label = tk.Label(root, text="Base 2:", font=("Arial", 14), anchor="w", bg="white")
    base2_label.place(x=10, y=110)
    
    base2_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    base2_entry.place(x=10, y=140)
    
    height_label = tk.Label(root, text="Height:", font=("Arial", 14), anchor="w", bg="white")
    height_label.place(x=10, y=170)
    
    height_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    height_entry.place(x=10, y=200)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(base1_entry.get, base2_entry.get, height_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=230)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=270)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white")
    perimeter_label.place(x=10, y=300)

def circle_GUI(root):
    global area_label, perimeter_label
    circle_label = tk.Label(root, text="Enter the radius of the circle:", font=("Arial", 16), anchor="w", bg="white")
    circle_label.place(x=10, y=10)

    img_label = tk.Label(root, image=display_ref["Circle"])
    img_label.place(x=500, y=0)

    radius_label = tk.Label(root, text="Radius:", font=("Arial", 14), anchor="w", bg="white")
    radius_label.place(x=10, y=50)
    
    radius_entry = tk.Entry(root, font=("Arial", 14), bg="gray")
    radius_entry.place(x=10, y=80)
    
    calculate_button = tk.Button(root, text="Calculate", command= lambda: calculate(radius_entry.get), font=("Arial", 14),)
    calculate_button.place(x=10, y=110)
    
    area_label = tk.Label(root, text="Area:", font=("Arial", 14), anchor="w", bg="white")
    area_label.place(x=10, y=150)
    
    perimeter_label = tk.Label(root, text="Perimeter:", font=("Arial", 14), anchor="w", bg="white")
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