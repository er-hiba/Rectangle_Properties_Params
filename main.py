from rectangle1 import Rectangle

l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))

rectangle1 = Rectangle(l, w)   

print("\nRectangle Properties : ")

rectangle1.Perimeter()

rectangle1.Area()

rectangle1.isSquare()

rectangle1.DisplayRectangle()
