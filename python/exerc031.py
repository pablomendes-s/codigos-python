def main():
    distancia = int(input("Qual a distancia percorrida? "))
    c1 = 0.50
    c2 = 0.45
    if distancia <= 200:
        print("Você gastará R${} para percorrer {}km".format(distancia * c1, distancia))
    else:
        print("Você gastará R${} para percorrer {}km".format(distancia * c2, distancia))
main()
