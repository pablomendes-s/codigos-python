from random import randint
from time import sleep
lista = []
total = 0
sorte = []
print("="*35)
print("==GERADOR DE JOGOS DA MEGA SENA==")
print("="*35)
quant = int(input("Quantos jogos deseja fazer? "))
while total <= quant:
    cont = 0
    total += 1
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sorte.append(lista[:])
    lista.clear()
print("Sorteando...")
for i , l in enumerate (sorte):
    sleep(1)
    print(f"Jogo {+1}: {l}")
print("\33[33mBoa Sorte!")



