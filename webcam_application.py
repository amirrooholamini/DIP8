import cv2

# cristiano = cv2.imread("resources/cristiano.png")
# cristiano[170:320,100:200] = [0,0,0]

saeed = cv2.imread("resources/saeed.png")
saeed[150:280,110:220] = [0,0,0]


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    saeed[150:280,110:220] = frame[150:280,110:220]

    if not ret:
        print("Failed to capture frame. Exiting...")
    cv2.imshow('Webcam', saeed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()