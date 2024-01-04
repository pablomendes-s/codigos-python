from random import randint
from time import sleep
tentativas = 1
sorteio = randint(1,10)
numero = int(input("Em que número estou pensando: "))
print("PENSANDO...")
sleep(2)
while numero != sorteio:
    if numero > sorteio:
        tentativas += 1
        numero = int(input("Menos...Tente novamente:"))
    elif numero < sorteio:
        numero = int(input("Mais...Tente novamente:"))
        tentativas += 1
print("você acertou na {} tentativa".format(tentativas))




