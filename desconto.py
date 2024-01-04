def main () :
    prod = float(input("Digite o preço do produto: "))
    desc = prod * 0.05
    desc2 = prod - desc
    print("O valor do produto na promoção é: {:.2f}".format(desc2))


main ()
