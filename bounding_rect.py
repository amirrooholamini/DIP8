def bounding_rect(contour):
    min_x, min_y = contour.min(axis=0).ravel()
    max_x, max_y = contour.max(axis=0).ravel()
    width = max_x - min_x
    height = max_y - min_y
    return min_x, min_y, width, height