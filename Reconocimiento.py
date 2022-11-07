import cv2

# Cargar el preset de cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #CARGA LA LIBRERIA DE IMAGENES YA CLASIFICADAS DE LAS CUALES LA IA APRENDE

# Cargamos la imagen a escanear
img = cv2.imread('JeffBezos.jpeg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #PASA LA IMAGEN A ESCALA DE GRISES

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4) #DETECTA LAS CARAS

# Dadas las cordenadas Punto1=x,y    Punto2=x+anchura,y+altura generar un rectangulo alrededor de la cara.
for (x, y, w, h) in faces: #x, y, widht height
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Inteligencia Artificial: Detector de rostros.', img)
cv2.waitKey()
cv2.imwrite("ia.jpg",img)