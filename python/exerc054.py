contmaior = 0
contmenor = 0
bibli1 = []
bibli2 = []
for lista in range (1,3):
    nome = str(input("Qual o \33[33mNOME\33[m da {}º pessoa?".format(lista)))
    idade = int(input("Qual a \33[35mIDADE\33[m da {}º pessoa?".format(lista)))
    if idade < 21:
        contmenor += 1
        bibli1 = [nome]
    elif idade >= 21:
        contmaior += 1
        bibli2 = [nome]
print("O número de pessoas MAIORES de idade são {} e seus nomes são {} ".format(contmaior, bibli2))
print("O número de pessoas MENORES de idade são: {} e seus nomes são{} ".format(contmenor, bibli1))


