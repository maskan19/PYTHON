import cv2
import numpy as np

grayImg = cv2.imread('image/lena.png', cv2.IMREAD_GRAYSCALE) 
cv2.imwrite('image/graylena.jpg', grayImg) 
cv2.imshow('gray', grayImg) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

arr = [
        [0,1,1,1,1,0],
        [0,1,1,0,1,0],
        [1,1,0,1,1,1],
        [1,1,0,0,1,1],
        [1,1,0,1,0,0]
    ]
arr_n = np.array(arr)*255
print(arr_n)

cv2.imwrite('image/arr.jpg', arr_n) 
cv2.waitKey(0) 
cv2.destroyAllWindows()