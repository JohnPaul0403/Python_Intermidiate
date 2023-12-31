#Crear una Agenda la sea capaz de agregar, mostrar y buscar contactos los cuales esten guardados en un archivo txt
import os
import pathlib as pl

def mostrar_menu():
    print('''1. Agregar contacto
2. Mostrar contactos
3. Buscar contactos
0. Salir''')

def agregar_contacto(agenda, nombres, carpeta):
    nombre = input("Escribe el nombre del contacto: ")
    tel = input("Escribe su numero telefonico: ")
    correo = input("Escribe su correo electronico: ")

    if not nombre in agenda:
        agenda.setdefault(nombre, [tel, correo])
        nombres.append(nombre)
    else:
        nombres.append(nombre)
        agenda.setdefault(f"{nombre + nombres.count(nombre)}", [tel, correo])

    archivo = f"./{carpeta}/{nombre + nombres.count(nombre) if nombres.count(nombre) > 1 else nombre}.txt"

    with open(archivo, "w") as archive:
        archive.write(f"{tel}\n {correo}")

def mostrar_contactos(agenda, carpeta):
    ruta = pl.Path(f"./{carpeta}")
    for archivo in ruta.iterdir():
        with open(archivo, "r") as archivo:
            dta = []
            for linea in archivo:
                dta.append(linea)
            agenda[archivo.name] = dta

    for key in agenda:
        print(f'''Nombre: {key}
Tel. : {agenda[key][0]}
Correo: {agenda[key][1]}
''')

def buscar_contactos(carpeta):
    nombre = input("Dime su nombre") + ".txt"
    ruta = pl.Path(f"./{carpeta}")
    archivo = ruta/nombre

    if archivo.exists():
        dta = []
        with open(f"./{ruta}/{nombre}") as archivo:
            for linea in archivo:
                dta.append(linea)
            print(f'''Nombre: {nombre}
Tel. : {dta[0]}
Correo: {dta[1]}''')
    else:
        print("No existe el contacto")

def main():
    print("Binevenido a tu agenda de contactos")
    input("Presiona enter para continuar...")
    os.system("clear")
    ruta = pl.Path("./py")
    carpeta = 0
    agenda = {}
    nombres = []
    for archivo in ruta.iterdir():
        if archivo.name == "agenda":
            carpeta += 1
            print("encontrado")
    if carpeta == 0:
        carpeta = ruta/"agenda"
        carpeta.mkdir()
    else:
        carpeta = ruta/"agenda"
    
    while True:
        mostrar_menu()
        valor = int(input("Elige una opcion: "))
        os.system("clear")
        if valor == 1:
            agregar_contacto(agenda, nombres, carpeta)
        elif valor == 2:
            mostrar_contactos(agenda, carpeta)
        elif valor == 3:
            buscar_contactos(carpeta)
        elif valor == 0:
            print("Nos vemos..")
            break
        else:
            print("Opcion invalida")

        input("Presiona enter para continuar...")
        os.system("clear")

if __name__ == "__main__":
    main()
