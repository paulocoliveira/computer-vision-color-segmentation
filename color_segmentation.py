import cv2
import numpy as np

# convert an image to an array
image = cv2.imread("colors.jpg")

#lower and upper limits of the desired color (red)
lower_range = np.array([0,0,200])
upper_range = np.array([10,10,255])

#create a mask using ranges
mask = cv2.inRange(image, lower_range, upper_range)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("image", image)
cv2.imshow("mask", mask)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows