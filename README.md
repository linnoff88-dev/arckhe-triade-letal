ï»¿# TrêÂ­ade Letal

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![TrêÂ­ade Letal](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/arckhe-/guia/)

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

Seu agente de IA pode vazar seus dados? Pode, se ele junta trêÂªs coisas ao mesmo tempo (o nome êÂ© de Simon Willison):

1. **Dados privados**: lêÂª e-mail, agenda, banco de clientes, arquivos, `.env`.
2. **ConteêÂºdo de terceiros**: lêÂª texto que outra pessoa escreveu (WhatsApp, e-mail recebido, pêÂ¡gina web, PDF).
3. **Canal de saêÂ­da**: consegue mandar algo para fora (mensagem, URL, upload, webhook).

Com as trêÂªs, qualquer pessoa que escreva o item 2 pode dar ordens ao agente. A defesa êÂ© **cortar uma perna**.

## ê°Å¸ââ Guia de uso

Guia completo (landing + passo a passo): **https://linnoff88-dev.github.io/arckhe-/guia/**

## O que tem aqui

| Arquivo | Para quêÂª |
|---|---|
| `inventario.py` | lista os servidores MCP do Claude Code e do Codex e monta a matriz para vocêÂª preencher |
| `CHECKLIST.md` | o passo a passo e as defesas, da mais forte para a mais fraca |
| `EXEMPLOS.md` | a trêÂ­ade nos kits atende-clinica, reserva-restaurante e reserva-hotel |

## Uso rêÂ¡pido

```bash
git clone https://github.com/linnoff88-dev/triade-letal && cd triade-letal
python3 inventario.py --demo          # exemplo fictêÂ­cio
python3 inventario.py --md matriz.md  # sua mêÂ¡quina; grava a matriz
```

O script sêÂ³ lêÂª arquivos de configuraêÂ§êÂ£o (`~/.claude.json`, `./.mcp.json`, `~/.codex/config.toml`). NêÂ£o acessa a rede e nêÂ£o imprime segredos. O "talvez" que ele marca êÂ© palpite pelo nome; quem confirma êÂ© vocêÂª.

Inspirado na palestra de Simon Willison sobre os êÂºltimos seis meses de LLMs. Projeto irmêÂ£o: [Arena da Capivara](https://linnoff88-dev.github.io/arckhe-/guia/).

LicenêÂ§a MIT êÂ· [ARCKHÉ AI](https://ARCKHÉ AI)

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>