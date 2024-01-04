lista = {}
partidas = []
time = []
sig = " "
soma = resp = 0
while True:
    lista.clear()
    lista ['jogador'] = str(input("Nome do Jogador: "))
    lista ['quant'] = int(input("Quantas partidas jogadas: "))
    partidas.clear()
    for c in range (0,lista['quant']):
        partidas.append(int(input(f'    Quantidade de Gol na partida {c+1}: ')))
    lista ["gols"] = partidas [:]
    lista ["total"] = sum(partidas)
    sig = str(input("Deseja cadastrar novo jogador [S/N]? ")).strip().upper()[0]
    time.append(lista.copy())
    while sig not in "SN":
        print("Opção Inválida!", end="v")
        sig = str(input("Deseja cadastrar novo jogador [S/N]? ")).strip().upper()[0]
    if sig in "N":
        break
print("-"*60)
print(f"Nº ",end="")
for i in lista.keys():
    print(f'{i:<15}', end="")
print()
print("--"*30)
for c,v in enumerate (time):
    print(f'{c:<3}',end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-="*30)
while True:
    resp = int(input('Informe o número do jogador a ser consultado ou 999 para sair: '))
    if resp == 999:
        break
    if resp >= len(time):
        print(f"ERRO! Não existe jogador com o código {resp}.")
    else:
        print(f"Os dados do jogador {time[resp]['jogador']} são: ")
        for i , g in enumerate (time[resp]["gols"]):
            print(f"   {time[resp]['jogador']}No {i+1}º jogo fez {g} Gols.")
print("-=-"*30)
print('Volte Sempre!')