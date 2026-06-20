# ⚔️ Simulador de RPG em Turnos (Texto)

Um simulador de jogo de RPG de turno jogado inteiramente via terminal. O projeto foi desenvolvido com o objetivo de consolidar conceitos fundamentais de programação em Python, focando em lógica pura, manipulação de estruturas de dados complexas, controle de fluxo e modularização por meio de funções, sem o uso de interfaces gráficas (GUI).

---

## 🎮 Funcionalidades Principais

### 1. Sistema de Combate e IA Contextual
* **Combate por Turnos:** Ciclo iterativo (`while`) onde o jogador e o inimigo alternam ações (Atacar, Usar Habilidade, Curar, Defender).
* **Máquina de Estados para Inimigos:** Os monstros não atacam de forma puramente aleatória; eles analisam o contexto da batalha (como a própria vida baixa ou ações iminentes do jogador) para decidir entre atacar, defender ou curar.

### 2. Gerenciamento de Estado e Inventário
* **Inventário Limitado por Peso:** Itens armazenados em dicionários contendo atributos de peso e quantidade. O sistema valida se novas coletas ultrapassam a capacidade máxima de carga do herói.
* **Efeitos de Status Prolongados (Buffs/Debuffs):** Lógica para aplicar e rastrear condições que persistem por múltiplos turnos, como envenenamento (dano contínuo), atordoamento (perda de turno) ou escudos de proteção.

### 3. Progressão e Customização
* **Árvore de Habilidades (Skill Tree):** Sistema de dependências estruturado em dicionários aninhados. O jogador gasta pontos obtidos em combate para liberar novas técnicas, respeitando pré-requisitos de nível e caminhos de aprendizado.

### 4. Persistência de Dados
* **Sistema de Save Game:** Funções dedicadas para serializar o estado atual do personagem (vida, inventário, progresso) e gravá-lo em um arquivo local, permitindo retomar a jornada posteriormente através da leitura e reconstrução dos dados.


