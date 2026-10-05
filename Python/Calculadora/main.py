from operacoes import somar, subtrair, multiplicar, dividir, raizQuadrada, media, resto, potencia

while opcao != 0:
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz Quadrada")
    print("6. Média")
    print("7. Resto")
    print("8. Potência")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
            print(somar(*numeros))
        case 2:
            primeiro = float(input("Digite o primeiro número: "))
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
            print(subtrair(primeiro, *numeros))
        case 3:
            primeiro = float(input("Digite o primeiro número: "))
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
            print(multiplicar(primeiro, *numeros))
        case 4:
            dividendo = float(input("Digite o dividendo: "))
            divisores = list(map(float, input("Digite os divisores separados por espaço: ").split()))
            print(dividir(dividendo, *divisores))
        case 5:
            numero = float(input("Digite o número: "))
            print(raizQuadrada(numero))
        case 6:
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
            print(media(*numeros))
        case 7:
            dividendo = float(input("Digite o dividendo: "))
            divisor = float(input("Digite o divisor: "))
            print(resto(dividendo, divisor))
        case 8:
            base = float(input("Digite a base: "))
            expoente = int(input("Digite o expoente: "))
            print(potencia(base, expoente))
        case 0:
            print("Saindo...")
        case _:
            print("Opção inválida!")