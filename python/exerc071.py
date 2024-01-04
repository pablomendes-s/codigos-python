print('======Banco Mendes====')
valor = int(input("Qual valor deseja sacar: R$"))
cedula = 50
valorfinal = valor
contc = 0
while True:
    if valorfinal >= cedula:
        valorfinal -= cedula
        contc += 1
    else:
        print(f" Total de {contc} cedulas de {cedula}")
        if cedula == 50:
            cedula = 20
            contc += 1
        elif cedula == 20:
            cedula = 10
            contc += 1
        elif cedula == 10:
            cedula = 1
            contc += 1
        contc = 0
        if valorfinal == 0:
            break

