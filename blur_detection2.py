import imutils
import cv2
import os
images = list()

path = '/Users/Erik/Documents/GitHub/imagesort/TestImages'
for filename in os.listdir(path):
    images.append(tuple((filename, cv2.imread(path + filename))))

print(images)

pic = cv2.imread(images[1][1])

cv2.imshow('image', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()



