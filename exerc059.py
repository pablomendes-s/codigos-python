n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
soma = n1 + n2
mult = n1 * n2
nv = 4
sair = 5
acao = 0
while acao != 5:
    print('''    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    acao = int(input("===>Escolha uma opção: "))
    if acao == 1:
        acao = n1 + n2
        print("\33[35mA soma de {} com {} é: {}\33[m".format(n1,n2,acao))
    elif acao == 2:
        mult = n1 * n2
        print("\33[35mA Multiplicação entre {} X {} = {}\33[m".format(n1, n2, mult))
    elif acao == 3:
        if n1 > n2:
            maior = n1
            print("\33[35mO maior número é {}\33[m".format(maior))
        else:
            maior = n2
            print("\33[35mO maior número é: {}\33[m".format(maior))
    elif acao == 4:
        print("##Digite novamente##....")
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
    elif acao == 5:
        print("Fim")
    else:
        print("Opção inválida")
    print("=-="*10)



