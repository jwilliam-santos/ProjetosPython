# Pong 2.0 - Python Implementation

Um projeto de prática para consolidar lógica de programação, detecção de colisões e o uso de Game Loops com **Pygame**.

## 🎮 Sobre o Projeto
O objetivo deste projeto é recriar o clássico *Pong* com uma estrutura de código profissional. O foco principal é aprender a manipular o fluxo de um jogo, tratar inputs em tempo real e lidar com colisões geométricas, preparando o terreno para o desenvolvimento de sistemas mais complexos.

## 🛠️ Tecnologias
*   **Linguagem:** Python
*   **Biblioteca:** `Pygame`
*   **Conceitos chave:**
    *   `Game Loop` (Estrutura fundamental de qualquer engine).
    *   `Match-case` para gerenciamento de estados (Menu, Jogando, Pause).
    *   Vetores e detecção de colisão (AABB - Axis-Aligned Bounding Box).

## 🚀 Funcionalidades
- [ ] **Game Loop Fluido:** Renderização estável a 60 FPS.
- [ ] **Sistema de Estados:** Alternância entre menus e gameplay usando lógica `match-case`.
- [ ] **IA Básica ou Multiplayer:** Implementação de controle para o player 2.
- [ ] **Aceleração Dinâmica:** A bola aumenta a velocidade a cada rebatida para aumentar a dificuldade.

## 📂 Como rodar
1. Clone este repositório:
   `git clone https://github.com/jwilliam-santos/pong-2.0`
2. Instale o Pygame:
   `pip install pygame`
3. Execute o jogo:
   `python main.py`
## 📂 Estrutura do Projeto

```text
Pong/
├── README.md           # Documentação específica deste projeto
├── main.py             # Ponto de entrada do jogo
├── assets/             # Recursos (imagens, sons, fontes)
│   ├── sound.wav
│   └── sprite.png
└── src/                # Módulos e lógica do código
    ├── __init__.py
    ├── game.py         # Lógica principal do game loop
    └── physics.py      # Cálculos de colisão e movimento