def leiaInt(numero):
    while True:
        num = input(numero)
        if num.isnumeric():
            return num
        print('\033[31mERRO! Digite um número inteiro válido\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')