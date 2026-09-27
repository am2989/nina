# Avaliação e Métricas — Nina

## Passo 5: Como testei

Segui a sugestão do desafio: fiz pelo menos 10 perguntas, incluindo uma fora do tema, e anotei o comportamento.

| # | Pergunta | Resposta correta? | Reconheceu que estava fora do âmbito quando aplicável? |
|---|----------|--------------------|-----------------------------------------------------------|
| 1 | O que é o regime simplificado? | ✅ Sim | — |
| 2 | O que é um recibo verde? | ✅ Sim | — |
| 3 | Quais as taxas de IVA em Portugal? | ✅ Sim | — |
| 4 | Como faço a minha declaração de rendimentos passo a passo? | ✅ Disse que não sabia | ✅ Sim |
| 5 | O que é uma reconciliação bancária? | ✅ Sim | — |
| 6 | Qual é a capital de Portugal? *(fora do tema)* | ❌ Respondeu sobre IVA em vez de dizer "não sei" | ❌ Não |
| 7 | O que é o NIF? | ✅ Sim | — |
| 8 | Posso deduzir despesas com o meu carro pessoal? | ✅ Disse que não sabia | ✅ Sim |
| 9 | Diferença entre fatura e fatura-recibo? | ✅ Sim | — |
| 10 | Expliquem-me a Segurança Social para independentes | ✅ Sim | — |

**Taxa de acerto:** 9/10 (90%)

## O que aprendi com o teste 6 (falha)

A pergunta "Qual é a capital de Portugal?" não tem nada a ver com contabilidade, mas
partilhava a palavra "Portugal" com uma entrada da base de conhecimento (taxas de IVA),
o que foi suficiente para ultrapassar o limiar de confiança do algoritmo simples de
correspondência por palavras-chave.

**Causa:** a versão atual (`src/assistente.py`) usa correspondência de palavras-chave, não
compreensão real de linguagem — não sabe distinguir "assunto relacionado" de "palavra em
comum por acaso".

**Como corrigir numa próxima iteração:**
1. Aumentar a lista de palavras a ignorar (nomes de países, geografia genérica)
2. Ligar a um modelo de IA real (ver `docs/prompts.md`), que entende contexto e não só
   palavras isoladas
3. Adicionar uma verificação extra: se a pergunta não contiver nenhuma palavra "âncora"
   do domínio (iva, fatura, imposto, contabilidade, etc.), recusar responder por defeito

## Métricas que faria sentido acompanhar numa versão futura

- Percentagem de perguntas respondidas corretamente
- Percentagem de "não sei" corretos vs. incorretos (falsos positivos como o caso 6)
- Tempo médio de resposta
- Perguntas mais frequentes sem resposta (para saber o que adicionar à base de conhecimento)
