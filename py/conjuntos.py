#Funciones de los conjuntos
conjunto = set()
conjunto = {1,2,3}
conjunto.add(5)#Agrega elementos al conjunto
conjunto.pop()#Elimina un elemento aleatorio
conjunto.remove(3) if 3 in conjunto else 3#Elimina el valor 
conjunto.discard(5)#Elimina eveitando errores
conjunto.add(7) if not 7 in conjunto else 7
len(conjunto)
a = {1,2,3,10}
b = {4,5,6,10}
a & b#Nos muestra los elmentos que tienen en comun
a | b #Muestra la union de los elementos sin repetidos
a - b #Muestra los elementos de a que no estan en b
b - a #Muestra los elementos de b que no estan en a
a ^ b# Union de las diferencias de los conjuntos
a > b #Evalua si un conjunto tiene todos los elementos de otro
a.isdisjoint(b)#Evalua si un conjunto no comparte elementos con otro

paises = ["brasil", "peru", "chile", "ecuador", "bolivia", "argentina", "venezuela", "cuba", "mexico", "honduras"]
conjunto = set()
for word in paises:
    for letter in word:
        conjunto.add(letter)

print(len(conjunto))
print(conjunto)
