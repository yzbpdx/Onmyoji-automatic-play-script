import cv2

img = cv2.imread(r"D:\565958399\FileRecv\MobileFile\1645693633048.jpg")
print(img.shape)
cropped = img[100:1978, 0:4225]
cv2.imshow("1", cropped)
cv2.imwrite(r"D:\565958399\FileRecv\MobileFile\4.jpg", cropped)
cv2.waitKey(0)