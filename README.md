# TrÃ­ade Letal

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![TrÃ­ade Letal](guia/assets/banner.jpg)](https://inematds.github.io/triade-letal/guia/)

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

Seu agente de IA pode vazar seus dados? Pode, se ele junta trÃªs coisas ao mesmo tempo (o nome Ã© de Simon Willison):

1. **Dados privados**: lÃª e-mail, agenda, banco de clientes, arquivos, `.env`.
2. **ConteÃºdo de terceiros**: lÃª texto que outra pessoa escreveu (WhatsApp, e-mail recebido, pÃ¡gina web, PDF).
3. **Canal de saÃ­da**: consegue mandar algo para fora (mensagem, URL, upload, webhook).

Com as trÃªs, qualquer pessoa que escreva o item 2 pode dar ordens ao agente. A defesa Ã© **cortar uma perna**.

## ðŸ“– Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/triade-letal/guia/**

## O que tem aqui

| Arquivo | Para quÃª |
|---|---|
| `inventario.py` | lista os servidores MCP do Claude Code e do Codex e monta a matriz para vocÃª preencher |
| `CHECKLIST.md` | o passo a passo e as defesas, da mais forte para a mais fraca |
| `EXEMPLOS.md` | a trÃ­ade nos kits atende-clinica, reserva-restaurante e reserva-hotel |

## Uso rÃ¡pido

```bash
git clone https://github.com/inematds/triade-letal && cd triade-letal
python3 inventario.py --demo          # exemplo fictÃ­cio
python3 inventario.py --md matriz.md  # sua mÃ¡quina; grava a matriz
```

O script sÃ³ lÃª arquivos de configuraÃ§Ã£o (`~/.claude.json`, `./.mcp.json`, `~/.codex/config.toml`). NÃ£o acessa a rede e nÃ£o imprime segredos. O "talvez" que ele marca Ã© palpite pelo nome; quem confirma Ã© vocÃª.

Inspirado na palestra de Simon Willison sobre os Ãºltimos seis meses de LLMs. Projeto irmÃ£o: [Arena da Capivara](https://inematds.github.io/arena-capivara/guia/).

LicenÃ§a MIT Â· [INEMA.CLUB](https://inema.club)

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>