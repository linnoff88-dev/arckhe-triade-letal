#!/usr/bin/env python3
"""Inventário da tríade letal: lista os servidores MCP que seus agentes enxergam
e monta a matriz para VOCÊ preencher (dados privados / conteúdo de terceiros / canal de saída).

O script NÃO decide se você está seguro. Ele só junta o que está configurado e dá um palpite
pelo nome — quem confirma é você, olhando o que cada ferramenta faz de verdade.

Lê (só leitura, nunca imprime segredo):
  ~/.claude.json            mcpServers global e por projeto (Claude Code)
  ./.mcp.json               MCP do projeto atual (Claude Code)
  ~/.codex/config.toml      [mcp_servers.*] (Codex CLI)
  --arquivo X.json          qualquer outro arquivo no formato {"mcpServers": {...}}

Uso:
  python3 inventario.py                 # sua máquina
  python3 inventario.py --demo          # exemplo fictício, para ver o formato
  python3 inventario.py --md matriz.md  # grava a matriz em Markdown para preencher
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    tomllib = None

# Palpites pelo nome. É só ponto de partida: um "github" pode ler issue pública (terceiros)
# E abrir PR (saída). Confirme cada linha.
PISTAS = {
    "privado": r"gmail|mail|drive|docs|calendar|agenda|notion|slack|supabase|postgres|mysql|sqlite|db|banco|crm|hubspot|stripe|pay|files|filesystem|memory|obsidian|github|jira|linear|sheets",
    "terceiros": r"fetch|browser|chrome|playwright|puppeteer|web|search|busca|scrape|crawl|firecrawl|reddit|twitter|x\b|youtube|rss|whatsapp|telegram|evolution|gmail|mail|slack|github|issue|jira|discord",
    "saida": r"gmail|mail|send|smtp|slack|discord|telegram|whatsapp|evolution|webhook|fetch|browser|chrome|playwright|github|publish|publicar|metricool|twitter|social|sms|twilio|upload",
}

DEMO = {
    "Claude Code (global)": {
        "gmail": {"command": "npx", "args": ["gmail-mcp"]},
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "postgres-clientes": {"command": "npx", "args": ["@modelcontextprotocol/server-postgres"]},
    },
    "Codex CLI": {
        "playwright": {"command": "npx", "args": ["@playwright/mcp"]},
    },
}


def palpite(nome, cfg):
    alvo = (nome + " " + " ".join(map(str, cfg.get("args", []))) + " " + str(cfg.get("url", ""))).lower()
    return {perna: bool(re.search(rx, alvo)) for perna, rx in PISTAS.items()}


def transporte(cfg):
    if cfg.get("url"):
        host = re.sub(r"^https?://([^/]+).*", r"\1", cfg["url"])
        return f"{cfg.get('type', 'http')} {host}"
    cmd = cfg.get("command", "?")
    args = [a for a in cfg.get("args", []) if not re.search(r"key|token|secret|senha|password", str(a), re.I)]
    return (cmd + " " + " ".join(map(str, args[:2]))).strip()


def ler_claude():
    fontes = {}
    arq = Path.home() / ".claude.json"
    if arq.exists():
        d = json.loads(arq.read_text())
        if d.get("mcpServers"):
            fontes["Claude Code (global)"] = d["mcpServers"]
        for proj, v in (d.get("projects") or {}).items():
            if v.get("mcpServers"):
                fontes[f"Claude Code ({proj})"] = v["mcpServers"]
    local = Path.cwd() / ".mcp.json"
    if local.exists():
        fontes[f"Claude Code ({local})"] = json.loads(local.read_text()).get("mcpServers", {})
    return fontes


def ler_codex():
    arq = Path.home() / ".codex" / "config.toml"
    if not arq.exists():
        return {}
    if tomllib is None:
        return {"Codex CLI": {n: {} for n in re.findall(r"^\[mcp_servers\.([\w.-]+)\]", arq.read_text(), re.M)}}
    d = tomllib.loads(arq.read_text())
    return {"Codex CLI": d.get("mcp_servers", {})} if d.get("mcp_servers") else {}


def marca(b):
    return "talvez" if b else "-"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--arquivo", action="append", default=[])
    ap.add_argument("--md", help="grava a matriz em Markdown neste arquivo")
    a = ap.parse_args()

    fontes = dict(DEMO) if a.demo else {**ler_claude(), **ler_codex()}
    for extra in a.arquivo:
        fontes[extra] = json.loads(Path(extra).read_text()).get("mcpServers", {})

    linhas = []
    for fonte, servidores in fontes.items():
        for nome, cfg in servidores.items():
            p = palpite(nome, cfg or {})
            linhas.append((fonte, nome, transporte(cfg or {}), p))

    if not linhas:
        print("Nenhum servidor MCP encontrado. Isso não zera o risco: confira também as ferramentas")
        print("nativas do agente (navegador, shell, envio de mensagem) na matriz em CHECKLIST.md.")
        return 0

    cab = f"{'onde':<34} {'servidor':<22} {'privado':>8} {'terceiros':>10} {'saída':>7}  transporte"
    print(cab)
    print("-" * len(cab))
    for fonte, nome, tr, p in linhas:
        print(f"{fonte[:34]:<34} {nome[:22]:<22} {marca(p['privado']):>8} {marca(p['terceiros']):>10} {marca(p['saida']):>7}  {tr[:40]}")

    pernas = {k: any(p[k] for *_, p in linhas) for k in PISTAS}
    print()
    print("Palpite somado do conjunto (o agente que enxerga TODOS esses servidores ao mesmo tempo):")
    for k, rot in [("privado", "dados privados"), ("terceiros", "conteúdo de terceiros"), ("saida", "canal de saída")]:
        print(f"  {'[x]' if pernas[k] else '[ ]'} {rot}")
    if all(pernas.values()):
        print("\n  As três pernas podem estar juntas. Confirme linha a linha e corte uma perna (ver CHECKLIST.md).")

    if a.md:
        md = ["# Matriz da tríade letal", "",
              "Preencha com sim/não depois de olhar o que cada ferramenta faz. 'talvez' é só palpite do nome.", "",
              "| onde | servidor | dados privados | conteúdo de terceiros | canal de saída | o que vou cortar |",
              "|---|---|---|---|---|---|"]
        for fonte, nome, tr, p in linhas:
            md.append(f"| {fonte} | {nome} | {marca(p['privado'])} | {marca(p['terceiros'])} | {marca(p['saida'])} |  |")
        Path(a.md).write_text("\n".join(md) + "\n")
        print(f"\nmatriz gravada em {a.md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
