# 🌊 Sistema de Monitoramento de Níveis de Água

Este projeto consiste num sistema simples de monitorização de reservatórios de água desenvolvido em Python para execução no terminal. O objetivo é simular um ambiente real de controlo de risco, utilizando alertas visuais coloridos de acordo com o nível atual da água.

Projeto desenvolvido para a atividade de recuperação da **Agenda 11 - Bibliotecas** do curso técnico em **Desenvolvimento de Sistemas I (ETEC)**.

---

## 🚀 Funcionalidades

- **Mapeamento de Níveis:** Categorização do reservatório em 5 níveis de risco.
- **Alertas Coloridos:** Uso da biblioteca externa `colorama` para destacar cada situação com cores específicas no terminal.
- **Função de Mapeamento de Cores:** Algoritmo dedicado para associar o nível de água à respetiva cor ANSI.
- **Restauração de Estilo:** Reset automático da cor do terminal após a exibição das mensagens (`Style.RESET_ALL`).

---

## 📊 Tabela de Níveis e Cores

| Nível | Situação | Cor no Terminal |
| :---: | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho |
| **Nível 2** | Baixo | 🟡 Amarelo |
| **Nível 3** | Médio | 🟢 Verde |
| **Nível 4** | Alto | 🔵 Ciano |
| **Nível 5** | Muito alto (alerta) | 🟦 Azul |
