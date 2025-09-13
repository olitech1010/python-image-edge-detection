# -------------------------------
# Edge Detection Assignment
# BY CLEMENT MENSAH
# -------------------------------

import cv2


# FUNCTION FOR SOBEL OPERATOR

def apply_sobel(img):
    # Sobel in X direction
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    # Sobel in Y direction
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    # Combine both using magnitude
    sobel = cv2.magnitude(sobelx, sobely)
    return sobel



# 1. TEXT IMAGE

img1 = cv2.imread("text.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original - Text", img1)

edges1 = cv2.Canny(img1, 50, 150)
cv2.imshow("Canny 50-150 - Text", edges1)

edges2 = cv2.Canny(img1, 100, 200)
cv2.imshow("Canny 100-200 - Text", edges2)

edges3 = cv2.Canny(img1, 150, 300)
cv2.imshow("Canny 150-300 - Text", edges3)

sobel = apply_sobel(img1)
cv2.imshow("Sobel - Text", sobel)

