'''
                **Requirements**

- Install open-CV library from "pip install opencv-python"

'''

import cv2

image = cv2.imread(r"C:\Users\ROHIT\Desktop\img.jpg")
cv2.imshow(r"C:\Users\ROHIT\Desktop\img", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(r"C:\Users\ROHIT\Desktop\img", gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.imshow(r"C:\Users\ROHIT\Desktop\img_inverted", inverted_image)
cv2.waitKey()

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow(r"C:\Users\ROHIT\Desktop\img Sktech", pencil_sketch)
cv2.waitKey(0)
cv2.imshow(r"C:\Users\ROHIT\Desktop\img original", image)
cv2.imshow(r"C:\Users\ROHIT\Desktop\img sketch pencil", pencil_sketch)
cv2.waitKey(0)
