__author__ = 'linzh'

import numpy as np
import cv2

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('X','V','I','D'), 20.0, (640,480))
img1 = cv2.imread('5.png')

height, width, layers = img1.shape

out = cv2.VideoWriter('output.wmv', cv2.cv.CV_FOURCC('W','M','V','1'), 25.0, (width,height), True)
print out.isOpened()

print height

for i in range(0, 1000):
    print "jpg"
    out.write(img1)

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
