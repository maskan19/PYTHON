import cv2

img = cv2.imread('image/blue.png', 1)
print(img)

cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

