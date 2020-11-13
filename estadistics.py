#Integrantes
#A01653368 José Andrés Miguel Martínez
#A01730698 Francisco Cancino Sastré
#A00821522 Juan Carlos Garza Sáncez
#A00818291 Ian Airy Suárez Barrientos
#A01244565 Cristian Palma  Martinez
import cv2
import numpy as np

# read image
img = cv2.imread('rayo.jpg')
img = cv2.resize(img, (540, 540))
cv2.imshow('orignal',img)
sigma = 1
ksize = sigma*6+1
#gaussian Blur
img = cv2.cv2.GaussianBlur(img,(ksize,ksize),sigma)


img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)#image in HSV space
img_BW  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#image in gray scale
img_t = (img_HSV, img_BW) # tuple of diferetn spactrum

refPt = []#save the cuadran

def mouse_click(event, x, y,flags, param):
	# to check if left mouse
	# button was clicked
	global refPt
	#only check the x,y values of the img
	if event == cv2.EVENT_LBUTTONDOWN:

		print('los valroes de de x={} y={}'.format(x,y))
		refPt = [(x,y)]
		#crooping = True
	if event == cv2.EVENT_LBUTTONUP:
		refPt.append((x,y))
		#crooping = False
		print('los valroes de de x={} y={}'.format(x,y))
		if(x==refPt[0][0]):
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
	write_tex(list_stad)




	# #add color one in HSV
	# #write_tex(sta)


def write_tex(stad):

	flag = int(input('To overwrite the file enter 1 >>>'))
	if(flag == 1):
		file = open('stad.txt','a')
		file.write('-------------new masure-------------\n')
	else:
		file = open('stad.txt','w')
		file.write('====================================\n')
		file.write('======stadistics_of_the_image=======\n')

	for i in stad:
		for j,k in i.items():
			text = str(j)+'-> '+str(k)+'\n'
			file.write(text)
	file.close()

cv2.setMouseCallback('orignal', mouse_click)


cv2.waitKey(0)
cv2.destroyAllWindows()


