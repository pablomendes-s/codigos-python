def main():
    from datetime import date
    print("=-=" * 20)
    print("\33[01;33m Descubra se você deve se ALISTAR\33[m")
    print("=-=" * 20)
    nasc = int(input("Digite o ano do seu nascimento: "))
    atual = date.today().year
    cal = atual - nasc
    if cal == 18:
        print("Você deve se alistar IMEDIATAMENTE")
    elif cal > 18:
        print('Você ja DEVERIA ter se ALISTADO à {} anos'.format(cal - 18))
    elif cal < 18:
        print("FALTA {} anos para você se ALISTAR!".format(cal - 18))


main()
