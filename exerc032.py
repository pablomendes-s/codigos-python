def main():
    from datetime import date
    ano = int(input("Digite um ano e descubra ele é Bisexto: "))
    c = ano % 4
    if ano == 0:
        ano = date.today().year
    if c == 0 and ano % 100 != 0:
        print("O ano {} é Bissexto!!".format(ano))
    else:
        print("O ano {} NÃo é Bissexto!!".format(ano))




main()