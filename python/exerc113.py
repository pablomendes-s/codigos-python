def leiaInt(numero):
    while True:
        try:
            num = int(input(numero))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número INTEIRO válido\033[m')
            continue
        else:
            return num


def leiaFlo(numero):
    while True:
        try:
            num = float(input(numero))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número INTEIRO válido\033[m')
            continue
        else:
            return num


ni = leiaInt("Digite um número INTEIRO: ")
nr = leiaFlo("Digite um número REAL: ")
print(f"Você digitou o número INTEIRO {ni} e o número REAL: {nr}")
