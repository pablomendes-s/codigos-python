lista = [[],[],[]]
n = 0
for c in range(0,9):
    n = (int(input(f"Digite um número: ")))
    if c <= 3:
        lista[0].append(n)
    elif c > 3 and c <= 6:
        lista[1].append(n)
    elif c > 6:
        lista[2].append(n)
print("=-="*30)
print(f"{lista[0]}")
print(f'{lista[1]}')
print(f'{lista[2]}')



