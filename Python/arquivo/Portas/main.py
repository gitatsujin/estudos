from portasFunc import verifica_portas

if __name__ == "__main__":
    n = int(input("Digite o número de portas a verificar: "))

    portas = []

    for i in range(n):
        porta = int(input(f"Porta {i+1}: "))
        portas.append(porta)

    verifica_portas(portas)