from datetime import datetime
lista = {}
lista ["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
lista ['idade'] = datetime.now().year - nasc
lista ['Ctps'] = int(input("Nº Carteira de Trabalho [0 não tem]: "))
if lista ['Ctps'] != 0:
    lista ['contratação'] = int(input("Ano de Contratação: "))
    lista ['Salário'] = float(input("Salário: " ))
    lista ['Aposentadoria'] = lista ['idade'] + 35
print("=-="*20)
for k,i in lista.items():
    print(f"   -{k} tem o valor de {i}")