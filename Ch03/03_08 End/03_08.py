import numpy as np
import cv2

import os
print("Current working directory is: {0}".format(os.getcwd()))
os.chdir("C:\\Users\\martynscn\\Desktop\\LinkedIn_\
Learning\\OpenCV for python developers\\Ex_Files_OpenCV_Python_\
Dev\\Exercise Files\\Ch03\\03_08 End")
print("Current working directory is: {0}".format(os.getcwd()))

img = cv2.imread("tomatoes.jpg",1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res,thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh",thresh)

edges = cv2.Canny(img, 100, 70)
cv2.imshow("Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()