def main():
    nome = str(input("Digite seu nome completo: "))
    print("Carregando dados do seu nome...")
    print ('Seu nome Maiusculo, fica: {}'.format(nome.upper()))
    print ('Seu nome minusculo, fica: {}'.format(nome.lower()))
    print ('Seu nome possui {} caracteres!!!'.format(len(nome)))



main()