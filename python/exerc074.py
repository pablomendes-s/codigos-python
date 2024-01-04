from random import randint
from time import sleep

sorteio = (randint(1,60)),(randint(1,60)),(randint(1,60)),(randint(1,60)),(randint(1,60)),
print('====Sorteio de números para LOTERIA====')
clik = str(input('Aperte ENTER para iniciar:'))
print('========================================')
print("Sorteando...")
sleep(1)
print(f'Os 5 número sorteados foram:{sorteio}')
print(f'O maior valor sorteado foi: {max(sorteio)}')
print(f'O menor valor sorteado foi: {min(sorteio)}')

