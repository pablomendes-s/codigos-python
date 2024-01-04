lista = []
par = []
impar = []
sig = " "
while True:
    n = int(input("Cadastre um número: "))
    lista.append(n)
    sig = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while sig not in "SN":
        sig = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if n % 2 == 0:
        par.append(n)
    if n % 2 != 0:
        impar.append(n)
    if sig in "N":
        break
print(lista)
print(f"Os números pares são:{par}")
print(f"Os números Impares são:{impar}")