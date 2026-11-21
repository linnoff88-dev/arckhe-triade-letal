# Lethal Trifecta

[![Lethal Trifecta](guia/assets/banner-en.jpg)](https://inematds.github.io/triade-letal/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

Can your AI agent leak your data? It can, if it combines three things at once (the term is Simon Willison's):

1. **Private data**: it reads e-mail, calendar, customer database, files, `.env`.
2. **Third-party content**: it reads text someone else wrote (WhatsApp, incoming e-mail, web page, PDF).
3. **An exit channel**: it can send something out (message, URL, upload, webhook).

With all three, anyone who writes item 2 can give the agent orders. The defense is to **cut one leg**.

## 📖 Guide

Full guide (landing + step by step): **https://inematds.github.io/triade-letal/guia/en/**

## What's here

| File | Purpose |
|---|---|
| `inventario.py` | lists the MCP servers of Claude Code and Codex and builds the matrix for you to fill in |
| `CHECKLIST.md` | the steps and the defenses, strongest first (in Portuguese) |
| `EXEMPLOS.md` | the trifecta in the atende-clinica, reserva-restaurante and reserva-hotel kits (in Portuguese) |

## Quick start

```bash
git clone https://github.com/inematds/triade-letal && cd triade-letal
python3 inventario.py --demo          # fictional example
python3 inventario.py --md matriz.md  # your machine; writes the matrix
```

The script only reads configuration files (`~/.claude.json`, `./.mcp.json`, `~/.codex/config.toml`). It does not touch the network and does not print secrets. Its "talvez" (maybe) marks are a guess based on the name; you confirm them. The script output is in Portuguese.

Inspired by Simon Willison's talk on the last six months in LLMs. Sister project: [Capybara Arena](https://inematds.github.io/arena-capivara/guia/en/).

MIT license · [INEMA.CLUB](https://inema.club)
