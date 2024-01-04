from datetime import date
def voto(nasc):
    '''

    :param nasc: Captura o ano de nascimento
    :return: mostra se a pessoa está apta a votar
    '''
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return (f"Com {idade} anos o voto é PROIBIDO!")
    elif 16 >= idade < 18 or idade >= 65:
        return (f"Com {idade} anos o voto é FACULTATIVO!")
    else:
        return (f"Com {idade} anos o voto é OBRIGATÓRIO!")


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))