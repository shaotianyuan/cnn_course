import cv2
import numpy as np
import matplotlib.pyplot as plt

def my_show(i):
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
    plt.show()

img = cv2.imread('homework.jpeg')

bg_color = [188,129,36]

B, G, R = cv2.split(img)
B = B.astype('uint32')
G = G.astype('uint32')
R = R.astype('uint32')

temp = (B - bg_color[0]) ** 2 + (G - bg_color[1]) ** 2 + (R - bg_color[2]) ** 2
img[temp < 8500] = 255

my_show(img)

cv2.imwrite('result.png',img)
