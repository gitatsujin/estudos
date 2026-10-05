import math


def somar(*numeros):
    return sum(numeros)

def subtrair(primeiro, *numeros):
    total = primeiro
    for numero in numeros:
        total -= numero
    return total

def subtrair_nova(primeiro, *numeros):
    return primeiro - sum(numeros)

def multiplicar(primeiro, *numeros):
    total = primeiro
    for numero in numeros:
        total *= numero
    return total

def multiplicar_nova(*numeros):
    return math.prod(numeros)

def dividir(dividendo, *divisores):
    total = dividendo
    for divisor in divisores:
        if divisor == 0:
            raise ValueError("Divisão por zero tende ao infinito")
        total /= divisor
    return total

def potencia(base, expoente):
    if isinstance(expoente, int) and expoente >= 0:
        total = 1
        for _ in range(expoente):
            total *= base
        return total
    raise ValueError("Somente expoentes inteiros igual ou maior que zero")

def potencia_nova(base, expoente):
    return base ** expoente

def raizQuadrada(numero):
    if numero < 0:
        raise ValueError("Somente números não negativos")
    return math.sqrt(numero)

def media(*numeros):
    if len(numeros) == 0:
        raise ValueError("Pelo menos um número deve ser fornecido")
    return sum(numeros) / len(numeros)

def resto(dividendo, divisor):
    if divisor == 0:
        raise ValueError("Divisor não pode ser zero")
    return dividendo % divisor

if __name__ == "__main__":
    print(somar(1,3,5))
    print(subtrair(10,2,4))
    print(multiplicar(10,3,4))
    print(dividir(120,4,3))
    print(potencia(2,3))
    print(raizQuadrada(16))
    print(media(1,3,5))
    print(resto(10,3))

    try:
        print(dividir(10,0))
    except ValueError as e:
        print("Erro esperado:", e)

    try:
        print(potencia(2, -1))
    except ValueError as e:
        print("Erro esperado:", e) 

    try:
        print(raizQuadrada(-16))
    except ValueError as e:
        print("Erro esperado:", e)  

    try:
        print(media())
    except ValueError as e:
        print("Erro esperado:", e)  

    try:
        print(resto(10, 0))
    except ValueError as e:
        print("Erro esperado:", e)  