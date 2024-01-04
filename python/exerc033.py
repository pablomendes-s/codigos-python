def main():
    from time import sleep
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro e ultimo número: "))
    print("Processando...")
    sleep(1)
    #Calculando o menor numero
    menor = n1
    if n2 < n1 and n2 < n3:
        menor = n2
    if n3 < n2 and n3 < n1:
        menor = n3
    print("O menor número é:{}".format(menor))
    #Calculando o Maior número
    maior = n1
    if n2 > n1 and n2 > n3:
        maior = n2
    if n3 > n2 and n3 > n1:
        maior = n3
    print ("O maior número é o {}!".format(maior))

main()