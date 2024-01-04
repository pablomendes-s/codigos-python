def main ():
    import random
    aluno1 = str(input("Digite o nome do 1º aluno para o sorteio:"))
    aluno2 = str(input("Digite o nome do segundo aluno: "))
    aluno3 = str(input("Digite o nome do terceiro aluno: "))
    aluno4 = str(input("digite o nome do quarto e último aluno: "))
    lista = [aluno1,aluno2,aluno3,aluno4]
    random.shuffle(lista)
    print("O aluno sorteado da vez foi:")
    print (lista)



main()