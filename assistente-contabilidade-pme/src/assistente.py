"""
Nina - Assistente de Contabilidade para Pequenos Negocios
Passo 4: Aplicacao funcional (CLI simples, sem dependencias externas)

Como funciona:
- Le a base de conhecimento em data/faq.json
- Para cada pergunta do utilizador, procura a entrada mais parecida (por palavras-chave)
- Se encontrar uma correspondencia razoavel, responde com base nela
- Se nao encontrar nada suficientemente proximo, diz claramente que nao sabe,
  em vez de inventar uma resposta (ver docs/prompts.md)
"""

import json
import os
import re

CAMINHO_FAQ = os.path.join(os.path.dirname(__file__), "..", "data", "faq.json")
LIMIAR_CONFIANCA = 0.34  # abaixo disto, a Nina assume que nao sabe

PALAVRAS_IGNORAR = {
    "o", "a", "os", "as", "um", "uma", "uns", "umas", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "para", "por", "com", "sem", "e", "ou", "que",
    "quais", "qual", "quanto", "quando", "como", "onde", "e", "ha", "sao", "ser",
    "meu", "minha", "meus", "minhas", "posso", "faco", "fazer", "sobre",
}


def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9áàâãéèêíïóôõöúçñ\s]", " ", texto)
    return texto


def extrair_palavras(texto):
    return {p for p in normalizar(texto).split() if p not in PALAVRAS_IGNORAR and len(p) > 1}


def carregar_base_conhecimento(caminho=CAMINHO_FAQ):
    with open(caminho, "r", encoding="utf-8") as ficheiro:
        return json.load(ficheiro)


def encontrar_melhor_resposta(pergunta_utilizador, base):
    palavras_pergunta = extrair_palavras(pergunta_utilizador)
    if not palavras_pergunta:
        return None, 0.0

    melhor_entrada = None
    melhor_pontuacao = 0.0

    for entrada in base:
        palavras_entrada = extrair_palavras(entrada["pergunta"])
        for tag in entrada.get("tags", []):
            palavras_entrada |= extrair_palavras(tag)

        intersecao = palavras_pergunta & palavras_entrada
        if not intersecao:
            continue

        # proporcao das palavras da pergunta do utilizador que foram reconhecidas
        pontuacao = len(intersecao) / len(palavras_pergunta)

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_entrada = entrada

    return melhor_entrada, melhor_pontuacao


def responder(pergunta_utilizador, base):
    entrada, pontuacao = encontrar_melhor_resposta(pergunta_utilizador, base)

    if entrada is None or pontuacao < LIMIAR_CONFIANCA:
        return (
            "Nao encontrei essa informacao na minha base de conhecimento atual. "
            "Para nao te dar um valor ou prazo errado, recomendo confirmares com um "
            "Contabilista Certificado (TOC) -- costuma depender do enquadramento "
            "especifico do teu negocio."
        )

    return entrada["resposta"]


def main():
    base = carregar_base_conhecimento()

    print("=" * 60)
    print("Nina - Assistente de Contabilidade para Pequenos Negocios")
    print("=" * 60)
    print("Pergunta algo sobre IVA, faturacao, recibos verdes, etc.")
    print("Escreve 'sair' para terminar.\n")

    while True:
        pergunta_utilizador = input("Tu: ").strip()
        if pergunta_utilizador.lower() in ("sair", "exit", "quit"):
            print("Nina: Ate breve!")
            break
        if not pergunta_utilizador:
            continue

        resposta = responder(pergunta_utilizador, base)
        print(f"Nina: {resposta}\n")


if __name__ == "__main__":
    main()
