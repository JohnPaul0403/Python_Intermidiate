#Agenda con la posibilidad de agregar, mostrar, buscar, modificar y eliminar contactos
import os

def mostar_menu():
    print('''Bienvenido a tu agenda virtual
1. Agregar contacto
2. Mostrar contactos
3. Buscar contacto
4. Modificar contacto
5. Eliminar contacto
0. Salir

''')

def agregar_contacto(agenda, nombres):
    nombre = input("Escribe su nombre: ")
    numero = input("Escribe su numero telefonico: ")
    correo = input("Escribe su correo electronico: ")
    if not nombre in agenda:
        agenda.setdefault(nombre, [numero, correo])
        nombres.append(nombre)
    else:
        nombres.append(nombre)
        agenda.setdefault(nombre + str(nombres.count(nombre)), [numero, correo])
    
    print(f"{nombre}, agregado a la agenda")

def mostrar_contactos(agenda):
    for key in agenda:
        print(f''' Nombre: {key}
Numero: {agenda[key][0]} 
Correo electronico: {agenda[key][1]}''')

def buscar_contacto(agenda):
    nombre = input("Dime el nombre del contacto: ")
    if nombre in agenda:
        print(f'''  Nombre: {nombre}
        numero: {agenda.get(nombre)[0]}
        Correo electronico: {agenda.get(nombre)[1]}''')
    else:
        print("No existe el contacto")

def modificar_contacto(agenda):
    nombre = input("Dime el nombre del contacto a modificar: ")
    os.system("clear")
    if nombre in agenda:
        valor = int(input('''Dime que quieres modificar
1. Numero
2. Correo electronico
3. Ambos
0. Salir
'''))
        os.system("clear")
        if valor == 1:
            numero = int(input("Dime el nuevo numero: "))
            for key in agenda:
                if key == nombre:
                    c = agenda[key][1]
            agenda[nombre] = [numero, c]
        elif valor == 2:
            correo = int(input("Dime el nuevo correo electronico: "))
            for key in agenda:
                if key == nombre:
                    n = agenda[key][0]
            agenda[nombre] = [n, correo]
        elif valor == 3:
            numero = int(input("Escribe su nuevo numero telefonico: "))
            correo = input("Escribe su nuevo correo electronico: ")
        elif valor == 0:
            print(" ")
        else:
            print("Valor incorrecto")
    else:
        print("El contacto no existe")

def eliminar_contacto(agenda):
    nombre = input("Dime el nombre del contacto a eliminar: ")
    agenda.pop(nombre, "El contacto no existe")

def main():
    agenda = {}
    nombres = []

    while True:
        mostar_menu()
        valor = int(input("Elige una opcion: "))
        input("Presiona enter para continuar")
        os.system("clear")
        if valor == 1:
            agregar_contacto(agenda, nombres)
        elif valor == 2:
            mostrar_contactos(agenda)
        elif valor == 3:
            buscar_contacto(agenda)
        elif valor == 4:
            modificar_contacto(agenda)
        elif valor == 5:
            eliminar_contacto(agenda)
        elif valor == 0:
            print("Nos vemos..")
            break
        else:
            print("Valor incorrecto")

        input("Presiona enter para continuar...")
        os.system("clear")

if __name__ == "__main__":
    main()
