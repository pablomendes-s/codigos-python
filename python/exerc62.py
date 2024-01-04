print("Gerador de Progreção Aritimetica")
print("=+"*10)
primeiro = int(input("Digite o primeiro termo: "))
frequencia = int(input("Qual a razão? "))
final = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} →".format(final), end='')
        final = final + frequencia
        cont += 1
    print("PAUSE")
    mais = int(input("Quantos termos quer mostrar a mais? "))
print("FIM")