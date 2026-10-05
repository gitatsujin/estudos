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