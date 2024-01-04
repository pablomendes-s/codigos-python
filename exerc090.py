aluno = {}
aluno ['Nome'] = str(input("Nome: "))
aluno ['media'] = float(input("Qual a média? "))
print("=-="*20)
if aluno["media"] >= 7:
    aluno ['situação'] = 'APROVADO!'
elif 5 >= aluno["media"] < 7:
    aluno ['situação'] = "RECUPERAÇÂO!"
else:
    aluno ['situação'] = "REPROVADO!"
for k,i in aluno.items():
    print(f"  - {k} é igual a {i}")
print("=-=" * 20)