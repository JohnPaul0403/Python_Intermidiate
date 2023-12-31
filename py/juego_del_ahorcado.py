import random as rd
import os

paises = ["brasil", "peru", "chile", "ecuador", "bolivia", "argentina", "venezuela", "cuba", "mexico", "honduras"]

def crear_palabra():

    str = paises[rd.randint(0, len(paises) - 1)]
    array = ["_" for i in range(len(str))]
    return str, array

def busca_valor(valor, str, array):
    lista = []
    for letter in valor:
        lista.append(letter)
    for letter in lista:
        q = str.count(letter)
        n = 0
        for i in range(q):
            pos = str.index(letter, n)
            array[pos] = letter
            n = pos + 1

def main():
    str, array = crear_palabra()
    vidas = 5

    print("Juego del ahorcado, con nombres de paises latinos")

    print(f"Palabra: {''.join(array)}")

    input("Presiona enter para continuar...")

    os.system("clear")


    while vidas != 0:

        valor = input("Elegi una letra: ").lower()

        if valor in str and len(valor) >= 1:
            busca_valor(valor, str, array)
            print("Bien hecho")
        else:
            vidas -= 1
            print(f"Valor incorrecto, vidas: {vidas}") if vidas > 0 else print(f"Perdiste, el pais era {str.upper()}")

        input("""
Presiona enter para continuar...""")

        os.system("clear")

        print(f'Palabra: {"".join(array).upper()}') if vidas != 0 else print("")

        if "".join(array) == str:
            print(f"Ganaste! el pais es {str.upper()}")
            break

main()
