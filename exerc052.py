def main():
    n = int(input("Digite um número Inteiro: "))
    for c in range(1, n + 1):
        if n % c == 0:
            print("\33[32m", end=" ")

        else:
            print("\33[35m", end=" ")
        print("{}".format(c), end=" ")

main()
