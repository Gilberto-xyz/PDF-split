# Dividir un pdf en Imagenes 

Este código en Python importa los módulos os y convert_from_path de la biblioteca pdf2image. Luego, obtiene una lista de todos los archivos en la carpeta actual y muestra cuántos de ellos son archivos PDF. Después, itera sobre cada archivo en la carpeta y verifica si es un archivo PDF. Si lo es, crea una nueva carpeta con el mismo nombre que el archivo (sin la extensión) y convierte cada página del archivo PDF en una imagen JPEG. Finalmente, guarda cada página como una imagen JPEG en la carpeta creada

Instalarse pdf2image para convertir pdf a imagenes

```pip install pdf2image```

Instalarse scoop para descargar poppler, que nos permite manipular los archivos pdf

Si estas trabajando con anaconda, instalar poppler con el siguiente comando 

```conda install -c conda-forge poppler```



Si estas trabajando con python, instalar scoop con el siguiente comando
```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
 irm get.scoop.sh | iex
 ```
Y luego instalar poppler con:  
```scoop install poppler```
