import cv2

img = cv2.imread('image/lena.png', 1)
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
print(img)

cv2.imshow('Test Image', img90)
cv2.waitKey(0)
cv2.destroyAllWindows()

