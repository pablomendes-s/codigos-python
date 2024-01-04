def main():
    nota1 = float(input("QUal sua primeira nota? "))
    nota2 = float(input("Qual sua segunda nota?"))
    cal = (nota1 + nota2) / 2
    if cal >= 7:
        print("Sua nota foi {}, você foi \33[00;32m APROVADO\33[m!".format(cal))
    elif cal < 5:
        print("Sua nota foi {}, você foi \33[00;31m REPROVADO\33[m".format(cal))
    else:
        print ("Sua nota foi {}, Você esta de \33[00;33m RECUPERAÇÃO\33[m".format(cal))


main()