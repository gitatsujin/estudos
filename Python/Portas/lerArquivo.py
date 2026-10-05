from portasDic import identifica_portas

if __name__ == "__main__":

    with (open ("portas.txt") as arquivo, 
          open ("Relatório.txt", "w") as saida, 
          open("Portas inválidas.txt", "w") as log_erros
):
        for linha in arquivo:
            try:
                porta = int(linha.strip())
                saida.write(f"{porta} -> {identifica_portas(porta)}\n")
            except ValueError:
                log_erros.write(f"{linha.strip()} não é uma porta válida\n")
