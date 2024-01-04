from time import sleep
from random import randint
from operator import itemgetter
dados = {'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3':randint(1,6),
         'Jogador4': randint(1,6)}
ranking = {}
print("### VALORES SORTEADOS ###")
for k,v in dados.items():
    print(f"O {k} tirou {v} no Dado")
    sleep(0.5 )
print("="*30)
print("   == RANKING DOS JOGADORES ==")
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate (ranking):
    print(f"Em {i+1}º Lugar: {v[0]} com {v[1]}.")
    sleep(0.5)