def identifica_portas(porta):
    if porta == 80:
        return "HTTP"
    elif porta == 443:
        return "HTTPS"
    elif porta == 22:
        return "SSH"
    else:
        return "Porta desconhecida"

if __name__ == "__main__":
    porta = int(input("Digite a porta que deseja identificar: "))

    print(identifica_portas(porta))