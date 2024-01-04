n = ((int(input(f"Digite o  número: "))),(int(input(f"Digite o  número: "))),
         (int(input(f"Digite o  número: "))),(int(input(f"Digite o  número: "))),
         (int(input(f"Digite o  número: "))))
print(n)
print(f'O úmero NOVE apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número TRÊS esta na posição: {n.index(3)+1}')
else:
    print('O número 3 não foi digitao em nenhuma posição')
print("OS números pares são:", end=" ")
for num in n:
    if num % 2 == 0:
        print(num, end=" ")
