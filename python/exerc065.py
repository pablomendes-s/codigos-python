soma = cont = media = maior = menor = 0
pergunta = 's'
while pergunta in 'sS':
    n = int(input("Digite um número : "))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    pergunta = str(input("Quer continuar [s] para SIM [n] para NÃo:")).upper().strip()[0]
media = soma / cont
print("A média dos números inseridos é: {:.2f}".format(media))
print("O maior valor é {} e o menor {}".format(maior, menor))