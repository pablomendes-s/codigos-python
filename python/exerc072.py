numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
pos = 0
resp = ' '
while True:
    pos = int(input("Digite um número de 0 a 20: "))
    print(f'Você digitou o número: {numeros[pos]}')
    resp = str(input('Quer tentar novamente[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('='*20)
print('FIM')