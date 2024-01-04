def main():
    print("=-="*15)
    print("SIMULAÇÃO DE PREÇO")
    print("=-=" * 15)
    preco = float(input("Qual o valor do produto? "))
    forma = int(input("Qual a forma de pagamento?\n[1] À Vista Dinheiro ou Cheque:\n[2] À Vista no cartão:\n"
                      "[3] Parcelado até 2x:\n[4] Parcelado 3x ou mais:\n"))
    if forma == 1:
        print("O valor final será: {}".format(preco - (preco*(10/100))))
    elif forma == 2:
        print ("O valor final do produto será: {}".format(preco - (preco *(5/100))))
    elif forma == 3:
        print("O valor final é: {}".format(preco))
    elif forma == 4:
        print("O valor final do produto será: {}".format(preco + (preco * (20/100))))

main()