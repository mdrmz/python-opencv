import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("a.jpeg")
cv2.blur(img,(10,10))
i= 50
for i in range(90):
   img[i,106] = [255, 255, 255]

for j in range(90):
    img[90,j] = [255, 255, 255]

plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
