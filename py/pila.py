def validar_expresion(expression):
    pila = []
    for simbol in expression:
        if simbol == "(":
            pila.append("(")
        elif simbol == ")":
            if len(pila) > 0:
                pila.pop()
            else:
                return False

    return len(pila) == 0

def main():
    e = input("Expresion: ")

    if validar_expresion(e):
        print("Esta correcta")
    else:
        print("incorrecto")

main()
