c = (   '\033[m',          # 0 - Padrão
        '\033[0;30;41m',   # 1 - Vermelho
        '\033[0;30;42m',   # 2 - Verde
        '\033[0;30;43m',   # 3 - Amarelo
        '\033[0;30;44m',   # 4 - Azul
        '\033[0;30;45m',   # 5 - Roxo
        '\033[0;30;47m'       # 6 - Branco
)


def ajuda(com):
    titulo (f'Acessando o manual de: \' {com}\'', 4)
    print(c[6], end="")
    help(com)
    print(c[0], end="")


def titulo(msg,cor=0):
    tam = len(msg)
    print (c[cor],end="")
    print(f'{"~" * (tam + 4)}')
    print(f"  {msg}")
    print(f'{"~" * (tam + 4)}')
    print(c[0],end="")

comando = ' '
while True:
    titulo("SISTEMA DE AJUDA",2)
    comando = str(input("Comando ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda (comando)
titulo("VOLTE SEMPRE!",3)


