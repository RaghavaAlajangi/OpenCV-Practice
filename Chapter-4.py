import cv2
import numpy as np
### Shapes and Texts ###
img = np.zeros((512,512,3), np.uint8)
cv2.line(img,(0,0), (img.shape[1], img.shape[0]) , (0,0,255),3)
cv2.rectangle(img, (0,0), (300,400), (0,255,0), 1)
cv2.circle(img, (100,450), 50, (255,0,0), 3)
cv2.putText(img, "Raghava", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
cv2.imshow("image", img)
cv2.waitKey(0)
