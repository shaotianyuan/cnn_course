import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('homework.jpeg')

def my_show(i):
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
    plt.show()

bg_color = [188,129,36]
threshold = 8500


def calc_diff(pixel):
    return (pixel[0]-bg_color[0])**2 + (pixel[1]-bg_color[1])**2 + (pixel[2]-bg_color[2])**2

def background(picture):
    h, w = picture.shape[0:2]
    for i in range(h):
        for j in range(w):
            if calc_diff(picture[i][j]) < threshold:
                picture[i][j][0] = 255
                picture[i][j][1] = 255
                picture[i][j][2] = 255

background(img)
my_show(img)

cv2.imwrite('result.png',img)