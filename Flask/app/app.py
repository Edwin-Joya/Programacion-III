import face_recognition
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializar el mensaje en blanco
    #message = ""
    return render_template('index.html')



    # Si se ha enviado el formulario
    if request.method == 'POST':
        # Obtener la imagen subida
        image = request.files['image']

        # Cargar la imagen en memoria
        image_data = face_recognition.load_image_file(image)

        # Cargar la imagen de referencia en memoria
        image1 = face_recognition.load_image_file("./static/image1.jpg")

        # Detectar rostros en las imágenes
        face_locations1 = face_recognition.face_locations(image1)
        face_locations2 = face_recognition.face_locations(image_data)

        # Verificar que solo se detecte un rostro en cada imagen
        if len(face_locations1) != 1 or len(face_locations2) != 1:
            message = "Error: las imágenes deben contener exactamente un rostro cada una"
        else:
            # Obtener las características faciales de cada rostro
            face_encodings1 = face_recognition.face_encodings(image1, face_locations1)[0]
            face_encodings2 = face_recognition.face_encodings(image_data, face_locations2)[0]

            # Comparar las características faciales de los rostros
            results = face_recognition.compare_faces([face_encodings1], face_encodings2)

            # Establecer el mensaje en función del resultado de la comparación
            if results[0]:
                message = "Las imágenes contienen la misma persona"
            else:
                message = "Las imágenes NO contienen la misma persona"

    # Mostrar el archivo HTML con los resultados
    return render_template('index.html', message=message, image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)