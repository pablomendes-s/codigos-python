def main ():
    from random import randint
    from time import sleep
    print("-=-"*15)
    print("Adivinhe o número que vou pensar de 1 a 5!!!")
    print("-=-" * 15)
    penso = randint(1,5)
    numero = int(input("Em que número estou pensando?"))
    print("PROCESSANDO...")
    sleep(3)
    print("Estou pensando no número: {}".format(penso))
    if numero == penso:
        print("Você acertou!!!")
    else:
        print ("Você errou!!")





main()
