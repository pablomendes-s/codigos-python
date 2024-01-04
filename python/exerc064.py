n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Digite um número ou [999 para PARAR]"))
    soma += n
    cont += 1
print("Você digitou {} números e a soma entre eles é:{}".format(cont -1, soma -999))
print("Fim")