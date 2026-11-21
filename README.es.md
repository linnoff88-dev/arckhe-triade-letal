# Tríada Letal

[![Tríada Letal](guia/assets/banner-es.jpg)](https://inematds.github.io/triade-letal/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

¿Tu agente de IA puede filtrar tus datos? Puede, si junta tres cosas al mismo tiempo (el término es de Simon Willison):

1. **Datos privados**: lee correo, agenda, base de clientes, archivos, `.env`.
2. **Contenido de terceros**: lee texto que escribió otra persona (WhatsApp, correo recibido, página web, PDF).
3. **Canal de salida**: puede enviar algo hacia afuera (mensaje, URL, subida de archivo, webhook).

Con las tres, cualquiera que escriba el punto 2 puede darle órdenes al agente. La defensa es **cortar una pata**.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/triade-letal/guia/es/**

## Qué hay aquí

| Archivo | Para qué |
|---|---|
| `inventario.py` | lista los servidores MCP de Claude Code y Codex y arma la matriz para que la completes |
| `CHECKLIST.md` | los pasos y las defensas, de la más fuerte a la más débil (en portugués) |
| `EXEMPLOS.md` | la tríada en los kits atende-clinica, reserva-restaurante y reserva-hotel (en portugués) |

## Uso rápido

```bash
git clone https://github.com/inematds/triade-letal && cd triade-letal
python3 inventario.py --demo          # ejemplo ficticio
python3 inventario.py --md matriz.md  # tu máquina; graba la matriz
```

El script solo lee archivos de configuración (`~/.claude.json`, `./.mcp.json`, `~/.codex/config.toml`). No usa la red y no imprime secretos. El "talvez" (quizás) que marca es una suposición por el nombre; tú lo confirmas. La salida del script está en portugués.

Inspirado en la charla de Simon Willison sobre los últimos seis meses de LLMs. Proyecto hermano: [Arena del Capibara](https://inematds.github.io/arena-capivara/guia/es/).

Licencia MIT · [INEMA.CLUB](https://inema.club)
