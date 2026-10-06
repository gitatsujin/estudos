from portasDic import identifica_portas


if __name__ == "__main__":

    numeroPortas = int(input("Digite o numero de portas a serem verificadas: "))

    for i in range(numeroPortas):
        porta = int(input("Porta: "))
        print(identifica_portas(porta))