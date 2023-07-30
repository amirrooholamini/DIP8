import cv2
import numpy as np
from helper_contours import clean_contours, merge_similar_contours

for i in range(1,4):
    name = f"dice{i}.png"
    path = "resources/" + name

    main_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

    threshold = 200
    if i == 3:
        threshold = 150
    elif i == 4:
        threshold = 50

    _, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    contours, h = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    R,C = img_thresh.shape
    r,c = R//10,C//10

    total = 0
    result = ""
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > r*c:
            total += 1
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(main_image, (x, y), (x + w, y + h), (255, 255, 0), 2)
            
            dice = img_thresh[y:y+h, x:x+w]
            if np.sum(dice == 255) > np.sum(dice == 0): # dice is white
                dice = 255 - dice
            R1,C1 = dice.shape
            sub_contours, h = cv2.findContours(dice, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            if i == 4 :
                r1,c1 = R1//100, C1//100
            else:
                r1,c1 = R1//10, C1//10

            r2,c2 = R1//3 , C1//3
            sub_contours = clean_contours(sub_contours,R1,C1, r1,c1,r2,c2)
            sub_contours = merge_similar_contours(sub_contours)
            number = len(sub_contours)
            result += str(number) + ","
            cv2.putText(main_image, str(number), (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2)
            for sub_contour in sub_contours:
                x1,y1,w1,h1 = cv2.boundingRect(sub_contour)
                cv2.rectangle(main_image, (x + x1, y + y1), (x + x1 + w1, y + y1 + h1), (255, 0, 255), 2)
                
    result = result[:len(result)-1]
    result = name + ": " + str(total) + " dices found-> " + result
    cv2.imwrite("outputs/"+str(i) + ".jpg", main_image)
    cv2.imshow(name ,main_image)
    cv2.waitKey()
    print(result)
