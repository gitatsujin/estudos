def perguntar_nome():
    nome = input("Qual o seu nome? ")
    return nome

def perguntar_idade():
    idade = input("Qual a sua idade? ")
    return idade

def exibir_nome_idade(nome, idade):
    print(f"Olá, {nome}! Você tem {idade} anos.")

if __name__ == "__main__": 
    nome = perguntar_nome()
    idade = perguntar_idade()
    exibir_nome_idade(nome, idade)