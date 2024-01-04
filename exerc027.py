def main():
    nome = str(input("Digite seu nome completo: "))
    n = nome.split()
    print("Muito prazer em te conhecer!!!")
    print("Seu primeiro nome é:{} ".format(n[0]))
    print("Seu último nome é: {}".format(n[-1]))

main()