def main() :
    import math
    cat1 = int(input("informe o valor do \33[00;34m primeiro cateto: "))
    cat2 = int(input("informe o valor do segundo cateto: "))
    h = math.hypot(cat1, cat2)
    print('A hipotenusa do triangulo é:{:.2f}'.format(h))


main()

