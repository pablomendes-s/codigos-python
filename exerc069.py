sig = sexo =' '
contf = contm = contid = 0
print("CADASTRO E PESSOAS")
while True:
    idade = int(input('Qual idade? '))
    sexo = str(input('Qual o sexo [M/F]? ')).strip().upper()[0]
    sig = str(input('Deseja Continuar [S/N]? ')).strip().upper()[0]
    print("=-=" * 10)
    if sig == 'N':
        break
    if idade >= 18:
        contid += 1
    if sexo == 'F' and idade >= 20:
        contf += 1
    if sexo == 'M':
        contm += 1
print(f"{contid} pessoas possuem mais de 18 anos;\nPossui {contm} Homens cadastrados;\nPossui {contf} Mulheres maiores de 20 anos")

