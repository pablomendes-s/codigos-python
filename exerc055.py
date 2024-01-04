maiorp = 0
menorp = 0
for bal in range(1,6):
    peso = float(input("Qual o peso da {}º pessoa? ".format (bal)))
    if bal == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso

print("O menor peso é: {}".format(menorp))
print("O MAIOR peso é: {}".format(maiorp))

