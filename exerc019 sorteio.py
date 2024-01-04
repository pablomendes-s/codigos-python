def main () :
    import random
    aluno1 = input("Digite o nome do 1º aluno para o sorteio:")
    aluno2 = input("Digite o nome do segundo aluno: ")
    aluno3 = input("Digite o nome do terceiro aluno: ")
    aluno4 = input("digite o nome do quarto e último aluno: ")
    lista = [aluno1, aluno2, aluno3, aluno4]
    sorteio = random.choice(lista)
    print("O aluno sorteado da vez foi: {}".format(sorteio))

main()