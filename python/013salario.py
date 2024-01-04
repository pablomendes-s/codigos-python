def main():
    salario = float(input("Informe o valor do seu salário atual:"))
    aumento = salario * 0.15
    aumento2 = salario + aumento
    print("O eu novo salário com aumento de 15% é de: {:.2f}".format(aumento2))



main()