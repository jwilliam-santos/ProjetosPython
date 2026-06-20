#IMPORTS
import random
import time
import json
from itens import itens_jogo, itens_padrao
from database import Goblin, Orc, Golem

carregar = input("Se você tiver um save e quiser carrega-lo digite 0, se não aperte enter.").strip()
if carregar == "0":
    arquivocarregar = input("Digite o nome do arquivo json para carrega-lo (como .json)")
    with open(arquivocarregar,"r") as f:#PRONTO
        try:
            Jogador = json.load(f)
        except FileNotFoundError:
            print("Save não encontrado")
else:
    print("Olá jogador, nesse maravilhoso mundo você, é o dono da historia, mas antes me diga algumas informações")
    nome = input("Qual o seu nome?\n")
    idade = int(input("Me informe sua Idade por favor:\n"))
    print(f"Olá {nome} ganhou uma espada de cobre, uma mochila é uma armadura")
    print("Mas infelizmente você so aguenta carregar 50Kg no total e sua vida é 100, sua defesa inicial e 5, para aumenta-la presica de uma armadura")
    print("A defesa diminui o Dano tomado em número, por exemplo com 5 de defesa em vez de levar 10 de ataque, levaria 5")
#time.sleep(2)
vida_max = 100
vida_max_com_boost = 220
Peso_Max = 50     # VERIFICAR SE PASSOU DOS 50KG,
pode_colocar_item = True

#time.sleep(3)
#time.sleep(1)
#Função de Inventário: Adicionar item checando peso (< 50Kg) e usar item de cura. FALTA USAR ITEM DE CURA
#Loop de Combate: Criar um 'while' (enquanto vida de ambos > 0) com menu de ações. FEITO
#IA dos Monstros: Criar regras condicionais ( Orc cura, Grakos carrega ataque).
#Save/Load: Funções com o módulo 'json' para salvar e carregar o progresso num arquivo. COMPLETO
Inventario = []
Jogador = {
    "nome" : nome,
    "idade": idade,
    "vida" : 100,
    "vida_max": 100,
    "defesa": 5,
    "Peso" : 20,  #SOMAR PESO COM O INVENTARIO, Dano também
    "dano": 15,    
    "mochila": Inventario
}
if carregar == "0":
    arquivocarregar = input("Digite o nome do arquivo json para carrega-lo (como .json)")
    with open(arquivocarregar,"r") as f:#PRONTO
        try:
            Jogador = json.load(f)
        except FileNotFoundError:
            print("Save não encontrado")

    
def verificar_peso(item): 
    global pode_colocar_item
    if Jogador["Peso"] + item["peso"] <= 50:
        print("O jogador Pode colocar item")
        pode_colocar_item = True
    if Jogador["Peso"] + item["peso"] > 50:
        print("O jogador não pode colocar mais nada no inventario")
        pode_colocar_item = False

def exibir_status_jogador():#PRONTO
    print("\n--- STATUS DO JOGADOR ---")
    print(f"Nome: {Jogador['nome']}")
    print(f"Idade: {Jogador['idade']} anos")
    print(f"Vida: {Jogador['vida']}/100")
    print(f"Defesa: {Jogador['defesa']}")
    print(f"Dano: {Jogador['dano']}")
    print(f"Peso Atual: {Jogador['Peso']}Kg")
    print("-------------------------\n")

def procurar_itens():
    
    item_final = random.choice(itens_padrao)
    print(f"Você encontrou um(a) {item_final['nome']} no chão!")
    print(f"As caracterististicas do item são {item_final}")
    verificar_peso(item_final)
    if pode_colocar_item == True:
        Jogador["mochila"].append(item_final)
        Jogador["Peso"] += item_final["peso"]
        Jogador["dano"] += item_final["dano"]
        Jogador["defesa"] += item_final["defesa"]
        print("O Item esta no seu aniversario e equipado")
    elif pode_colocar_item == False:
        print("O item não foi adicionado ao seu inventario ")    

def escolha_atacar():
    print("Para escolhar qual irá atacar, digite:\n1-) Atacar Goblin\n2-)Atacar Orc\n3-) Atacar Golem")
    escolhad_ataque = input("Eai, Vai escolher qual?")
    if escolhad_ataque == "1":
        Inimigo = Goblin["nome"]
        vida = Goblin["vida"]
        dano = Goblin["dano"]            
        defesa = Goblin["defesa"]

def usar_consumivel():
    for c in Jogador["mochila"]:
        if c["tipo"] == "Consumível":
            confirmar = input("Quer usar o Consumível {c} Digite 's' somente\n").strip().lower
            if confirmar == "s":
                Jogador["Peso"] -= c["peso"]
                Jogador["mochila"].remove(c)
                print(f"O Consumível {c} foi Utilizado")
            else:
                print("Nada foi usado nem alterado")

def descartar():
    print("descartar um item é uma escolha permanente, tem certeza?")
    for c in Jogador["mochila"]:
        if c["tipo"] == "Consumível":
            confirmar = input("Quer descartar o item {c} Digite 's' se sim\n").strip().lower
            if confirmar == "s":
                Jogador["Peso"] -= c["peso"]
                Jogador["mochila"].remove(c)
                print(f"O Item {c} foi Descartado")
                if Jogador["vida"] > Jogador["vida_max"]:
                    Jogador["vida"] = Jogador["vida_max"]
            else:
                print("Nada foi descartado")

#LOOP WHILE DO JOGO
while Jogador["vida"] > 0:
    #=========================MENU DE OPÇÕES=================================
    print("\n\n\n")
    print("Para escolher você pode\n")
    print("1-)Atacar o Goblin Orc ou Golem\n") # FALTA ISSO
    print("2-)Olhar seu Inventario\n")#PRONTO
    print("3-)Procurar Itens\n") #PRONTO
    print("4-)Salvar O jogo é sair\n") #PRONTO
    print("5-)Sair sem salvar\n")#PRONTO
    print("6-)Mostrar estatisticas\n")#PRONTO
    print("7-)Usar algum consumível de seu inventario\n")
    print("8-)Retirar item do inventario (descarta-lo)\n")
    

    opção = input("Eai, qual opção vai ser a escolhida da vez?\nObs: digite só o número").strip()

    if opção == "1":
        print("Para escolhar qual irá atacar, digite:\n1-) Atacar Goblin\n2-)Atacar Orc\n3-) Atacar Golem")
        escolha_ataque = input("Eai, Vai escolher qual?")
        if escolha_ataque == "1":
            escolha_atacar()

    elif opção == "2":#PRONTO
        print(f"Seu Inventario é {Jogador["mochila"]}")
    
    elif opção == "3":
        procurar_itens()

    elif opção == "4": #PRONTO
        arquivo = input("Digite o nome do arquivo que vai querer salvar, com extensão .json no final")
        with open(arquivo,"w") as f:
            json.dump(Jogador,f,indent=4)
        print("Tchau, até a proxíma")
        break

    elif opção == "5":#PRONTO
        print("Tchau,ate a proxíma")
        break

    elif opção == "6":#PRONTO
        exibir_status_jogador()
    
    elif opção == "7":
        usar_consumivel()
    elif opção == "8":
        descartar()



    
            
