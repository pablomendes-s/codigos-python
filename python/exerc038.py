def main():
    n1 = int(input("PRIMEIRO Número: "))
    n2 = int(input("SEGUNDO Número: "))
    if n1 > n2:
        print("{} é maior que {}".format(n1,n2))
    elif n1 < n2:
        print("{} é maior que {}".format(n2,n1))
    elif n1 == n2:
        print ("Os números são iguais:")




main()