lista = {}
gols = []
lista ['jogador'] = str(input("Nome do Jogador: "))
lista ['partidas'] = int(input("Quantas partidas jogadas: "))
for c in range (0,lista['partidas']):
    gols.append(int(input(f'Quantidade de Gol na partida {c+1}: ')))
lista ['Total'] = sum(gols)
print("-="*30)
print(lista)
print("-="*30)
for k,i in lista.items():
    print(f'   -{k} tem o valor: {i}')
print("-="*30)
for k,v in enumerate (gols):
    print(f" O jogo {k+1} teve {v} gols")
print(f"Um total de {lista['Total']} gols")