#Funciones de los archivos
archivo = open("archivo.txt", "w")#Con el metod write crea el archivo
archivo.close()#Por seguridad se cierran los archivos
archivo.write("Hola amigos")
archivo = open("archivo.txt", "r")#Modo lectura
archivo.read()#Lee toda la informacion 
archivo = open("archivo.txt", "r+")#Modo escritura y lectura
archivo = open("archivo.txt", "a")#Modo append
archivo.write(" como estan")
with open("archivo.txt", "w") as archivo:
    for i in range(11):
        archivo.write(f'{i}\n')

with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea, end='')

#Abrir y filtrar archivos
import pathlib as pl

ruta = pl.Path(".")

for  archivo in ruta.iterdir():
    print(archivo)

for archivo in ruta.glob("*.py"):
    print(archivo)

archivo = ruta/"pila.py"

if archivo.exists():
    print(f"Encontrado y  mide {archivo.stat().st_size/1000} MB")
else:
    print("No existe")

#Organizar archivos en una carpeta
extensiones_unicas = set()
for archivo in ruta.iterdir():
    print(archivo.suffix)
    extensiones_unicas.add(archivo.suffix)

archivos = {extencion : [v.name for v in ruta.glob(f"*{extencion}")] for extencion in {archivo.suffix for archivo in ruta.iterdir()}}

archivos = {extencion : [v for v in ruta.glob(f"*{extencion}")] for extencion in {archivo.suffix for archivo in ruta.iterdir()}}

for extension, archivs in archivos.items():
    carpeta = ruta/extension[1:]
    carpeta.mkdir()
    for archivo in archivs:
        archivo.replace(carpeta/ archivo.name)
