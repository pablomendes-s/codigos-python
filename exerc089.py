lista = []
sig = " "
media = 0
while True:
    nome = str(input("Nome do Aluno: "))
    nota1 = float(input("1º Nota:"))
    nota2 = float(input("2º Nota:"))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    sig = str(input("Deseja continar [S/N]? ")).strip().upper()[0]

    while sig not in "SN":
        sig = str(input("Deseja continar [S/N]? ")).strip().upper()[0]
    if sig == "N":
        break
print('=== BOLETIM ESCOLAR ===')
print('=-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, l in enumerate (lista):
    print(f"{i:<4}{l[0]:<10}{l[2]:>8.1f}")
while True:
    print('~~'*20)
    opc = int(input("Qual aluno deseja consultar a nota? [ou 999 para SAIR]: "))
    if opc == 999:
        print("Finalizando...")
        break
    else:
        print(f"As notas do aluno {lista[opc][0]} são {lista[opc][1]}")
print("Volte Sempre!!!")