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



