from time import sleep
def contador (a, b, c):
    print("=-"*25)
    print(f"Contagem de {a} a {b}, em {c} em {c}")
    if a < b:
        for c in range (a, b, c):
            sleep(0.5)
            print(f"{c}", end = " ")
        print(" FIM!")
    else:
        for c in range(a, b, -c):
            sleep(0.5)
            print(f"{c}", end=" ")
        print(" FIM!")


contador(1,11, 1)
contador(10,0,2)
print("=-"*25)
print("~~~~CONTAGEM PERSONALIZADA~~~~")
a = int(input("Número inicial: "))
b = int(input("Número final: "))
c = int(input("Intervalo: "))
contador(a, b, c)