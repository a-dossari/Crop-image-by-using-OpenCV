import cv2
import numpy as np

img = cv2.imread('example.jpg')

width = 430
height = 595
p1 = np.float32([[1072, 256], [1480, 191], [1092, 850], [1519, 852]])
p2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(p1, p2)
imgcropped = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("OriginalImage", img)
cv2.imshow("CroppedImage", imgcropped)

cv2.waitkey(0)




