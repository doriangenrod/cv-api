#!flask/bin/python
# -*- coding: UTF-8 -*-
""" codigo para levantar el servidor
from flask import Flask

app = Flask(__name__)

if __name__=='__main__':
    app.run(debug=True)

"""# fin de codigo para levantar servidor en modo debug

""" codigo para responder con un hola mundo cuando se invoca al servidor y al puerto de desarrollo
from flask import Flask

app = Flask(__name__)

@app.route('/')   #decorador
def index():
    return "Hola mundo cruel!"


if __name__=='__main__':
    app.run(debug=True)

"""#Hasta aqui tenemos una "API" que responde a algo cuando se la invoca

"""Desde aqui respondemos con la estructura de datos que nuestra Api va a responder
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')   #decorador
def index():
    info = {                                                                            # esto es un diccionario que estamos poniendo
        "mensaje" : "Bienvenido a la API del curriculum Vitae de Roberto Canavides.", 
        "acciones" : [
            "GET / curriculum",
            "POST /mensajes"
        ]
    }                                                     # fin del diccionario, esto es lo que va a estar repondiendo nuestra API
    return jsonify(info)                                  # estamos respondiendo un elemento json con acciones y mensajes
                                                          # con GET y POST va a tener una respuesta  


if __name__=='__main__':
    app.run(debug=True)

"""#fin de la estructura con la que responderemos

"""#Desde aqui vamos a agregar la respuesta al metodo GET definido anteriormente
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')   #decorador
def index():
    info = {                                                                            # esto es un diccionario que estamos poniendo
        "mensaje" : "Bienvenido a la API del curriculum Vitae de Roberto Canavides.", 
        "acciones" : [
            "GET / curriculum",
            "POST /mensajes"
        ]
    }                                                     # fin del diccionario, esto es lo que va a estar repondiendo nuestra API
    return jsonify(info)                                  # estamos respondiendo un elemento json con acciones y mensajes
                                                          # con GET y POST va a tener una respuesta  
@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/Tamales.jpg" #tenemos que crear una carpeta que se llame static y pondremos la foto 
    cv = {
        "nombre" : "Roberto",
        "apellido" : "Canavides",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "< describe tu posición>",
            "empresa" : "< nombre de tu empresa >",
            "desde" : "< cuándo empezaste a trabajar >",
            "hasta" : "< si ya no trabajas más, cuándo >",
            "descripcion" : "< detalles >"
        }],
        "educación" : {
            "nivel" : "< nivel de tus estudios >",
            "titulo" : "< nombre de tu carrera >",
            "institucion" : "< dónde estudiaste >",
            "facultad" : "< más detalles >"
        },
        "intereses" : ["python", "apis", "enseñar"],
        "redes" : {
            "github" : "https://github.com/nahueltori",
            "twitter" : "https://twitter.com/nahueltori",
            "Facebook" :"https://facebook.com",
            "linkedin" : "https://www.linkedin.com/in/nahueltori"
        },
        "foto" : url_imagen
    }
    return jsonify(cv)

if __name__=='__main__':
    app.run(debug=True)
"""# fin de agregar el metodo GET

#agregamos el metodo POST
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] #Elimina todos los caracteres de manera que la api envia bien los resultados


@app.route('/')   #decorador
def index():
    info = {                                                                            # esto es un diccionario que estamos poniendo
        "mensaje" : "Bienvenido a la API del curriculum Vitae de Roberto Canavides.", 
        "acciones" : [
            "GET / curriculum",
            "POST /mensajes"
        ]
    }                                                     # fin del diccionario, esto es lo que va a estar repondiendo nuestra API
    return jsonify(info)                                  # estamos respondiendo un elemento json con acciones y mensajes
                                                          # con GET y POST va a tener una respuesta  
@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/Tamales.jpg" #tenemos que crear una carpeta que se llame static y pondremos la foto 
    cv = {
        "nombre" : "Roberto",
        "apellido" : "Canavides",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "< describe tu posición>",
            "empresa" : "< nombre de tu empresa >",
            "desde" : "< cuándo empezaste a trabajar >",
            "hasta" : "< si ya no trabajas más, cuándo >",
            "descripcion" : "< detalles >"
        }],
        "educación" : {
            "nivel" : "< nivel de tus estudios >",
            "titulo" : "< nombre de tu carrera >",
            "institucion" : "< dónde estudiaste >",
            "facultad" : "< más detalles >"
        },
        "intereses" : ["python", "apis", "enseñar"],
        "redes" : {
            "github" : "https://github.com/nahueltori",
            "twitter" : "https://twitter.com/nahueltori",
            "Facebook" :"https://facebook.com",
            "linkedin" : "https://www.linkedin.com/in/nahueltori"
        },
        "foto" : url_imagen
    }
    return jsonify(cv)

@app.route('/mensajes', methods=['POST']) #metodo para enviar informacion atraves de la url Endpoint mensajes
def contacto():
    mensaje = request.get_data()

    if not mensaje:         #verificamos si hay un mensaje o no completo los campos que necesita para funcionar, aqui solo verifica que haya algo

        abort(400, description="Debe enviar su mensaje en el body del POST.") #400 significa bad request

    print("MENSAJE DE CONTACTO: " + str(mensaje))

    return "Gracias por su mensaje."


if __name__=='__main__':
    app.run()

#fin agregar metodo Post
#Tareas para preparar nuestro proyecto para el deploy
#1 app.config['JSONIFY_PRETTYPRINT_REGULAR'] #Elimina todos los caracteres de manera que la api envia bien los resultados
#2 quitar el modo debug app.run(debug=true)
#3 agregar el archivo .gitignore en este archivo le decimos a github que debe ignorar ciertos archivos y carpetas
#4 agregar el archivo requirements.txt esto le dice a heroku que requerimientos necesita para funcionar 
#   con el codigo  pip freeze > requirements.txt se genera en el archivo una lista de todas las librerias que utilizo 
# en el entorno virtual para funcionar, en este caso solo vamosa poner Flask y gunicorn
# Flask es la libreria que usamos para construir este sitio y gunicorn es un navegador web para sitios productivos
#5 particular de Heroku, le dice que es lo que tiene que utilizar para que funcione nuestra app