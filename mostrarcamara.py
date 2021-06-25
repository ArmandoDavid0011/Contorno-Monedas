import cv2 as cv
capturaVideo=cv.VideoCapture(0) #Para abrir el video en la camara de pc 0 Camaras de PC 1 Camaras de seguridad
if not capturaVideo.isOpened(): # Se hace la toma de decisión
    print ("No se enocontro una camara")
    exit()
while True: #se ejecuta un bucle. 
    tipocamara,camara=capturaVideo.read() #Para inicializar el video
    grises=cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
    cv.imshow("Fn Vivo",grises) # Para abir la camara
    if cv.waitKey(1)==ord("q"): #1 es continuo, presionar "q" para cerrar
        break #Para cerrar   
capturaVideo.release() #Para detener video
cv.destroyAllWindows() #Para destruir las ventanas