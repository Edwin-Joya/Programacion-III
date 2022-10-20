#import os
#os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/bin")
#importar librerias
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os
from flask import Flask, render_template, request

#leer datos de entrenamiento
temperaturas = pd.read_csv("G:/Universidad/PROGRAMACION III/PARCIAL/grados.csv", sep=";")
print(temperaturas["celsius"], temperaturas["kelvin"])

#graficar datos
sb.barplot(temperaturas, x="celsius", y="kelvin")
plt.show()

#datos de entrada y salida
celsius = temperaturas["kelvin"]
fahrenheit = temperaturas["celsius"]


#Modelo de entrenamiento
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compilar modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')


#Entrenar el modelo
epocas = modelo.fit(celsius, fahrenheit, epochs=300, verbose=1)



app = Flask (__name__)

@app.route('/')

def template():
     
    return render_template("form.html")
    

@app.route('/usuario',methods=['POST'])
def usuario():
         

    nombreUser = request.form[nombreUser + "</h1>"]

if __name__ == '__main__':
     app.run(debug=True)




#Hacer predicciones... Verificar si el resultado es el esperado
f = modelo.predict([5778])
print(f[0][0])