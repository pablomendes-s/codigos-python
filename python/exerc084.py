temp = []
princ = []
maior = menor = 0
sig = ' '
while True:
    temp.append(str(input("Digite um Nome: ")))
    temp.append(float(input("Qual o peso da pessoa: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    sig = str(input("Deseja continuar  [S/N]?")).strip().upper()[0]
    while sig not in "SN":
        sig = str(input("Deseja continuar  [S/N]?")).strip().upper()[0]
    if sig == "N":
        break
print("=-="*20)
print(f"Foram cadastradas {len(princ)} pessoas")
print(f"O maior peso foi de: {maior}Kg pertencente á ", end='')
for p in princ:
    if p[1] == maior:
        print(f' [{p[0]}] ', end= "")
print()
print(f"O menor peso foi de: {menor}Kg pertencente á ",end="")
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
print()