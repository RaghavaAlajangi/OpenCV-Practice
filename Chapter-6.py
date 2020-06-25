import cv2
import numpy as np
### Joining images ###
### Stack function, which can join images ###
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
##########################################
pic = cv2.imread("Data/cat.jpg")
img = cv2.resize(pic, (400,400))
img_canny = cv2.Canny(img, 100,100)
img_hor = np.hstack((img,img,img))
img_ver = np.vstack((img,img,img))
# cv2.imshow("Hstacked_image", img_hor)
# cv2.imshow("Vstacked_image", img_ver)
# cv2.waitKey(0)
##########################################
img_H = stackImages(0.5, [img,img,img])
img_V = stackImages(0.5, [[img],[img],[img]])
img_matrix = stackImages(0.5, [[img, img_H, img], [img, img,img_canny]])
cv2.imshow("Hstacked_image", img_H)
cv2.imshow("Vstacked_image", img_V)
cv2.imshow("Matrix_stacked_image", img_matrix)
cv2.waitKey(0)