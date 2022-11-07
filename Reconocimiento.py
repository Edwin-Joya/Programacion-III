import cv2
 
#Cargamos los clasificadores requeridos
face_cascade = cv2.CascadeClassifier('C:/users/edwin/appdata/local/programs/python\python310/lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
 
#Utilizamos un fichero de imagen del disco duro
img = cv2.imread('cara.jpg')
 
while(True):
    #Convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Buscamos las coordenadas de los rostros
    caras = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Dibujamos un rectángulo en las coordenadas de cada rostro
    numCaras = 0
    for (x,y,w,h) in caras:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
        numCaras = numCaras + 1
    #Mostramos la imagen
    cv2.imshow('img',img)
    #Pulsando la tecla "q" salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
print ("Número de caras detectadas: {}".format(numCaras))