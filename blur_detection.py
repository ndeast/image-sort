import cv2

threshold = 100.0

def laplacian_variance(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def image_size(image):
    dimensions = image.shape
    return image.shape[0] * image.shape[1]

image = cv2.imread('images/ferrari800600.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = "Not Blurry"

fm = laplacian_variance(gray)

if (fm < threshold):
    text = "Blurry"

print(text)
print(fm)
print(image_size(image))

