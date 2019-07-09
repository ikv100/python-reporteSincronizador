
import json

ruta = 'D:\\codigos\\python\\A_pass\\pass.json'
suscriptores = []
dic = {"mail":"", "pass": "", "text": ""}


def cargar_datos(ruta):
    with open(ruta) as contenido:

        datosAlmacenados = json.load(contenido)

        for correo in datosAlmacenados["configuracion"]:
            #print(correo.get('mail'))
            #print(correo.get('pass'))
            #lista.append(correo.get('mail'))
            #lista.append(correo.get('pass'))
            #lista.append(correo.get('text'))
            dic["mail"] = (correo.get('mail'))
            dic["pass"] = (correo.get('pass'))
            dic["text"] = (correo.get('text'))

        for suscriptor in datosAlmacenados["suscriptores"]:
            print( "Suscriptor ", correo.get('mail') )
            suscriptores.append(suscriptor.get('mail'))

cargar_datos(ruta)