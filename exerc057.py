sexo = str(input("Qual seu sexo: [M/F]? ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Dados inválidos, tente novamente: [M/f]?")).strip().upper()[0]
print("O sexo registrado foi o {}".format(sexo))
