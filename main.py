# Importing the 'Rectangle' class from the file 'rectangle1'
from rectangle1 import Rectangle

# Asking the user to input the length and width of a rectangle
l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))

# Creating an instance of the 'Rectangle' class using user-provided dimensions
rectangle1 = Rectangle(l, w)   

print("\nRectangle Properties : ")

# Displaying the properties of the rectangle using the 'DisplayRectangle' method
rectangle1.DisplayRectangle()  
