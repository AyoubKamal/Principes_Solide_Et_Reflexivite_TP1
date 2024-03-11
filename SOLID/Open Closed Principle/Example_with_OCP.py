from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()

# Exemple d'utilisation
square = Square(4)
circle = Circle(3)

calculator = AreaCalculator()
print(calculator.calculate_area(square))
print(calculator.calculate_area(circle))
