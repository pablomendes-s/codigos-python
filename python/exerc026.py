def main():
    nome = str(input("Digite uma frase: ")).strip()
    print("Na sua frase a letra A aparece {} vezes!".format(nome.upper().count("A")))
    print("A primeira letra A aparece da posição: {}".format(nome.upper().find("A")+1))
    print("A última letra A aparece da posição: {}".format(nome.upper().rfind("A")))

main()