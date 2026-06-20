#Aqui vai ficar o Dic com os itens

itens_jogo = {
    # --- ITENS DE CURA ---
    "pocao_pequena": {
        "nome": "Poção de Cura Menor",
        "peso": 0.5,
        "tipo": "Consumível",
        "cura": 30,
        "defesa": 0,
        "dano": 0,
    },
    "elixir_vital": {
        "nome": "Elixir do Xamã",
        "peso": 0.8,
        "tipo": "Consumível",
        "cura": 60,
        "defesa":0,
        "dano" : 0
    },
    "pedra_filosofal_derretida": {
        "nome": "Pedra Filosofal Derretida",
        "peso": 5.0,
        "tipo": "DROP BOSS",
        "cura": 120,
        "vida_max": 220,
        "defesa":0,
        "dano":0,
    },

    # --- ITENS PADRÃO (Equipamentos) ---
    "Espada_Ferro": {
        "nome": "Espada de Ferro",
        "peso": 4.0,
        "tipo": "Arma",
        "dano": 8,
        "defesa": 0
    },
    "armadura_couro": {
        "nome": "Armadura de Couro",
        "peso": 8.0,
        "tipo": "Armadura",
        "defesa": 6,
        "dano" : 0
    },
    "escudo_madeira": {
        "nome": "Escudo de Madeira",
        "peso": 5.0,
        "tipo": "Armadura",
        "defesa": 4,
        "dano":0
    },

   # DROP BOSS
    "adaga_gax": {
        "nome": "Adaga Serrilhada de Gax",
        "peso": 2.0,
        "tipo": "Drop",
        "dano": 14,
        "defesa": 0
    },  
    "colar_orc": {
        "nome": "Amuleto rúnico do Orc",
        "peso": 1.5,
        "tipo": "Acessório",
        "dano": 5,
        "defesa": 5
    },
    "coracao_grakos": {
        "nome": "Núcleo de Pedra de Grakos",
        "peso": 30.0,  
        "tipo": "Relíquia",
        "dano": 10,
        "defesa": 25
    }
}
itens_cura = []
for item in itens_jogo.values():
    if item["tipo"] == "Consumível":
        itens_cura.append(item)
itens_padrao = []
for item in itens_jogo.values():
    if item["tipo"] in ["Arma", "Armadura","Escudo"]:
        itens_padrao.append(item)
