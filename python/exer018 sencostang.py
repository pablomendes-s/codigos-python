def main ():
    import math
    ang = float(input("Digite o valor de um angulo qualquer: "))
    cosseno = math.cos(math.radians(ang))
    print("O angulo de {} tem o COSSENO de: {:.2f}".format(ang, cosseno))
    seno = math.sin(math.radians(ang))
    print("O angulo de {} tem o SENO de: {:.2f}".format(ang, seno))
    tangente = math.tan(math.radians(ang))
    print("O angulo {} tem a TANGENTE de: {:.2f}".format(ang, tangente))


main()