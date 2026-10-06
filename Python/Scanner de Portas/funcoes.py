import socket

def validar_porta(entrada):
    while True:
        try:
            numero = int(input(entrada))
            
            if 1 <= numero <= 65535:
                return numero
            else:
                print("O número deve estar entre 1 e 65535.")
                
        except ValueError:
            print("Você deve digitar um número inteiro válido!")

def validar_host(entrada):
    while True:
        host = input(entrada).strip()
        if host == "":
            host = "127.0.0.1"
        try: 
            socket.gethostbyname(host)
            return host
        except socket.gaierror:
            print("Host inválido ou não encontrado. Tente novamente!")


def extrair_banner (banner):
    linhas = banner.split("\n")
    for linha in linhas:
        if linha.startswith("Server:"):
            return linha.strip()
    return banner.strip()

def porta_aberta(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((host, porta))
    s.close()
    return resultado == 0

def pega_banner (host, porta):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, porta))
        s.send(b"GET / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024)
        s.close()
        return banner.decode(errors="ignore").strip()
    
    except Exception:
        return None 

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

def escaneia_porta(host, porta):
    if porta_aberta(host, porta):
        banner = pega_banner(host, porta)
        servico = identifica_portas(porta)
        if banner:
            return (porta, servico, banner)
        else:
            return (porta, servico, None)
    return None