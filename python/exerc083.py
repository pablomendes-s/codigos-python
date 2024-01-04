expre = str(input("Digite uma exressõa:"))
lista = []
for simb in expre:
    if simb == "(":
        lista.append("(")
    elif simb == ")":
        if len(lista) >= 1:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("A expressõa esta correta!")
else:
    print("A expressão esta errada!")

