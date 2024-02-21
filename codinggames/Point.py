# Define the Point class
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

# Create a new instance of Point
point1 = Point(3, 4)
print("Point 1 coordinates:", point1.x, point1.y)  # Output: Point 1 coordinates: 3 4

# Create another instance of Point
point2 = Point(5, 6)

# Compare two Point instances for equality
print("Are point1 and point2 equal?", point1 == point2)  # Output: False
