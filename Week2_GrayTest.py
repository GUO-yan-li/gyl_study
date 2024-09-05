# 导入常用第三方模块
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

# 读取原图像lenna.png
image = cv.imread('E:\GUO_APP\GUO_AI\picture\lenna.png')
# BGR 转为 RGB
image1 = cv.cvtColor(image,cv.COLOR_BGR2RGB)
# 建立 2*2的画布
plt.subplot(221)
# 创建并配置图像
plt.imshow(image1)
# 展示图像image1
plt.show()
# cv.imshow('week2_zy1',image1)

# 灰度化
image = cv.imread('E:\GUO_APP\GUO_AI\picture\lenna.png',0)
cv.imwrite('E:\GUO_APP\GUO_AI\picture\lenna_gray.png',image)
image2 = plt.imread('E:\GUO_APP\GUO_AI\picture\lenna_gray.png')
#cv.imshow('test',image2)
plt.subplot(222)
plt.imshow(image2,cmap='gray')
plt.show()

# 二值化
image3 = np.where(image2 >= 0.5,1,0)
plt.subplot(223)
plt.imshow(image3,cmap='gray')
plt.show()
# 图像等待-直到按任意键消失
cv.waitKey(0)
plt.delaxes(224)
