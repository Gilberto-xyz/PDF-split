# Pasar muchos archivos pdf a imagenes y guardarlas en una carpeta con el nombre del archivo pdf
import os
from pdf2image import convert_from_path

# Obtener una lista de todos los archivos en la carpeta
archivos = os.listdir()

# Iterar sobre cada archivo en la carpeta
for archivo in archivos:
    # Comprobar si el archivo es un PDF
    if archivo.endswith('.pdf'):
        # Crear una nueva carpeta con el mismo nombre que el archivo PDF
        nombre_carpeta = os.path.splitext(archivo)[0]
        os.makedirs(nombre_carpeta, exist_ok=True)
        
        # Convertir el archivo PDF a imágenes
        archivo_pdf = convert_from_path(archivo)
        for paginas in range(2, len(archivo_pdf)-1):
            archivo_pdf[paginas].save(f'{nombre_carpeta}/pagina{paginas}.jpg', 'JPEG')
