import socket
from portasDic import identifica_portas

def porta_aberta(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.25)
    resultado = s.connect_ex((host, porta))
    s.close()
    return resultado == 0

if __name__ == "__main__":

    host = "127.0.0.1"
    with open ("Relatório.txt", "w") as relatorio:
        print(f"Varrendo {host} ...")
        for porta in range (1,6000):
            if porta_aberta(host, porta):
                print (f"[ABERTA] {porta} -> {identifica_portas(porta)}")
                relatorio.write(f"{porta} -> {identifica_portas(porta)}\n")
        print(f"Varredura concluída.")        