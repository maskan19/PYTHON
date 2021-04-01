import cv2

img = cv2.imread('image/red.png', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img_gray)

cv2.imshow('Test Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

