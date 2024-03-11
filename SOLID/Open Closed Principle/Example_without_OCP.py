class Shape:
    def __init__(self, type):
        self.type = type

class AreaCalculator:
    def calculate_area(self, shape):
        if shape.type == "square":
            return shape.side * shape.side
        elif shape.type == "circle":
            return 3.14 * shape.radius * shape.radius

# Exemple d'utilisation
square = Shape("square")
square.side = 4

circle = Shape("circle")
circle.radius = 3

calculator = AreaCalculator()
print(calculator.calculate_area(square))
print(calculator.calculate_area(circle))
