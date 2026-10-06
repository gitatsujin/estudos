import socket
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from funcoes import (
    pega_banner,
    identifica_portas,
    extrair_banner,
    validar_porta,
    validar_host,
    porta_aberta,
    escaneia_porta,
)

pasta = Path(__file__).parent

if __name__ == "__main__":

    host = validar_host("Digite o host: ")

    inicio = validar_porta("Digite a porta inicial: ")
    final = validar_porta("Digite a porta final: ")

    if inicio > final:
        inicio, final = final, inicio

    print(f"Varrendo {host} ...")

    # FASE 1 — escanear em paralelo (as threads fazem o trabalho pesado)
    resultados = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futuros = [executor.submit(escaneia_porta, host, porta) for porta in range(inicio, final + 1)]
        for futuro in futuros:
            resultado = futuro.result()
            if resultado is not None:
                resultados.append(resultado)

    # FASE 2 — ordenar por porta
    resultados.sort()

    # FASE 3 — apresentar (só LÊ o que já foi coletado, não escaneia de novo)
    with open(pasta / "Relatórios" / "Relatorio.txt", "w") as relatorio:
        for porta, servico, banner in resultados:
            if banner:
                print(f"[ABERTA] {porta} -> {servico} | {extrair_banner(banner)}")
                relatorio.write(f"{porta} -> {servico} | {banner}\n")
            else:
                print(f"[ABERTA] {porta} -> {servico} | (sem banner)")
                relatorio.write(f"{porta} -> {servico} | (sem banner)\n")

    print("Varredura terminada.")