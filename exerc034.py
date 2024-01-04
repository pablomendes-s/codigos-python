def main():
    salario = float(input("Qual o valor do seu salário? "))
    if salario > 1250:
        print("Seu aumento será de 10% totalizando: {}".format(salario + (salario * 10/100)))
    else:
        print("Seu aumento será de 15% totalizando: {}".format(salario + (salario * 15/100)))




main()