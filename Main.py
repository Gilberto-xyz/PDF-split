import os
from pdf2image import convert_from_path

archivos = os.listdir()

# Iterar sobre cada archivo en la carpeta
for archivo in archivos:
    # Verificar si el archivo es un PDF
    if archivo.endswith('.pdf'):
        # Obtener el nombre del archivo sin la extensión
        nombre_archivo = os.path.splitext(archivo)[0]
        os.makedirs(nombre_archivo, exist_ok=True)
        # Convertir el archivo PDF a imágenes
        print(f'Trabajando en {archivo}...')
        imagenes = convert_from_path(archivo)
        # Guardar cada página como una imagen
        for pagina in range(len(imagenes)):
            print(f'Convirtiendo página {pagina}...')
            imagenes[pagina].save(f'{nombre_archivo}/pagina{pagina}.jpg', 'JPEG')
