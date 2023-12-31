str = "Hola mundo!"
str[3:7]

#Funciones especificas de las cadenas
str.count('l')#Cuenta la cantidad de veces que se repite el numero
str.find("!")#Encuentra la letra, en caso de existir regresa un valor negativo
str.index("a", 2)#Busca el indice de la letra, pero en caso de existir regresa un error
str.index("x") if "x" in str else print("No existe")#Para evitar un error
", ".join(["Nombre", "Apellido", "Ciudad"])#Une objetos iterables en una cadena con la letra dada
", ".join("Hey")
str.lower()#Pone en minusculas la palabra
str.upper()#Pone en mayusculas la palabra
str.replace("o", "e", 1)#Reemplaza un valor por el nuevo dado en la cadena y la cantidad de veces que quieras que lo haga
str = str[:9] + "O" + str[10:]
str.split(" ")#Separa la cadena por la letra dada y devuelve una lista
