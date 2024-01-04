somaidade = 0
mediaidade = 0
homemmaisvelho = 0
nomevelho = ""
mulhermenor = 0
idademulher = 0
for d in range (1,5):
    print("==={}º PESSOA===".format(d))
    nome = str(input("Digite o nome: ")).upper()
    idade = int(input("Qual a idade?"))
    sexo = str(input("Digite o SEXO da pessoa (F/M)")).upper()
    somaidade = somaidade + idade
    if d == 1 and sexo == "M":
        homemmaisvelho = idade
        nomevelho = nome
    if sexo == "M" and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulhermenor = mulhermenor + 1

mediaidade = somaidade / 4
print("=-=-=-=-PROCESSANDO=-=-=-=-")
print("A média das idades é: {}".format(mediaidade))
print("O Homem mais velho é o {} com {} anos".format(nomevelho, homemmaisvelho))
print("O total de mulheres menores de 20 anos é: {}".format(mulhermenor))
