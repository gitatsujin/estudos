def separa_texto(texto, separador):
    return texto.split(separador)

if __name__ == "__main__":
    texto = input("Digite o que deseja separar ")
    separador = input("Digite o separador 1")

    print(separa_texto(texto, separador))