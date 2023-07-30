def contour_area(contour):
    area = 0.0
    n = len(contour)

    for i in range(n):
        x1, y1 = contour[i]
        x2, y2 = contour[(i + 1) % n]

        area += (x1 * y2) - (x2 * y1)

    return abs(area) / 2

# Example usage
contour = [[0, 0], [0, 10], [10, 10], [10, 0]]
area = contour_area(contour)
print("Area: ", area)