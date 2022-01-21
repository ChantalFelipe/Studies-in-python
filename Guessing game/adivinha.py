def jogar():
    import random

    print("*****************************************")
    print("*** Bem vindo ao Jogo de Adivinhação! ***")
    print("*****************************************")

    total_tentativa = 1
    numero_secreto = random.randrange(1, 101)

    while total_tentativa <= 3:
        print("Tentativa {} de 3 tentativas".format(total_tentativa))

        chute_str = input("Digite um numero: ")
        chute_int = int(chute_str)
        if chute_int < 1 or chute_int > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if chute_int == numero_secreto:
            print("Acertou!")
            break
        else:
            if chute_int > numero_secreto:
                print("Não Acertou! Seu chute foi maior que o número secreto")
            else:
                print("Não Acertou! Seu chute foi menor que o número secreto")
        total_tentativa = total_tentativa + 1
    print("Fim de jogo!")
    print("O numero secreto era: {}".format(numero_secreto))


if (__name__ == "__main__"):
    jogar()
