"""
Integrantes
A01653368 José Andrés Miguel Martínez
A01730698 Francisco Cancino Sastré
A00821522 Juan Carlos Garza Sáncez
A00818291 Ian Airy Suárez Barrientos
A01244565 Cristian Palma  Martinez

"""
import numpy as np
import cv2 as cv

#Funcion para dibujar circulos en imagen y plot
def onclick(event, x, y, flags, param):
    if event ==cv.EVENT_LBUTTONDBLCLK:
        #Obtiene valor en rgb del pixel
        global r,g,b,img
        r,g,b = img[x,y]
        #Dibuja circulo
        cv.circle(img, (x, y), 5,(0,0,255), 2)
        cv.imshow("img", cv.cvtColor(img, cv.COLOR_BGR2RGB))
        ##temos que marcar en cambas valor 200 
        Azul = DrawHist(histb,(255,0,20),y)
        Azul=cv.resize(Azul, (512,512))
        cv.imshow("Azul",Azul)
       
        Rojo = DrawHist(histr,(0,0,255),y)
        Rojo=cv.resize(Rojo, (512,512))
        cv.imshow("Rojo",Rojo)

        Verde = DrawHist(histg,(0,255,0),y)
        Verde=cv.resize(Verde, (512,512))
        cv.imshow("Verde",Verde)

#Funcion para crear histograms de acuerdo al histograma que se recibe y el color a dibujarla


def DrawHist (histo,coolor,new):
    j=0
    maxHistR =int(np.max(histo))
    cambas = 255*np.ones((maxHistR,256*4,3), dtype= np.uint8)
    for i  in range(len(histo)):
        val =histo[i]
        tam = int(val)
        if i==new:
            cv.line(cambas, pt1=(j,maxHistR),pt2=(j,maxHistR-tam), color=(0,0,0),thickness=10)
        else:
            cv.line(cambas, pt1=(j,maxHistR),pt2=(j,maxHistR-tam), color=coolor,thickness=2)
        j +=4
    return cambas       


#Carga img y la convierte a 512x512
img=np.array(cv.imread('rayo.jpg'))
img=cv.resize(img, (512,512))

#Muestra img y cambia el display a 600x600
cv.imshow("img", img)
cv.resizeWindow('img',512,512)


img=cv.cvtColor(img, cv.COLOR_BGR2RGB)


#convierte rgb a gbr, luego separa los colores
r,g,b=cv.split(img) #separa la imagen para el histograma

#Histograma y su plot
histr=cv.calcHist([r], [0], None, [256], [0, 256])
histg=cv.calcHist([g], [0], None, [256], [0, 256])
histb=cv.calcHist([b], [0], None, [256], [0, 256])


Azul = DrawHist(histb,(255,0,0),0)
Azul=cv.resize(Azul, (512,512))
cv.imshow("Azul",Azul)

Rojo = DrawHist(histr,(0,0,255),0)
Rojo=cv.resize(Rojo, (512,512))
cv.imshow("Rojo",Rojo)

Verde = DrawHist(histg,(0,255,0),0)
Verde=cv.resize(Verde, (512,512))
cv.imshow("Verde",Verde)



#Trigger para mandar a llamar la funcion de dibujar circulo
cv.setMouseCallback('img', onclick)


#plt.show()
#Wait y limpia
cv.waitKey(0)
cv.destroyAllWindows()
