def main():
    frase = str(input("Digite uma frase e descubra se é um palindromo:")).strip().upper()
    palavra = frase.split()
    junto = "".join(palavra)
    inverso = junto[::-1]
    print("{}".format(inverso))
    if inverso == junto:
        print("A frae digitada é um PALINDROMO")
    else:
        print ("Afrase não é um PALINDROMO")






main()