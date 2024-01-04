def main ():
    primeiro = int(input("Digite o primeiro termo: "))
    frequencia = int(input("Qual a razão? "))
    final = primeiro + (10-1) * frequencia
    for n in range (primeiro,final + frequencia,frequencia):
        print("{}".format(n),end="░")
    print("ACABOU!")
    else:
        print ("Informação Incorreta")

main()