import socket
from portasDic import identifica_portas

def porta_aberta(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((host, porta))
    s.close()
    return resultado == 0

if __name__ == "__main__":

    host = "127.0.0.1"
    with (
        open ("portas.txt") as arquivo, 
        open ("RelatórioPortas.txt", "w") as relatorio, 
        open ("PortasInválidas.txt", "w") as log_erros
        ):
        for linha in arquivo:
            try:
                porta = int(linha.strip())
                if porta < 1 or porta > 65535:
                    log_erros.write(f"{linha.strip()} está fora da faixa de portas (1-65535)\n")
                elif porta_aberta(host, porta):
                    print(f"[ABERTA] {porta} -> {identifica_portas(porta)}")
                    relatorio.write(f"{linha.strip()} -> {identifica_portas(porta)} [ABERTA]\n")
                else:
                   relatorio.write(f"{linha.strip()} Fechada\n")
            except ValueError:
                log_erros.write(f"{linha.strip()} não é uma porta válida\n")