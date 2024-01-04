l = []
menor = maior = 0
for n in range(0,5):
    l.append(int(input(f"Digite o {n+1}º número: ")))
    if n == 0:
        menor = maior = l[n]
    else:
        if l[n] > maior:
            maior = l[n]
        if l[n] < menor:
            menor = l[n]
print(f'A lista é: {l}')
print(f'O maior número é: {maior} na posição ', end="")
for i, v in enumerate(l):
    if v == maior:
        print(f"{i+1}...")
print(f"O menor número é: {menor} na posição ", end = "")
for i, v in enumerate(l):
    if v == menor:
        print(f"{i+1}...")