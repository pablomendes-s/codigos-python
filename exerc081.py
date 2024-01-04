list = []
conf = 0
while True:
    n = int(input("Digite um número: "))
    sig = str(input("Deseja continuar [S/N]?")).strip().upper()[0]
    list.append(n)
    if n == 5:
        conf += 1
    while sig not in "SN":
        sig = str(input("Deseja continuar [S/N]?")).strip().upper()[0]
    if sig in "N":
        break
list.sort(reverse=True)
print(list)
print(f'O número Cinco apareceu {conf} vezes na seguinte lista:')
print (f'Foram digitados {len(list)} númros')

