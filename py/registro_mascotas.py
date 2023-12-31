import os

#Tener la posibilidad de agregar, ver, y eleminar mascotas de la lista

def mostrar_menu():
    print('''Elege una opcion

1. Agregar mascota
2. Ver mascotas
3. Eleminar mascotas
4. Salir
''')

def agregar_mascota(lista):
    nombre = input("Dime su nombre: ")
    edad = input("Dime su edad: ")
    peso = input("Dime su peso: ")
    tipo = input("Dime el tipo de animal: ")
    mascota = (nombre, edad, peso, tipo)
    lista.append(mascota)

def ver_mascotas(lista):
    i = 1
    for mascota in lista:
        x,y,z,a = mascota
        print(f''' Mascota {i}
Nombre: {x}
Edad: {y}
Peso: {z}
Tipo: {a}
''')
        i += 1

def eliminar_mascota(lista):
    i = 1
    for mascota in lista:
        x,y,z,a = mascota
        print(f''' Mascota {i}
Nombre: {x}
Edad: {y}
Peso: {z}
Tipo: {a}
''')
        print("*^*"*20)
        i += 1
    
    valor = int(input("Elegi el numero de mascota que queieras eleminar: ")) - 1
    lista.pop(valor)

def main():
    print("Bienvenido, esta es un cuaderno digital para guerdar tus mascotas")
    input("Presiona enter para continuar...")
    os.system("clear")

    lista = []

    while True:
        mostrar_menu()
        valor = int(input())

        os.system("clear")

        if valor == 1:
            agregar_mascota(lista)
        elif valor == 2:
            ver_mascotas(lista) if len(lista) > 0 else print("No tienes animales registrados")
        elif valor == 3:
            eliminar_mascota(lista) if len(lista) > 0 else print("No tienes animales registrados")
        elif valor == 4:
            print("Nos vemos")
            break
        else:
            print("Valor incorrecto")

        input("Presiona enter para continuar...")
        os.system("clear")

if __name__ == "__main__":
    main()
