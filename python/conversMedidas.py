def main ():
    medida = float(input("Digite uma medida em Metros:"))
    cent = medida * 100
    mili = medida * 1000
    print("A conversão de {}m em centimetros é {}cm e em mmilimetros é {}mm ".format(medida,cent,mili))

main()