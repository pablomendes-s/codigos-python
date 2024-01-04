def ficha(nome='',gol=''):
    if nome == '':
        nome = "< Desconhecido >"
    if gol == '':
        gol = int(0)
    return f"O Jogador {nome} marcou {gol} Gol(s)."


nome = str(input("Nome do jogador: "))
gol = str(input("Quantidade de Gol(s): "))
print(ficha(nome,gol))