class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def isSquare(self):
        if self.length == self.width:
            return True
        else:
            return False

    def DisplayRectangle(self):
        print(f"- Length: {self.length}")
        print(f"- Width: {self.width}")
        print(f"- Perimeter: {self.Perimeter()}")
        print("- Area:", self.Area())

        if self.isSquare() == True:
            print("- It is a square")
        else:
            print("- It's not a square")
