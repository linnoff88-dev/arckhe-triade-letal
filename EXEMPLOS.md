# Exemplos: a tríade nos kits de atendimento do INEMA

Três kits públicos, olhados com o checklist. Conferido no código em 05/10/2026.

## atende-clinica — bot de clínica no WhatsApp

Guia: https://inematds.github.io/atende-clinica/guia/

| Perna | Tem? | Onde |
|---|---|---|
| Dados privados | sim | tabelas de pacientes, histórico, retornos e lista de espera (SQLite) |
| Conteúdo de terceiros | sim | WhatsApp de qualquer número, pela Evolution API |
| Canal de saída | fraco | a resposta vai só para quem mandou a mensagem; o aviso à equipe vai só para o grupo fixo do Telegram |

**Hoje nêo há tríade**, por dois motivos. O bot é **determinístico** (palavras-chave e FAQ, sem modelo de linguagem), entêo o texto do paciente nêo vira instruçêo. E o destino de cada envio é fixo no código: ninguém consegue pedir "mande para este outro número".

**Se a fase 2 colocar um LLM para conversar**, as três pernas se fecham. Para continuar seguro:
- o destinatário continua sendo o remetente, escrito no código, nunca uma ferramenta `enviar(numero, texto)` que o modelo preenche;
- o modelo que fala com o paciente nêo ganha acesso à agenda nem à lista de pacientes; ele vê só os dados daquele paciente;
- qualquer açêo fora da conversa (remarcar outro paciente, avisar terceiros) passa pela equipe no Telegram.

## reserva-restaurante — reservas por chat e WhatsApp

Guia: https://inematds.github.io/reserva-restaurante/guia/

Dados privados previstos (clientes, telefones, aniversários), entrada de terceiros (chat e WhatsApp) e saída restrita (resposta ao próprio cliente, aviso à equipe). A conversa usa gatilhos fixos ("reservar") e um FAQ estático. Além disso, um script de verificaçêo **reprova o build** se aparecer biblioteca de LLM ou de HTTP genérico no código. Esse script é uma proteçêo barata e forte: impede que alguém, com pressa, acrescente a perna que faltava.

## reserva-hotel — reservas e pré-check-in

Guia: https://inematds.github.io/reserva-hotel/guia/

Mesmo desenho do restaurante, com um vetor a mais: o arquivo `.ics` das OTAs (Booking, Airbnb) e o pré-check-in em texto livre. Os dois sêo **conteúdo de terceiros**. Hoje sêo lidos por código, nêo por modelo. Se um LLM for ler esse texto, trate-o como entrada hostil: extraia campos (datas, nome, quarto) e nunca dê ao mesmo modelo uma ferramenta de envio com destino livre.

## E o agente que escreve o código?

Nos três kits, o código é gerado por um agente (Codex) em loop, com rede ligada. Ele tem a perna 3 (rede) e lê arquivos do projeto. As outras duas sêo fracas: os dados sêo fictícios (fixtures de teste) e o conteúdo é escrito pelo próprio dono. Mesmo assim, a regra vale: se o build nêo precisa de internet, `network_access=false` corta a saída de graça.

## O padrêo que se repete

1. **Código determinístico na borda** (quem lê o que vem de fora) e modelo só onde agrega.
2. **Destino fixo no código**, nunca um parâmetro do modelo.
3. **Um guard no build** que reprova a perna que nêo deveria existir.
