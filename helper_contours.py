import cv2
import numpy as np

def calculate_iou(contour1, contour2):
    # Calculate the intersection rectangle
    x1 = max(cv2.boundingRect(contour1)[0], cv2.boundingRect(contour2)[0])
    y1 = max(cv2.boundingRect(contour1)[1], cv2.boundingRect(contour2)[1])
    x2 = min(cv2.boundingRect(contour1)[0] + cv2.boundingRect(contour1)[2],
             cv2.boundingRect(contour2)[0] + cv2.boundingRect(contour2)[2])
    y2 = min(cv2.boundingRect(contour1)[1] + cv2.boundingRect(contour1)[3],
             cv2.boundingRect(contour2)[1] + cv2.boundingRect(contour2)[3])

    # If there is no intersection, return 0
    if x2 <= x1 or y2 <= y1:
        return 0.0

    # Calculate the areas of each contour and the intersection
    area1 = cv2.contourArea(contour1)
    area2 = cv2.contourArea(contour2)
    intersection_area = cv2.contourArea(np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]]))

    # Calculate IoU
    iou = intersection_area / (area1 + area2 - intersection_area)
    return iou

def merge_similar_contours(contours):
    merged_contours = []
    for contour in contours:
        add_contour = True

        for merged_contour in merged_contours:
            iou = calculate_iou(contour, merged_contour)
            
            if iou > 0.9:
                # Merge the contour with the existing one
                merged_contour = np.concatenate((merged_contour, contour))
                add_contour = False
                break

        if add_contour:
            # If no match found, add the contour as a new merged contour
            merged_contours.append(contour)

    return merged_contours

def clean_contours(contours, R,C , r1,c1, r2,c2):
    # r1,c1 = R//100, C//100
    # r2,c2 = R//3, C//3 
    real_contours = []
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        if w*h > r1*c1 and w*h < r2*c2 :
            if w/h < 1.3  and w/h > 0.7:
                if x > 0.1*R and x<0.9*R and y > 0.1*C and y<0.9*C:
                    real_contours.append(contour)
    while True:
        remove = False
        for i in range(len(real_contours)-1):
            x1,y1,w1,h1 = cv2.boundingRect(real_contours[i])
            for j in range(i+1, len(real_contours)):
                x2,y2,w2,h2 = cv2.boundingRect(real_contours[j])
                if x2 >= x1 and w2<=w1 and y2 >= y1 and h2<=h1:
                    real_contours.pop(j)
                    remove = True
                    break
            if remove:
                break
        if not remove:
            break
    return real_contours
    