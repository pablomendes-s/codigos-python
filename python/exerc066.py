n = s = 0
c = 0
while True:
    n = int(input("Digite um número OU [999 para SAIR]:"))
    if n == 999:
        break
    c += 1
    s += n
print(f"Foram digitados {c} números, e sua soma é {s}")
