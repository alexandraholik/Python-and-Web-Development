import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        return math.sqrt(dx ** 2 + dy ** 2)

# Create two Point objects
point1 = Point(1, 2)
point2 = Point(4, 6)

# Create a Line object using composition
line = Line(point1, point2)

# Calculate the length of the line
line_length = line.length()
print(f"The length of the line is: {line_length}")
