cont = somag = menor = contmenor = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto:')).upper()
    valor = float(input('Valor do Produto: '))
    somag += valor
    contmenor += 1
    if valor >= 1000:
        cont += 1
    if contmenor == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    sig = ' '
    while sig not in 'SN':
        sig = str(input('Deseja Continuar [S/N]? ')).strip().upper()[0]
    if sig == 'N':
        break
print('-'*20)
print(f'''O valor total é de: R${somag}
A quantidade de produtos com valor maior que Mil reais é de :{cont}
O Menor valor cadastrado é: {menor}
E o Nome do produto mais barato é:{barato}''')
print('-=-'*10)
print('Cadastro Finalizado!!!')