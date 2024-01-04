def main():
    soma = 0
    quant = 0
    for cont in range (1,7):
        n = int(input("Digite o {}º número:".format(cont)))
        if n % 2 == 0:
            soma = soma + n
            quant = quant + 1
    print("A soma dos {} números pares é: {}".format(quant,soma))
main()