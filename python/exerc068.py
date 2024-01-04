from random import randint
cont = 0
print('===JOGUE PAR OU IMPAR===')
print('=-='*10)
while True:
    jogador = int(input("Escolha um número de 1 a 10: "))
    sorteio = randint(0, 10)
    resultado = jogador + sorteio
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("PAR ou IMPAR [P/I]? ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {sorteio}, total de {resultado}:", end =' ')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if resultado % 2 == 0:
            print('Você venceu!!!')
            cont += 1
        else:
            print('GAME OVER')
            break
    elif tipo == 'I':
        if resultado % 2 != 0:
            print('Você Venceu!!!')
            cont += 1
        else:
            print('Game Over')
            break
    print('Tente novamente...')
    print('=-='*10)
print(f'Você teve {cont} vitórias')