"""Lesson: return sends a value back to the caller."""

def rectangle_area(width, height):
    return width * height


area = rectangle_area(4, 6)
print(area)
print(rectangle_area(2, 9) + 1)