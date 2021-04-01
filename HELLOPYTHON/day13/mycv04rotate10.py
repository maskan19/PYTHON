import cv2

img = cv2.imread('image/lena.png', 1)
print(img)


M = cv2.getRotationMatrix2D((512/2.0, 512/2.0), #회전 중심
                            -10, # 회전각도(양수 반시계방향, 음수 시계방향)
                            0.5) # 이미지 배율
img_rotation = cv2.warpAffine(img, M, (512, 512))
cv2.imshow("rotation", img_rotation)

cv2.waitKey(0)
cv2.destroyAllWindows()

