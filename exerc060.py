fatorial = int(input("Digite um número para calcular seu fatorial: "))
resultado = fatorial
f = 1
while resultado > 0:
    print(" {} ".format(resultado), end= '')
    print("X" if resultado > 1 else "=", end='')
    f = f * resultado
    resultado -= 1
print(f)