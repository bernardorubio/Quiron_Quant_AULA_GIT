"""
Indicadores simples sobre uma série de preços.

Como rodar (a partir da pasta do projeto):
    python src/indicadores.py
"""

import csv
from pathlib import Path

ARQUIVO_PRECOS = Path(__file__).resolve().parent.parent / "dados" / "precos.csv"

# Quantos dias entram em cada média
janela = 3


def ler_precos(caminho):
    """Lê o CSV e devolve uma lista de pares (data, preço de fechamento)."""
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return [(linha["data"], float(linha["fechamento"])) for linha in leitor]


def media_movel(valores, janela):
    """Para cada dia, a média dos últimos `janela` valores.

    Os primeiros dias, que ainda não têm `janela` valores antes deles, ficam como None.
    """
    medias = []
    for i in range(len(valores)):
        if i + 1 < janela:
            medias.append(None)
        else:
            ultimos = valores[i + 1 - janela : i + 1]
            medias.append(sum(ultimos) / janela)
    return medias


def main():
    precos = ler_precos(ARQUIVO_PRECOS)
    datas = [data for data, _ in precos]
    fechamentos = [preco for _, preco in precos]
    medias = media_movel(fechamentos, janela)

    print(f"Média móvel de {janela} dias\n")
    print(f"{'data':<12}{'fechamento':>12}{'média':>12}")
    for data, preco, media in zip(datas, fechamentos, medias):
        texto_media = f"{media:.2f}" if media is not None else "-"
        print(f"{data:<12}{preco:>12.2f}{texto_media:>12}")


if __name__ == "__main__":
    main()

if peter == gay:
    break