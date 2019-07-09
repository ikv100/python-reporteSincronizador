
from lib import miniDB
from lib import correo
    
if __name__ == '__main__':
    print("Main ejecutandose")
    #leeArchivos.cargar_datos( leeArchivos.ruta )

    #correo.envioCorreo( miniDB.dic["mail"], miniDB.dic["pass"], miniDB.dic["mail"], "# URGENTE #", "Usando diccionario" )

    for suscriptor in miniDB.suscriptores:
        print("Desde el main ", suscriptor)
        payload = "Este es un mensaje personalizado para " + suscriptor
        correo.envioCorreo( miniDB.dic["mail"], miniDB.dic["pass"], suscriptor, "# URGENTE #", payload )