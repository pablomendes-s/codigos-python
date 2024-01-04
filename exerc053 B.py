frase = str(input("Digite uma frase e descubra se é um palindromo:")).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
inverso = ''
for p in range(len(junta) -1, -1, -1):
    inverso += junta[p]
print(junta, inverso)
if junta == inverso:
    print("É palindromo")
else:
    print("Não é Palindromo")