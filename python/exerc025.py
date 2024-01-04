def main ():
    nome = str(input("Digite seu nome complete: ")).strip()
    print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))

main()