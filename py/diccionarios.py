#Funciones de los diccionarios
d = {}
d = dict()
d = {
    1 : "uno",
    2 : "dos"
}
d[3] = "tres"
d.setdefault(5, [1,2,3,4,5])
d[5] = "cinco"
d[5]#En caso de no existir la llave devuelve error
d.get(55, "No existe")#Devuelve el valor sin posibildad de errores
d.pop(5, "No existe")#Elimina por la key, en caso de existir se le puede poner un texto por default
d.popitem()#Elimina por el metodo de pila LIFO
d.keys()#Devuelve las keys del diccionario
d.values()#Deveulve los valores del diccionario
d.items()
len(d)
3 in d

for key in d:
    print(f"{key}: {d[key]}")

for key, value in d.items():
    print(f"{key}: {value}")

d.clear()
