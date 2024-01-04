prod = ('Detergente', 7.95,
        'Macarrão', 4.80,
        'Café', 3.80,
        'Cebola', 1.65,
        'Achocolatado', 7.75,
        'Bolacha', 5.98)
print("========LISTA MERCADO=======")
print("_"*35)
for c in range (0,len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:.<30}R$', end="")
    else:
        print(prod[c])
print("-"*30)