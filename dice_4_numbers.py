import cv2

img = cv2.imread('resources/dice4.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detected_edges = cv2.Canny(gray_img,9, 150, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
R,C,Z = img.shape

close = cv2.morphologyEx(detected_edges, cv2.MORPH_CLOSE, kernel, iterations=2)
circles = cv2.HoughCircles(close, cv2.HOUGH_GRADIENT, 1.1, 5, param1=50, param2=30, minRadius=0, maxRadius=90)

for circle in circles[0]:
    center = (int(circle[0]), int(circle[1]))
    radius = int(circle[2])
    cv2.circle(img,center,radius,(255,100,0),3)

cv2.putText(img, str(len(circles[0])), (C//2 - 10, 130), cv2.FONT_HERSHEY_SIMPLEX, 2,(120, 0, 10), 2)
cv2.imwrite("outputs/4.jpg", img)
print(len(circles))
cv2.imshow("1", img)
cv2.waitKey()