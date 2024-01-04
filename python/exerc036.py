def main():
    casa = float(input("Qual o valor da casa que pretende comprar? "))
    salario = float(input("Qual o valor da sua RENDA MENSAL? "))
    anos = int(input("Em quantos anos pretende financiar? "))
    parcela = casa / ( anos * 12)

    if parcela > (30/100) * salario:
        print("Lamento, seu financiamento foi NEGADO para {} meses!!".format(parcela))
    else:
        print("PARABÉNS, seu financiamento foi APROVADDO para {:.0f} meses!!".format(parcela))





main()