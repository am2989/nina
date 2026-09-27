# Pitch — Nina (3 minutos)

## 1. O problema (30s)

Muitos pequenos empresários e trabalhadores independentes em Portugal não têm um
contabilista à distância de uma mensagem para tirar dúvidas rápidas do dia a dia — o que é
IVA, quando emitir uma nota de crédito, o que é um recibo verde. Acabam a adiar decisões,
a perguntar ao Google e por vezes a cometer erros que custam dinheiro.

## 2. A solução (45s)

A Nina é um assistente que responde a essas perguntas básicas de forma simples e honesta:
quando não sabe, diz que não sabe, em vez de inventar uma resposta — o que é essencial
em contabilidade, onde um erro pode ter custo real.

## 3. Demonstração (60s)

*(mostrar ao vivo, no terminal, 2-3 perguntas: uma que a Nina sabe responder bem, e uma
fora do âmbito para mostrar que ela recusa arriscar uma resposta errada)*

```
Tu: o que é um recibo verde?
Nina: O recibo verde é o documento fiscal emitido por trabalhadores independentes...

Tu: quanto vou pagar de IVA este mês?
Nina: Não encontrei essa informação na minha base de conhecimento atual...
```

## 4. Como foi construído (30s)

- Base de conhecimento com 12 perguntas frequentes sobre fiscalidade e contabilidade
  em Portugal (`data/faq.json`)
- Motor de resposta por palavras-chave, testado com 10 perguntas (90% de acerto)
- Persona e prompts documentados para evoluir facilmente para um modelo de IA real

## 5. Próximos passos (15s)

- Ligar a um LLM real seguindo o prompt em `docs/prompts.md`
- Expandir a base de conhecimento com mais temas (Segurança Social, faturação eletrónica)
- Adicionar uma interface web simples (ex.: Streamlit)

---
*Link do repositório: (https://github.com/am2989/nina)*
