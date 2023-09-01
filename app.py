#Importamos flask 
from flask import Flask,jsonify 
import numpy as np
app= Flask(__name__)

#definimos la ruta principal 
@app.route("/")
def  HolFlask():
    return"<h1>¡ Hola Flask! </h1> <hr> "

#definimos una segunda ruta 
@app.route("/notas")
#definimos una tercera ruta     
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")

def notas (nota1=0, nota2=0, nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return jsonify  ({"resultado": resultado})
@app.route("/edades")
@app.route("/edades/<int:edad>")

def edades (edad=0):
    if edad <18:
        r="menor de edad"
    elif (edad<60):
        r="Adulto"
    else:
        r="Adulto mayor"
    return jsonify  ({"resultado": r})
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:colmunas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")

def arreglos(valores=0, columnas=0,filas=0):
    if filas ==0:
        arreglo =np.random.randint(valores,size=columnas)
    else: 
        arreglo= np.random.randint(valores,size=(filas,columnas))
        
    return jsonify  ({"arreglo":arreglo.tolist() })







if __name__=='__main__':
    app.run(debug=True)       
            