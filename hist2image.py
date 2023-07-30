import cv2
import numpy as np
import math
import random

def create_image(hist):
    s = np.sum(hist)
    print(s)
    sqrt = math.sqrt(s)
    if sqrt == round(sqrt):
        r = c = sqrt
    else:
        start_r = start_c = int(sqrt//10)
        end_r = end_c = int(10 * sqrt)
        r = c = None
        for i in range(start_r,end_r + 1):
            for j in range(start_c, end_c + 1):
                if i*j == s:
                    if r is None or abs(r-c) > abs(i-j):
                        r = i
                        c = j

    if r is None or c is None:
        return None
    image = np.zeros((r,c), dtype=np.uint8)
    column = 0        
    for i in range(r):
        for j in range(c):
            while True:
                if hist[column] > 0:
                    image[i,j] = column
                    hist[column] -= 1
                    break
                else:
                    column+=1
    return image
        
    


hist = []
for i in range(256):
    hist.append((random.randint(0,1000)))

img = create_image(hist)
if img is None:
    print("can not find size for this histogram")
else:
    cv2.imshow("1", img)
    cv2.waitKey()
