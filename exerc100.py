from random import randint
from time import sleep
numeros = []
def sorteia(lista):
    print("Sorteando 5 valores da lista:",end="")
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        sleep(0.3)
        print(f" {n}", end="", flush=True)

def somaPar(lista):
    print("A soma dos valores Par é: ",end="")
    soma = 0
    for v in lista:
        if v %2 == 0:
            soma += v
    print(f"{soma}", end="")


sorteia(numeros)
print()
somaPar(numeros)
