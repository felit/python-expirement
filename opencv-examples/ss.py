import cv2
import numpy as np
filename = "/Users/congsl/Downloads/Learning_OpenCV_3_Computer_Vision_with_Python_Second_Edition_Code/Chapter_8_Code/meanshift.jpg"
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,23,0.04)