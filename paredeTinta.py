def main ():
    altura = float(input("Digite a altura da parede:" ))
    largura = float(input("Digite a largura da parede: "))
    area = altura * largura
    tinta = 2
    quant = area / tinta
    print ("Será necessário **{}L** de tinta para pintar toda a parede".format(quant))



main()