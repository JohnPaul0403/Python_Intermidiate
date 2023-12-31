import os
import queue as qe

def mostrar_menu():
    print('''Seleciona una opcion
1. Agendar
2. Atender
3. Mostrar agenda
4. Salir
''')

def crear_evento(evento, agenda, lista_eventos):
    agenda.put(evento)
    lista_eventos.append(evento)
    if len(lista_eventos) > 1:
        lista_eventos.sort()
    print("Evento agendado")

def atender_evento(agenda, lista_eventos):
    agenda.get()
    print(f"Evento {lista_eventos[0][0]} atendido")
    lista_eventos.pop(0)

def mostrar_agenda(lista_eventos):
    for event in lista_eventos:
        for i in event:
            print(i)

def main():
    print("Bienvenido a tu agenda virtual")
    input("Presiona enter para continuar...")

    agenda = qe.PriorityQueue()
    lista_eventos = []

    os.system("clear")

    while True:
        mostrar_menu()
        valor = int(input())
        os.system("clear")

        if valor == 1:
            evento = input("Escribe tu evento ")
            fecha = input("Escribe cuantos dias falta para el evento ")
            crear_evento([evento, fecha], agenda, lista_eventos)
        elif valor == 2:
            if not agenda.empty():
                atender_evento(agenda, lista_eventos)
            else:
                print("No tiene eventos a atender")
        elif valor == 3:
            if len(lista_eventos) != 0:
                mostrar_agenda(lista_eventos)
            else:
                print("No tiene eventos registrados")
        elif valor == 4:
            print("Nos vemos....")
            break
        else:
            print("Valor incorrecto")

        input("Presiona enter para continuar...")
        os.system("Clear")

if __name__ == "__main__":
    main()
