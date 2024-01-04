def main():
    print("=-=" * 10)
    print("Digite a medida de 3 retas para ver se formam um triangulo:")
    print("=-="*10)
    r1 = int(input("Digite o comprimento da \33[00;33m 1º reta\33[m: "))
    r2 = int(input("Digite o comrimento da \33[00;34m2º reta\33[m: "))
    r3 = int(input("Digite o comprimento da \33[00;35m3º reta\33[m: "))
    if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
        print("È possivel formar um triangulo!")
    else:
        print("NÃO é possivel formar um triangulo!")
main()