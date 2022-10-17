from xml.dom import HierarchyRequestErr
import cv2
import numpy as np       #安装两个库

path='C:/Users/admin/Desktop/VisualStudio/GitHub/red_bluepicture.jpg'  #导入图片（路径只能有英文）
img=cv2.imread(path)

gau = cv2.GaussianBlur(img,(3,3),0)      #将原图像进行高斯模糊处理

img_hsv = cv2.cvtColor(gau,cv2.COLOR_BGR2HSV)   #BGR转HSV

ero = cv2.erode(img_hsv,None,iterations=1)      #腐蚀化

hsv_l=np.array([50,100,100])          #HSV阈值
hsv_h=np.array([120,255,255])
mask=cv2.inRange(img_hsv,hsv_l,hsv_h)   #二值化（去除背景部分）
med=cv2.medianBlur(mask,7)      #图像平滑（中值滤波）

contours,Hierarchy = cv2.findContours(med,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)     #轮廓检测，图像绘制
cv2.drawContours(img,contours,-1,(0,255,255),3)


cv2.imshow("red_bluepicture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
