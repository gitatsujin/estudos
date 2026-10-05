from portasDic import identifica_portas

def verifica_portas(lista_de_portas):
    for porta in lista_de_portas:
            servico = identifica_portas(porta)
            print(f"{porta} -> {servico}")