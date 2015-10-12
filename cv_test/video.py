import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')

height , width , layers =  img1.shape

print height

video = cv2.VideoWriter('test2.avi', -1, 1, (width,height))
print video

print video.isOpened()

print "write"

#cv2.WriteFrame(video, img1)

print video.write(img1)
video.write(img2)
video.write(img3)

cv2.destroyAllWindows()


print video.release()

