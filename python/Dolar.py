def main():
    reais = float(input("Digite a quantidade de reais na carteira: "))
    cot = reais / 5.78
    print ("Com essa quatidade de Reais, é possivel comprar:  {:.2f} Dolares".format(cot))

main()