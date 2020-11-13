#Integrantes
#A01653368 José Andrés Miguel Martínez
#A01730698 Francisco Cancino Sastré
#A00821522 Juan Carlos Garza Sáncez
#A00818291 Ian Airy Suárez Barrientos
#A01244565 Cristian Palma  Martinez
import cv2
import numpy as np
import time


# read image
img = cv2.imread('rayo.jpg')
img = cv2.resize(img, (540, 540))
cv2.imshow('orignal',img)
sigma = 2
ksize = sigma*6+1
#gaussian Blur
img = cv2.cv2.GaussianBlur(img,(ksize,ksize),sigma)

t1 = 0
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#image in HSV space
img_BW  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#image in gray scale
img_t = (img_HSV, img_BW) # tuple of diferetn spactrum

refPt = []#save the cuadran

def mouse_click(event, x, y,flags, param):
	global t1
	t1 =time.time()
	# to check if left mouse
	# button was clicked
	global refPt
	#only check the x,y values of the img
	if event == cv2.EVENT_LBUTTONDOWN:

		#print('los valroes de de x={} y={}'.format(x,y))
		refPt = [(x,y)]
		#crooping = True
	if event == cv2.EVENT_LBUTTONUP:
		refPt.append((x,y))
		#crooping = False
		#print('los valroes de de x={} y={}'.format(x,y))
		if(x==refPt[0][0] or y == refPt[0][1]):
			pass
		else:
			filter_area(refPt)


def filter_area(list_area):
	global img_t
	global img

	list_stad =[]
	#x , y values of the img [y;col,x:rows]
	x1 , y1 = list_area[0]
	x2 , y2 = list_area[1]
	x_max = max(x1, x2)
	y_max = max(y1, y2)
	x_min = min(x1, x2)
	y_min = min(y1, y2)

	#black and white
	imgCopy = img_t[1][y_min:y_max,x_min:x_max]
	mean = np.mean(imgCopy)
	median = np.median(imgCopy)
	max_v = np.max(imgCopy)
	min_v = np.min(imgCopy)
	std   = np.std(imgCopy)

	aux = {'Type':'GRAY_SCALE','mean' : mean, 'median' : median, 'max': max_v,
	 	   'min':min_v, 'std' : std}
	list_stad.append(aux)

	for i in range(0,3):
		imgCopy = img_t[0][y_min:y_max,x_min:x_max,i]
		#gurada H,S,V
		mean = np.mean(imgCopy)
		median = np.median(imgCopy)
		max_v = np.max(imgCopy)
		min_v = np.min(imgCopy)
		std   = np.std(imgCopy)
		if i == 0:
			tipe = 'H'
		elif i == 1:
			tipe = 'S'
		else:
			tipe = 'V'
		aux = {'Channel':tipe,'mean' : mean, 'median' : median, 'max': max_v,
		'min':min_v, 'std' : std}
		list_stad.append(aux)
	filter_color(list_stad)

	# #add color one in HSV
	# #write_tex(sta)
def filter_color(list_stad):
	global img_t
	global img
	img2 = np.copy(img)
	lower_th = [list_stad[1].get('min'),list_stad[2].get('min'),
		          list_stad[3].get('min')]
	upper_th = [list_stad[1].get('max'),list_stad[2].get('max'),
		          list_stad[3].get('max')]

	# umbral_std = np.array((list_stad[1].get('std'),
	# 	                   list_stad[2].get('std'),list_stad[3].get('std')) ,np.uint8)
	# umbral_mean = np.array((list_stad[1].get('mean'),
	# 	                   list_stad[2].get('mean'),list_stad[3].get('mean')) ,np.uint8)
	lower_th = np.array(lower_th, np.uint8)
	upper_th = np.array(upper_th, np.uint8)
	# print(upper_th)
	# print(lower_th)

	mask = cv2.inRange(img_t[0], lower_th, upper_th)

	#cv2.imshow('mask1',mask)
	# mask2 = cv2.inRange(img_t[0],umbral_std,umbral_mean)
	# mask = mask + mask2
	res  = cv2.bitwise_and(img2, img2, mask=mask)
	cv2.imshow('filter_color_img',res)
	#####black and white
	bw_img = np.copy(img_t[1])
	bw_img[bw_img<list_stad[0].get('min')]=0
	bw_img[bw_img>list_stad[0].get('max')]=0
	cv2.imshow('black and white',bw_img)
	t2 = time.time()
	print('Time ',t2-t1)

	#hue = np.where(np.logical_and(hue<120, hue>105), 110, 250)




cv2.setMouseCallback('orignal', mouse_click)


cv2.waitKey(0)
cv2.destroyAllWindows()
