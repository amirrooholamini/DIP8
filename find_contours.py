import cv2
import numpy as np

def findContours(image):
    contours = []
    rows, cols = image.shape[:2]
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if image[row, col] == 255 and (row, col) not in visited:
                contour = []
                stack = [(row, col)]

                while stack:
                    curr_row, curr_col = stack.pop()
                    visited.add((curr_row, curr_col))
                    contour.append((curr_row, curr_col))

                    neighbors = [(curr_row - 1, curr_col), (curr_row + 1, curr_col),(curr_row, curr_col - 1), (curr_row, curr_col + 1)]

                    for neighbor_row, neighbor_col in neighbors:
                        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                            if image[neighbor_row, neighbor_col] == 255 and (neighbor_row, neighbor_col) not in visited:
                                stack.append((neighbor_row, neighbor_col))

                contours.append(contour)

    return contours


image = cv2.imread("resources/find_contours.jpg", cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

contours = findContours(binary_image)
canvas = np.zeros_like(image)

for contour in contours:
    for point in contour:
        canvas[point[0], point[1]] = 120

cv2.imshow("Contours", canvas)
cv2.waitKey(0)