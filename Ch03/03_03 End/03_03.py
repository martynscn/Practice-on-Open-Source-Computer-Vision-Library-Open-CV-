import numpy as np
import cv2

import os
print("Current working directory is: {0}".format(os.getcwd()))
os.chdir("C:\\Users\\martynscn\\Desktop\\LinkedIn_\
Learning\\OpenCV for python developers\\Ex_Files_OpenCV_Python_\
Dev\\Exercise Files\\Ch03\\03_03 End")
print("Current working directory is: {0}".format(os.getcwd()))

img = cv2.imread('sudoku.png',0)
cv2.imshow("Original",img)

ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary",thresh_basic)

thres_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Threshold",thres_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()