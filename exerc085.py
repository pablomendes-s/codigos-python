lista = [[],[]]
valor = 0
for v in range (0,7):
    valor = (int(input(f"Digite o {v+1}º valor: ")))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f"Os números pares são: {lista[0]}")
print(f"Os número Impares são: {lista[1]}")




