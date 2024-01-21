import math
class Shapes:
    def __init__(self, perimeter, area):
        self.perimeter = perimeter
        self.area = area

    def print_perimeter(self):
        print("The perimeter is: " + str(self.perimeter))

    def print_area(self):
        print("The area is: " + str(self.area))

class Triangle(Shapes):
    def __init__(self,side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        perimeter = self.triangle_perimeter()
        area = self.triangle_area()
        super().__init__(perimeter, area)

    def triangle_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def triangle_area(self):
        semi_perimeter = self.triangle_perimeter() / 2
        return math.sqrt(semi_perimeter*(semi_perimeter - self.side_a) * (semi_perimeter - self.side_b) * (semi_perimeter - self.side_c))


class Square(Shapes):
    def __init__(self,side):
        self.side = side
        perimeter = self.square_perimeter()
        area = self.square_area()
        super().__init__(perimeter, area)

    def square_perimeter(self):
        return self.side * 4

    def square_area(self):
        return self.side ** 2

class Rectangle(Shapes):
    def __init__(self,side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        perimeter = self.rectangle_perimeter()
        area = self.rectangle_area()
        super().__init__(perimeter, area)

    def rectangle_perimeter(self):
        return self.side_a * 2 + self.side_b * 2

    def rectangle_area(self):
        return self.side_a * self.side_b

class Circle(Shapes):
    def __init__(self, r):
        self.r = r
        perimeter = self.circle_perimeter()
        area = self.circle_area()
        super().__init__(perimeter, area)

    def circle_perimeter(self):
        return 2 * math.pi * self.r

    def circle_area(self):
        return (math.pi * self.r) ** 2

class Cylinder(Circle):
    def __init__(self, r, height):
        self.height = height
        super().__init__(r)

    def cylinder_volume(self):
        return super().circle_area() * self.height
