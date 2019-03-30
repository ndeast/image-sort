import cv2
import os

threshold = 100.0

def laplacian_variance(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def image_size(image):
    dimensions = image.shape
    return image.shape[0] * image.shape[1]

def print_values(images):
    for image in images:
        print(image[0])
        print('Variance: ' + str(laplacian_variance(image[1])))
        print('Size: ' + str(image_size(image[1])) + '\n')
    return

images = list()

path = os.getcwd() + '\TestImages'

for filename in os.listdir(path):
    images.append(tuple((filename, cv2.imread(path + '\\' + filename))))

print_values(images)

# imshow(name, image)
# cv2.imshow(images[0][0], images[0][1])
# cv2.waitKey(0)
# cv2.destroyAllWindows()


