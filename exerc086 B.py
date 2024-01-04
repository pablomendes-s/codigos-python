lista = [[0,0,0],[0,0,0],[0,0,0]]
n = 0
soma = 0
for l in range(0,3):
    for c in range (0,3):
        lista [l][c] = int(input(f"Digite o número na posição [{l},{c}]: "))
        soma += 1
print("=-="*30)
for l in range(0,3):
    for c in range (0,3):
        print(f"[{lista[l][c]:^5}]",end="")
    print()

