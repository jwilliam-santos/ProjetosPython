#  Face Transformer

Um sistema de Realidade Aumentada (AR) em tempo real que utiliza Visão Computacional para mapear a malha facial 3D e aplicar efeitos dinâmicos.

## 🎯 Sobre o Projeto
O objetivo é criar uma camada de sobreposição digital que rastreia os movimentos e expressões faciais do usuário. O foco principal é aprender a manipular malhas (meshes) 3D, cálculos de transformação espacial e processamento de imagem de alta performance.

## 🛠️ Tecnologias
* **Linguagem:** Python
* **Bibliotecas:** `OpenCV`, `MediaPipe`, `NumPy`

# 🚀 Funcionalidades
**Rastreamento de Alta Precisão:** Mapeamento facial 3D em tempo real.
**Filtros Dinâmicos:** Sobreposição de elementos que acompanham rotação X, Y e Z.
**Performance Otimizada:** Processamento para manter 60 FPS estáveis.
**Modularidade:** Fácil adição de novos filtros ou máscaras.#

## 📂 Como rodar
1. Clone este repositório:
   `git clone https://github.com/jwilliam-santos/ar-face-transformer`
2. Instale as dependências:
   `pip install opencv-python mediapipe numpy`
3. Execute o sistema:
   `python main.py`

## 📂 Estrutura do Projeto
```text
AR-Face-Transformer/
├── README.md           # Documentação do projeto
├── main.py             # Ponto de entrada e loop de vídeo
├── assets/             # Filtros, máscaras e texturas
│   ├── filter_base.png
│   └── mask_layer.png
└── src/                # Módulos de processamento
    ├── __init__.py
    ├── processor.py    # Lógica de detecção MediaPipe
    └── filters.py      # Aplicação matemática dos filtros