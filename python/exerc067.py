n = 0
while True:
    n = int(input("Quer ver a tabuada de qua valor?"))
    print("=-=" * 10)
    if n < 0:
        break
    for cal in range (1, 11):
        print(f" {n} X {cal} = {n*cal}")
    print("=-="*10)
print("FIM!!!")