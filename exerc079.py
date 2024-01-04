val = []
sig = ''
while True:
    n = int(input("Digite um número para cadastro: "))
    if n not in val:
        val.append(n)
        sig = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    else:
        print("número ja cadastrado, tente novamente!")
    while sig not in "SN":
        print("opção inválida...", end='')
        sig = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    if sig in "N":
        break
val.sort()
print(val)