import cv2
# TODO this code is to read and display images
img = cv2.imread("Data/pic.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)

# TODO this code is to read and display videos
cap = cv2.VideoCapture("Data/test.mp4")
while True:
    sucues, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# TODO this code is to access webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)
cap.set(10,150)
while True:
    sucues, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
