import cv2
import numpy as np
### Basic functions of OpenCV ###
kernel = np.ones((5,5), np.uint8)
pic = cv2.imread("Data/cat.jpg")
img = cv2.resize(pic, (300,300))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img, (7,7), 0)
img_canny = cv2.Canny(img, 100,100)
img_dialiation = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_dialiation, kernel, iterations=1)
#cv2.imshow("output", img)
#cv2.imshow("Grey_image", img_gray)
#cv2.imshow("Blur_image", img_blur)
cv2.imshow("Canny_image", img_canny)
cv2.imshow("Dialation_image", img_dialiation)
cv2.imshow("Eroded_image", img_eroded)
cv2.waitKey(0)