import socket
from pega_banner import pega_banner

def porta_aberta(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((host, porta))
    s.close()
    return resultado == 0

def identifica_portas(porta):

    portas = {
        20 : "FTP (Dados)",
        21 : "FTP (Controle)",
        22 : "SSH",
        23 : "Telnet",
        25 : "SMTP",
        53 : "DNS",
        80 : "HTTP",
        110 : "POP3",
        143 : "IMAP",
        443 : "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP alternativo"
    }

    return portas.get(porta, "Porta desconhecida")

if __name__ == "__main__":

    host = "127.0.0.1"
    with open("Relatorio.txt", "w") as relatorio:
        print(f"Varrendo {host} ...")
        for porta in range (1,6001):
            if porta_aberta(host, porta):
                banner = pega_banner(host, porta)
                if banner:
                    print(f"[ABERTA] {porta} -> {identifica_portas(porta)} | Banner: {banner}")
                    relatorio.write(f"{porta} -> {identifica_portas(porta)} | {banner}\n")
                else:
                    print(f"[ABERTA] {porta} -> {identifica_portas(porta)} | (sem banner)")
                    relatorio.write(f"{porta} -> {identifica_portas(porta)} | (sem banner)\n")                
        print("Varredura terminada.")