def main ():
    from datetime import date
    ano = int(input("Qual seu ano de nascimento?"))
    atual = date.today().year
    idade = atual - ano
    if idade <= 9:
        print("Com {} anos, você está na categoria MIRIM".format(idade))
    elif idade <=14:
        print("Com {} anos, você estará na categoria INFANTIL".format(idade))
    elif idade <=19:
        print("Com {} anos, você estará na categoria JÚNIOR".format(idade))
    elif idade <=25:
        print ("Com {} anos, você estará na categoria SENIOR".format(idade))
    elif idade > 25:
        print("Com {} anos, você estará na categoria MASTER".format(idade))

main()