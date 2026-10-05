import socket

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