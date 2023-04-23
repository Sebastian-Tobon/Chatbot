import pickle
import os

def leer_contenido_archivo_binario(ruta_archivo):
    """
    Lee el contenido de un archivo binario.
    
    ruta_archivo: Ruta del archivo binario a leer.
    
    return: Objeto Python recuperado desde un archivo binario.
    """
    if os.path.exists(ruta_archivo):
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'rb') as f:
                return pickle.load(f)
        else:
            return None
    else:
        return None
    
archivo = 'chatbot_model.h5'
    
print(archivo)

resultado = leer_contenido_archivo_binario(archivo)
print (resultado)