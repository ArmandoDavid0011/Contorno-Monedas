from cv2 import cv2 
# Analisis de imagenes
import numpy as np
#Operaciones de matrices
#Trabajar con matrices
def ordenarpuntos(puntos): # Esta es una funcion y se define con un "def"
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist() #Unir o enlazar matrices
    # Cordenadadas definir X y Y; Key sirve para ordenar
    y_order=sorted(n_puntos,key=lambda n_puntos:n_puntos[1]) # El 1 es la Y
    x1_order=y_order[0:2]
    x1_order=sorted(x1_order,key=lambda x1_order:x1_order[0]) # El 0 es la X
    x2_order=y_order[2:4]
    x2_order=sorted(x2_order,key=lambda x2_order:x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]
def alineamiento(imagen,ancho,alto):
    imagen_alineada=None
    grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoumbral,umbral=cv2.threshold(grises, 15,255, cv2.THRESH_BINARY)
    cv2.imshow("umbral", umbral)
    # Se utiliza lo siguiente porque trabajas con una camara externa "cv2.RETR_EXTERNA"
    contorno=cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno=sorted(contorno,key=cv2.contourArea,reverse=True)[:1] # reverse=True es para ordenar de mayor a menar Sorted se utiliza para ordenar matrices
    for c in contorno:
        epsilon=0.01*cv2.arcLength(c, True) # epsilon sirve para encontrar el area. "arc length encontrar el area" 
        approximacion=cv2.approxPolyDP(c,epsilon, True) 
        if len(approximacion)==4: #Aqui se ponen los puntos a declar
            puntos=ordenarpuntos(approximacion)
            #Convertir datos de ancho y altura
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0], [0,alto],[ancho,alto]])
            #Capacidad de la camara desde aqui, metodo de perspectiva
            M = cv2.getPerspectiveTransform(puntos1,puntos2) #Representacion de la parte perspectiva
            imagen_alineada=cv2.warpPerspective(imagen, M,(ancho,alto))#Es para pasar información.
            #Conversión de unidades
    return imagen_alineada
capturevideo=cv2.VideoCapture(0)

while True:
    tipocamara,camara=capturevideo.read()
    if tipocamara==False:
        break # break es para cerrar
    imagen_A6=alineamiento(camara,ancho=480,alto=677) # Proceso de imagen, decir la medida
    if imagen_A6 is not None: # si hay datos o imagen que continue trabajando
        puntos=[]
        imagen_gris=cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagen_gris,(5,5),1) # Aqui se hace desenfoque primer filtro
        #aplicar parte de obtener reseultado
        _,umbral2=cv2.threshold(blur,0,225,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)#aplicar el umbralizado
        #dcv2.imshow("Umbral", umbral2)
        contorno2=cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6, contorno2, -1, (255,0,0),2)
        suma1=0.0
        suma2=0.0 
        for c_2 in contorno2:
            area=cv2.contourArea(c_2)
            #encontrar el centro del circulo
            Momentos = cv2.moments(c_2) 
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            X=int(Momentos["m10"]/Momentos["m00"]) #Momentos de desplazamiento
            Y=int(Momentos["m01"]/Momentos["m00"])
        #Trabajar con las areas
            if area<7900 and area>7100:
                  # Se esta dando el tipo de fuente
                  font=cv2.FONT_HERSHEY_SIMPLEX
                  cv2.putText(imagen_A6,"MXM/0. 0.01",(X,Y), font, .95, (0,255,0),2)
                  suma1=suma1+0.2

            if area<9300 and area>8700:
                  font=cv2.FONT_HERSHEY_SIMPLEX
                  cv2.putText(imagen_A6,"MXM/0. 0.05",(X,Y), font, .95, (0,255,0),2)
                  suma2=suma2+0.1
        total=suma1+suma2
        print("Sumatoria tontal en Centimos", round(total,2))
        cv2.imshow("Imagan_A6", imagen_A6)
        #cv2.imshow("Camara", camara)
    if cv2.waitKey(1)==ord("s"):
      break
capturevideo.release()
cv2.destroyAllWindows()

