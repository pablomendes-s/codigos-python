def main ():
   n1 = int(input("\33[00;35m Digite um número para converte-lo:\33[m "))

   print ("Digite a opçãp de conversão:\n[1]Converter para BINÁRIO:\n[2]Converter para HEXADECIMAL:\n[3]Converter para OCTAL:")
   opcao= int(input("Qual sua opção?"))
   if opcao == 1:
       print("O número {} em binário é: {}".format(n1,bin(n1)[2:]))
   elif opcao == 2:
       print("O número {} em Hexadecimal fica: {}".format(n1,hex(n1)[2:]))
   elif opcao == 3:
       print ("O número {} em Octal, fica: {}".format(n1,oct(n1)[2:]))
   else:
       print("\33[00;33mOpção inválida, tente novamente!")



main()