def fatorial (num, show = False):
    '''

    :param num: número que deseja calcular o fatorial
    :param show: Opção para mostrar a equação completa até o resultado
    :return: mostra para o usuário o resultado do fatorial do número digitado
    '''
    f = 1
    for c in range(num , 0, -1):
        f *= c
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ",end="")
    return f'{f}'


print(fatorial(5,show=False))
help(fatorial)