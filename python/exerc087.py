lista = [[0,0,0],[0,0,0],[0,0,0]]
spar = maivs = somat = 0
for l in range(0,3):
    for c in range (0,3):
        lista [l][c] = int(input(f"Digite o número na posição [{l},{c}]: "))
print("=-="*30)
for l in range(0,3):
    for c in range (0,3):
        print(f"[{lista[l][c]:^5}]",end="")
        if lista [l][c] % 2 == 0:
            spar += lista[l][c]
    print()
print("=-=" * 30)
print(f'A soma dos números pares são: {spar}')
for l in range (0,3):
    somat += lista[l][2]
print(f'A soma dos valore da 3º coluna é: {somat}')
print(f'O maior valor da segunda linha:{max(lista[1])}.')
