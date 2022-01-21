import adivinha
import forca


def escolhe_jogo():
    print("*****************************************")
    print("***** Bem vindo ao seletor de Jogos! ****")
    print("*****************************************")

    print("1 - Jogo da Força | 2 - Advinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando Força")
        adivinha.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        forca.jogar()
    else:
        print("Jogo inválido!")


if (__name__ == "__main__"):
    escolhe_jogo()
