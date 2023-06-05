# This code loads an image and converts it from BGR to HSV color space using the cvtColor function from OpenCV. 
# It then defines a range of color to detect and creates a mask using this range and the inRange function. 
# The mask is applied to the original image using the bitwise_and function to keep only the pixels that fall within the defined color range. 
# Finally, the result is displayed using imshow and waitKey functions.
#
# By: Caesar R. Watts-Hall
# Date: June 5, 2023

import cv2
import numpy as np

# Load an image
image = cv2.imread("image.jpg")

# Convert the image from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define a range of color to detect
lower_color = np.array([0, 100, 100])
upper_color = np.array([10, 255, 255])

# Create a mask using the defined color range
mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Show the result
cv2.imshow("Result", result)
cv2.waitKey(0)
