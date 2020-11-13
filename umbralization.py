#Integrantes
#A01653368 José Andrés Miguel Martínez
#A01730698 Francisco Cancino Sastré
#A00821522 Juan Carlos Garza Sáncez
#A00818291 Ian Airy Suárez Barrientos
#A01244565 Cristian Palma  Martinez
import cv2

#value above which pixel values will be set to max_value
#value to which pixels above threshold will be set
#thresholding_Img the img in binary
img = cv2.imread('rayo.jpg',0)
img = cv2.resize(img, (540, 540))

def thresholding_Img(img):
  max_value = 255
  threshold = int(input('Set the value of the threshold>> '))
  ret, img_binary = cv2.threshold(img, threshold, max_value, cv2.THRESH_BINARY)
  return img_binary

img = thresholding_Img(img)
cv2.imshow('image', img)
cv2.waitKey(0)
