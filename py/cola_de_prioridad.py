#funcionamento de las colas
import queue as qe

cola = qe.Queue()#Crea una cola
cola.put([1,2,3])#Pone los datos en la cola
cola.put(4)
cola.get()#Muestra el elemnto que esta primero en la fila y lo elimina
cola.empty()#Nos avisa si la cola esta vacia con un valor booleano

cola.put(4) if cola.empty() else cola.get()

#Colas de prioridad
import random as rd

paises = ["brasil", "peru", "chile", "ecuador", "bolivia", "argentina", "venezuela", "cuba", "mexico", "honduras"]
cp = qe.PriorityQueue()#Esta cola organiza los valores de menor a mayor
for i in range(10):
    cp.put([rd.randint(1,10), paises[rd.randint(0, len(paises) -1)]]) 

for i in range(10):
    cp.get()
