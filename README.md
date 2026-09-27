# Nina — Assistente de Contabilidade para Pequenos Negócios

Assistente virtual que ajuda pequenos empresários e trabalhadores independentes em Portugal a tirar dúvidas básicas de contabilidade e fiscalidade (IVA, faturação, recibos verdes, prazos), sem substituir o acompanhamento de um Contabilista Certificado.

Projeto desenvolvido para o desafio **"Construa Seu Assistente Virtual Com Inteligência Artificial"** do Bootcamp Bradesco (DIO).

## Porquê este tema

Trabalho há mais de 13 anos em contabilidade (faturação, reconciliações bancárias, IVA, folhas de pagamento). Muitos pequenos empresários perdem tempo e dinheiro por não perceberem conceitos básicos — a Nina tenta preencher essa lacuna com respostas simples, sem inventar informação fiscal.

## Estrutura do projeto

```
assistente-contabilidade-pme/
├── README.md
├── docs/
│   ├── agente.md         # Persona e documentação do agente
│   ├── prompts.md        # Prompts / instruções do agente
│   ├── avaliacao.md      # Testes e métricas
│   └── pitch.md          # Guião do pitch (3 min)
├── data/
│   └── faq.json          # Base de conhecimento
└── src/
    └── assistente.py     # Aplicação funcional (CLI)
```

## Como executar

Não precisa de instalar nada além do Python 3 (já vem com o `difflib` incluído).

```bash
cd src
python3 assistente.py
```

Escreva uma pergunta (ex.: `o que é o regime simplificado?`) e prima Enter. Escreva `sair` para terminar.

## Limitações (importante)

- A Nina responde apenas com base na `data/faq.json`. Se a pergunta não estiver coberta, ela diz claramente que não sabe, em vez de inventar.
- Não substitui aconselhamento profissional — é sempre recomendado confirmar com um Contabilista Certificado (TOC) para o caso concreto de cada negócio.
- Não trata, guarda nem pede dados sensíveis de clientes.

## Próximos passos

Ver `docs/avaliacao.md` para os testes feitos e `docs/pitch.md` para a apresentação final.
