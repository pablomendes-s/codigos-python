def main():
    from random import randint
    from time import sleep
    print("{:=^40}".format(" MANOLO GAME "))
    print("{:=^40}".format(" JO KEN PO "))
    lista = ("PEDRA", "PAPEL", "TESOURA")
    sorteio = randint(0,2)
    op = int(input('''Escolha uma das opções abaixo:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Resposta:'''))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print('PO !!!')
    sleep(1)
    print('=-='*20)
    print("Você escolheu {} e o computador {}".format(lista [op], lista[sorteio]))
    if op == sorteio:
        print("\33[00;33mEMPATE")
    elif op == 1 and sorteio == 2:
        print("\33[00;35mVitória do COMPUTADOR!")
    elif op == 2 and sorteio == 0:
        print("\33[00;35mVitória do COMPUTADOR")
    elif op == 0 and sorteio == 1:
        print("\33[00;35mVitória do COMPUTADOR!")
    else:
        print("\33[00;32mVitória do JOGADOR!!\33[m")
    print('=-=' * 20)



main()
