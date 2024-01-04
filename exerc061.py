print("Gerador de Progreção Aritimetica")
print("=+"*10)
primeiro = int(input("Digite o primeiro termo: "))
frequencia = int(input("Qual a razão? "))
final = primeiro
cont = 1
while cont <= 10:
    print("{} →".format(final), end='')
    final = final + frequencia
    cont += 1

print("FIM")
