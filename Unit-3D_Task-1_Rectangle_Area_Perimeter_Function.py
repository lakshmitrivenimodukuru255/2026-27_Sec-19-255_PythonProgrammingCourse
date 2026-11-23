def rectangle_stats(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

area, perimeter = rectangle_stats(10, 5)
print("Area:", area)
print("Perimeter:", perimeter)
