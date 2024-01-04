def main():
    velo = int(input("Qual a velocidade registrada:"))
    limite = 85
    multa = (velo - limite) * 7
    if velo <= 85:
        print ("Você esta dentro do limite de velocidade de {}km/h".format(limite))
    else:
        print("Você excedeu o limite de {}km/h e será multado em R${:.2f}".format(limite,multa))


main()