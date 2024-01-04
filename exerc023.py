def main():
    numero = int(input("Digite um número inteiro: "))
    n = str(numero)
    print ("Analisando o número {}".format(numero))
    print ("Unidade: {}".format(n[3]))
    print ("Dezena: {}".format(n[2]))
    print ("Centena: {}".format(n[1]))
    print ("Milhar: {}".format(n[0]))

main()