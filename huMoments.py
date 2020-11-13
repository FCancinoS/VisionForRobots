'''
A01730698 Francisco Cancino Sastré
A00821522 Juan Carlos Garza Sánchez
A01653368 José Andrés Miguel Martínez
A00818291 Ian Airy Suárez Barrientos
A01244565 Cristian Ignacio Palma Martinez
This File returns you the hu moments of the images on the folder you select acoording a color filter you define in 
lower and upper
'''
import sys
import cv2 as cv
import numpy as np
import math
import os
route = 'C:/Users/Franc/Desktop/Ambiente/TrianguloVerde/'
nObj = 1
x=[[]]
def humomenter(imge):
    lower = np.array([0, 179, 0])  
    upper = np.array([127,255,255]) #With lower and upper we apply a filter  by color
    imgHSV = cv.cvtColor(imge, cv.COLOR_BGR2HSV) #  Conversion BGR to HSV
    imgBlur = cv.GaussianBlur(imgHSV, (5, 5), 1) # Elimination of noise
    mask = cv.inRange(imgBlur, lower, upper)  # creation of the mask
    ret, thresh = cv.threshold(mask , 127, 255, 0)# threshold to binarize the image

    moments = cv.moments(thresh) #We obtain the moments
    huMoments = cv.HuMoments(moments)# We obtain Hu Moments
    return huMoments

def getImg(folder, n): # This function read the images and applies dehumomenter
    global x
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder, filename))
        if img is not None:
            x[n].append(humomenter(img))

for n in range(nObj):    
    getImg(route, n)
print(x)

