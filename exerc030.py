def main():
    n = int(input("Digite um número e descubre se ele é PAR ou IMPAR:"))
    resultado = n % 2

    if resultado == 1:
        print("O número {} é IMPAR!!!".format(n))
    else:
        print("O número {} é PAR!!!".format(n))



main()