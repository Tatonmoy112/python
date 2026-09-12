import cv2
src=cv2.imread("image001.jpeg",cv2.IMREAD_UNCHANGED)
cv2.imshow("random",src)

scale_per=50

new_width=int(src.shape[1] *scale_per/100)
new_height=int(src.shape[0] *scale_per/100)

new_jpeg=cv2.resize(src,(new_width,new_height))

cv2.imwrite("New001.png",new_jpeg)
cv2.waitKey(0)
