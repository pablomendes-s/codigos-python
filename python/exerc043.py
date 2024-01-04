def main():
    peso = float(input("Qual seu peso?"))
    altura = float(input("Qual sua altura em metros?"))
    imc = peso / (altura ** 2)
    print ("Com altura de {} e peso de {}kg seu IMC é de: {:.2f}".format(altura, peso, imc))
    if imc < 18.5:
        print("Você esta ABAIXO do peso!")
    elif imc >= 18.5 and imc < 25:
        print("Peso ideal!")
    elif imc >= 25 and imc < 30:
        print("Você esta com sobrepeso!")
    elif imc >= 30 and imc < 40:
        print("Você esta com OBESIDADE!")
    elif imc >= 40:
        print("Voce esta com OBESIDAE MÓRBIDA!!")

main()