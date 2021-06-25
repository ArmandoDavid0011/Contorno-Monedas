from cv2 import cv2
imagen=cv2.imread('W:/Documentos/CURSOS/PYTHON/Proyecto Python RF/Curso/MonedasContorno/contorno.jpg')
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral=cv2.threshold(grises,100, 255, cv2.THRESH_BINARY)
contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(65,105.225),3)

# Este punto del codigo es para mostrar imagenes.

#cv2.imshow('Escala de grises',grises)
cv2.imshow('Imagen Original',imagen)
#cv2.imshow('Imagen con umbral',umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
