"""
Doc
"""
import math
def calculate_circle_area(radius):
    """
    DOC
    """
    if radius < 0:
        return None
    return math.pi * radius * radius
def function(shape):
    """
    DOC
    """
    print(f"Area: {shape.calc_area()}")
    print(f"Perimeter: {shape.calcPerimeter()}")
class ShapeCalculator:
    """
    DOC
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        """
        DOC
        """
        return self.length * self.width
    def calc_perimeter(self):
        """
        DOC
        """
        return 2 * (self.length + self.width)
def main():
    """
    DOC
    """
    circle_area = calculate_circle_area(5)
    print(f"Circle Area: {circle_area}")
    rectangle = ShapeCalculator(10, 20)
    print(f"Rectangle Area: {rectangle.calc_area()}")
    print(f"Rectangle Perimeter: {rectangle.calc_perimeter()}")

if __name__ == "__main__":
    print(main.__doc__)
    main()
