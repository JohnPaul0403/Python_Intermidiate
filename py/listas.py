#Funciones de las listas

array = []
print(array)

array = [1,2,3]
print(array)

#Formas de agregar y eleminar contenido a una lista con python
array.append(4)
array += [5,6]
array.extend([7,8,9])
array.insert(1, 2)
array.insert(32, 10)#En caso de pasarse de rango python lo posicionara como ultimo en la lista
array.insert(-10, 0)#En caso de ser menor que el rango python lo posicionara como a la inversa de la lista (Contando de arrevez).
array.pop()#Elimina el ultimo elemento de la lista y nos devuelve dicho numero
array.pop(2)#Elimina el elemento del indice
array.remove(9)#Elimina el valor dado
if 0 in array:#El comando in verifica si un valor esta en la lista devolviendo un valor booleano
    print(array.index(0))#Te devuelve el indice del valor dado de la lista
    array.remove(0)
    print(array)
array.index(3, 1) #Busca el valor desde la posicion dada
array.count(2) #Busca la cantidad de veces que se repite el valor
array.sort()#Ordena la lista (solo sirve siempre y cuando sean el mismo tipo de elemento)
len(array)#Nos dice la elementos en la lista
min(array)#Nos devuelve el minimo valor de la lista
max(array)#Nos devuelve el valor maximo de la lista
array.clear()#Limpia la lista
#help(list)# Nos imprime un manual en donde estan todas las funciones de las listas

#Ejercicio con listas

import os 

agregar = 1
insertar = 2
mostrar = 3
buscar = 4
eleminar = 5
ordenar = 6
limpiar = 7
salir = 0

frutas = []

def menu():
    os.system('cls')
    print(f'''      frutas
    {agregar}) Agregar
    {insertar}) Insertar
    {mostrar}) Mostrar
    {buscar}) Buscar
    {eleminar}) Eleminar
    {ordenar}) Ordenar
    {limpiar}) Limpiar
    {salir}) Salir''')

def agregar_registro():
    print("     Agregar")
    nombre = input("Nombre: ")
    frutas.append(nombre)

def insertar_registro():
    print("     Agregar")
    nombre = input("Nombre: ")
    pos = int(input("Posicion: "))
    frutas.insert(pos, nombre)

def mostrar_registro():
    if len(frutas) > 0 :
        for fruit in frutas:
            print(fruit)
    else:
        print("No hay registros")

def buscar_registro():
    print("     Buscar")
    nombre = input("Nombre: ")
    if nombre in frutas:
        cantidad = frutas.count(nombre)
        inicio = 0
        for i in range(cantidad):
            pos = frutas.index(nombre, inicio)
            print(f"{nombre} se encuentra en la poscion: {pos + 1}")
            inicio = pos + 1
    else:
        print("No existe el valor")

def eleminar_registro():
    print("     Elimina")
    nombre = input("Nombre: ")
    frutas.remove(nombre)

def ordenar_lista():
    frutas.sort()
    print(frutas)

def limpiar_lista():
    frutas.clear()

def main():
    continuar = True
    while continuar:
        menu()
        opc = int(input("Selcciona un opcion:"))
        if opc == agregar:
            agregar_registro()
        elif opc == insertar:
            insertar_registro()
        elif opc == mostrar:
            mostrar_registro()
        elif opc == buscar:
            buscar_registro
        elif opc == eleminar:
            eleminar_registro()
        elif opc == ordenar:
            ordenar_lista()
        elif opc == limpiar:
            limpiar_lista()
        elif opc == salir:
            continuar = False
        else:
            print("Pendejo")
        input()

#if __name__ == '__main__':
 #   main()

#Funciones de las listas
array = [0] * 10#Crea una lista con el valor dado multiplicado n veces
l1 = array#Copia la lista anterior/ Es otra forma de nombre la primera lista, se modifica en las dos listas aunque solo llamemos una
l1[9] = 10#Modifica el valor dado por el indice
l1 = array.copy()#Copia la lista
l1[8] = 9
l1[2:8:2]#Muestra desde el indice n hasta l-1, z para cuantas posiciones saltar
l3 = [i**2 for i in range(10)]#Con el for se puede crear lista de manera automatica, i inicialmente se lo puede modificar para que cambie su valor
import random as rd
l3 = [rd.randint(1,10) for i in range(20)]
#Listas de mas de una dimension 
matrix = [[1,2,3], [4,5,6], [7,8,9]]#Una lista de listas
matrix[0][:2]

#Ejemplos de matrices
n = 20
m1 = [[rd.randint(1,100) for i in range(n)]for j in range(n)]
m2 = [[rd.randint(1,100) for i in range(n)]for j in range(n)]
r = [[0]*n for i in range(n)]

for i in range(n):
    for s in range(n):
        r[i][s] = m1[i][s] + m2[i][s]

print(f'''{m1}
{m2}
{r}''')

r = [[m1[i][s] + m2[i][s] for s in range(n)] for i in range(n)]
print (r)

for i in range(n):
    print(f'{m1} + {m2} = {r}') if i == n//2 else print(f'{m1}   {m2}   {r}') 
