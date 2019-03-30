import cv2

threshold = 100.0

image = cv2.imread('images/ferarri.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def laplacian_variance(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

text = "Not Blurry"

fm = laplacian_variance(gray)

if (fm < threshold):
    text = "Blurry"

print(text)
print(fm)