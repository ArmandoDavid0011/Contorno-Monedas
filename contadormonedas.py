#Ingresar Datos
from cv2 import cv2
import numpy as np

valorGauss=3
valorKernel=3
#Matrices de 3x3

original=cv2.imread('W:/Documentos/CURSOS/PYTHON/Proyecto Python RF/Curso/MonedasContorno/monedassoles.jpg') #variable de la moneda
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(valorGauss, valorGauss), 0)
canny=cv2.Canny(gauss, 60,100)
kernel=np.ones((valorKernel, valorKernel),np.uint8) #trabajando con NUMPY
cierre=cv2.morphologyEx(canny, cv2.MORPH_CLOSE ,kernel)

contornos, jerarquia=cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original, contornos, -1, (0,0,255),2)
#Mostrar datos 'Resultado'
cv2.imshow("GRISES", gris)
cv2.imshow("GAUSS", gauss)
cv2.imshow("CANNY", canny)
cv2.imshow("KERNEL", kernel)
cv2.imshow("CIERRE", cierre)
cv2.imshow("Resultado", original)
cv2.waitKey(0)