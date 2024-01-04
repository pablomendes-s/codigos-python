def main():
    n = int(input("Digite um número e descubra sua tabuada: "))
    for mult in range (0,11):
        print("{} x {} = {}".format(n, mult, (n*mult)))



main()