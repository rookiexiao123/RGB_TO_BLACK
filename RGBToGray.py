#-*- coding:utf-8 -*-
import cv2
import os

path = '/home/xhz/文档/test/JPEGImages'
savepath = '/home/xhz/文档/test/Image/'
count = 0

for file in os.listdir(path):
	count+=1
	img_path = path+ '/'+ file
	#读取图片
	img = cv2.imread(img_path)
	#转为灰度图
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#高斯滤波
	img_GaussianBlur=cv2.GaussianBlur(img_gray, (5,5), 0)
	#保存图片
	cv2.imwrite(savepath + str(file), img_GaussianBlur)
	#cv2.imshow('GRAY', img_gray)
	print(count)
	#cv2.waitKey(0)

#打印文件夹下面文件数
print(count)
#print(os.listdir(path))显示文件夹下面文件名

