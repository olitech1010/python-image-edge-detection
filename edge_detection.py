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

#to close  all windows when a key is pressed
cv2.waitKey(0)  
cv2.destroyAllWindows()



# 2. LANDSCAPE IMAGE
# =============================
img2 = cv2.imread("landscape.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original - Landscape", img2)

edges1 = cv2.Canny(img2, 50, 150)
cv2.imshow("Canny 50-150 - Landscape", edges1)

edges2 = cv2.Canny(img2, 100, 200)
cv2.imshow("Canny 100-200 - Landscape", edges2)

edges3 = cv2.Canny(img2, 150, 300)
cv2.imshow("Canny 150-300 - Landscape", edges3)

sobel = apply_sobel(img2)
cv2.imshow("Sobel - Landscape", sobel)

cv2.waitKey(0)  # press any key
cv2.destroyAllWindows()



# 3. FACE IMAGE

img3 = cv2.imread("face.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original - Face", img3)

edges1 = cv2.Canny(img3, 50, 150)
cv2.imshow("Canny 50-150 - Face", edges1)

edges2 = cv2.Canny(img3, 100, 200)
cv2.imshow("Canny 100-200 - Face", edges2)

edges3 = cv2.Canny(img3, 150, 300)
cv2.imshow("Canny 150-300 - Face", edges3)

sobel = apply_sobel(img3)
cv2.imshow("Sobel - Face", sobel)

cv2.waitKey(0)  # press any key
cv2.destroyAllWindows()


