import cv2
import numpy as np
### Resizing and Cropping ###
img = cv2.imread("Data/cat.jpg")
print(img.shape)
img_reshape = cv2.resize(img, (400,400))
img_cropped = img_reshape[0:300, 100:300]
cv2.imshow("Resized_imgage", img_reshape)
cv2.imshow("Cropped_imgage", img_cropped)
cv2.waitKey(0)