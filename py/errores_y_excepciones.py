#Programa que maneje errores y excepciones
import os

def mostrar_menu():
    print('''       Personajes
1. Mago
2. Guerrero
3. Tu madre
0. Salir
''')

def main():
    try :
        with open("archivo.txt", "r") as archive:
            pass
    except:
        with open("archivo.txt", "w") as archive:
            pass
    print("olo")
    input("Enter para continuar")
    os.system("clear")

    while True:
        mostrar_menu()
        valor = input("Elige una opcion: ")
        try:
            valor = int(valor)
        except ValueError as error:
            valor = -1
            print(error)

        os.system("clear")

        if valor == 1:
            print("Esta magamente mamado")
        elif valor == 2:
            print("Es un guerreo educado")
        elif valor == 3:
            print("Tu madre es la mejor")
        elif valor == 0:
            print("nos vemos..")
            break
        else:
            print("opcion no valida")

        input("Enter para continuar")
        os.system("clear")

if __name__ == "__main__":
    main()
