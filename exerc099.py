from time import sleep
def maior(*num):
    print("="*20)
    cont = maior = 0
    for valor in num:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'\nFoi informado {cont} valores')
    print(f"O maior valor foi {maior}")


maior(5, 8, 9, 12, 54, 119)
maior(4,9,3,2,8)
maior(51,98,336,58,114)