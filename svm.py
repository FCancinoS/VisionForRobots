'''
A01730698 Francisco Cancino Sastré
A00821522 Juan Carlos Garza Sánchez
A01653368 José Andrés Miguel Martínez
A00818291 Ian Airy Suárez Barrientos
A01244565 Cristian Ignacio Palma Martinez
'''
from sklearn import svm
x = [
[ 1.28726328e-03,
        9.09567013e-07,
        4.77946008e-10],#star (first object)
[ 7.52147038e-04,
        2.75238503e-10,
        2.67424833e-10],#triangle (second object)
[ 7.96839202e-04,
        2.07613965e-07,
        6.86808737e-16],#rectangle (third object)
[ 2.31031554e-02,
        1.27780793e-04,
        3.52639453e-06]#circle (fourth object)
] 

#x = [[]] 
y = ['estrella azul','triangulo verde','rectangulo naranja','circulo rojo']


def initSVM(x, y):
    global clf
    clf = svm.SVC()
    clf.fit(x, y)

initSVM(x,y); 

moments = [[    
		7.63328744e-04,
        1.52327703e-07,
        6.07346550e-12
       ]] #In this matrix  save the data you gonna use for test your SVM

Respond = clf.predict(moments)
print(Respond);