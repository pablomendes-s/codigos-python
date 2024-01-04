from exerc107.utilidadesCeV.moeda import*


while True:
    resposta = menu (['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        print("Opção 1")
    elif resposta == 2:
        print("Opção 2")
    elif resposta == 3:
        cabecalho('Saindo...Até logo!')
        break
    else:
        print("\33[31mERRO! Digite uma opção válida!\33[m")
