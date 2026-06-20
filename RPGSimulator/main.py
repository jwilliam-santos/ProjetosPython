#IMPORTS
import random
import time
import json
from itens import itens_jogo, itens_padrao
from database import Goblin, Orc, Golem
print("Se tiver um save e quiser carrega-lo aperte enter no nome e idade")
print("Olá jogador, nesse maravilhoso mundo você, é o dono da historia, mas antes me diga algumas informações")

vida_max = 100
vida_max_com_boost = 220
Peso_Max = 50     
pode_colocar_item = True
idade = input("Me informe sua Idade por favor:\n")
nome = input("Qual o seu nome?\n")
carregar = input("Se você tiver um save e quiser carrega-lo digite 0, se não aperte enter.").strip()

print("Você ganhou uma espada de cobre, uma mochila é uma armadura")

print("Mas infelizmente você so aguenta carregar 50Kg no total e sua vida é 100, sua defesa inicial e 5, para aumenta-la presica de uma armadura")

print("A defesa diminui o Dano tomado em número, por exemplo com 5 de defesa em vez de levar 10 de ataque, levaria 5")
Inventario = []
Jogador = {
    "nome" : nome,
    "idade": idade,
    "vida" : 100,
    "vida_max": 100,
    "defesa": 5*2,
    "Peso" : 0,  
    "dano": 15*2,    
    "mochila": Inventario
}
if carregar == "0":
    arquivocarregar = input("Digite o nome do arquivo json para carrega-lo (como .json)").strip()
    with open(arquivocarregar,"r") as f:
        try:
            Jogador = json.load(f)
        except FileNotFoundError:
            print("Save não encontrado")
        except Exception as e:
            print("houve um erro {e}")

    
def verificar_peso(item): 
    global pode_colocar_item
    if Jogador["Peso"] + item["peso"] <= 50:
        print("O jogador Pode colocar item")
        pode_colocar_item = True
    if Jogador["Peso"] + item["peso"] > 50:
        print("O jogador não pode colocar mais nada no inventario")
        pode_colocar_item = False

def exibir_status_jogador():
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
        print("O Item esta no seu Inventario e equipado")
    elif pode_colocar_item == False:
        print("O item não foi adicionado ao seu inventario ")    

def escolha_atacar():
    print("Para escolhar qual irá atacar, digite:\n1-) Atacar Goblin\n2-)Atacar Orc\n3-) Atacar Golem")
    escolhad_ataque = input("Eai, Vai escolher qual?").strip().lower()
    if escolhad_ataque == "1":
        Inimigo = Goblin["nome"]
        vida = Goblin["vida"]
        dano = Goblin["dano"]            
        defesa = Goblin["defesa"]
    elif escolhad_ataque == "2":
        Inimigo = Orc["nome"]
        vida = Orc["vida"]
        dano = Orc["dano"]            
        defesa = Orc["defesa"]
    elif escolhad_ataque == "3":
        Inimigo = Golem["nome"]
        vida = Golem["vida"]
        dano = Golem["dano"]            
        defesa = Golem["defesa"]
   
    while Jogador["vida"] > 0 and vida > 0:
        

        dano_no_monstro = Jogador["dano"] - defesa
        if dano_no_monstro < 1: 
            dano_no_monstro = 1
            
        vida -= dano_no_monstro  
        print(f"Você atacou o {Inimigo} e causou {dano_no_monstro} de dano!")
        print(f"Vida restante do {Inimigo}: {vida}")
        print("-----------------------------------")
        
       
        if vida <= 0:
            print(f"O {Inimigo} morreu! Vitória!")
            break
            
      
        dano_no_jogador = dano - Jogador["defesa"]
        if dano_no_jogador < 1:  
            dano_no_jogador = 1
            
        Jogador["vida"] -= dano_no_jogador  
        print(f"O {Inimigo} te atacou e causou {dano_no_jogador} de dano!")
        print(f"Sua vida restante: {Jogador['vida']}")
        print("===================================\n")

        if Jogador["vida"] <= 0:
            print("É... ASSIM QUE TU MORREU! F no chat.")
            break
    
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
        
            confirmar = input(f"Quer descartar o item {c} Digite 's' se sim\n").strip().lower()
            if confirmar == "s":
                Jogador["Peso"] -= c["peso"]
                Jogador["mochila"].remove(c)
                print(f"O Item {c} foi Descartado")
                break
            else: 
                print("Nada foi descartado")


while Jogador["vida"] > 0:

    print("\n\n\n")
    print("Para escolher você pode\n")
    print("1-)Atacar o Goblin Orc ou Golem\n") 
    print("2-)Olhar seu Inventario\n")
    print("3-)Procurar Itens\n") 
    print("4-)Salvar O jogo é sair\n") 
    print("5-)Sair sem salvar\n")
    print("6-)Mostrar estatisticas\n")#
    print("7-)Usar algum consumível de seu inventario\n")
    print("8-)Retirar item do inventario (descarta-lo)\n")
    

    opção = input("Eai, qual opção vai ser a escolhida da vez?\nObs: digite só o número").strip()

    if opção == "1":
        print("Para escolhar qual irá atacar, digite:\n1-) Atacar Goblin\n2-)Atacar Orc\n3-) Atacar Golem")
        escolha_ataque = input("Eai, Vai escolher qual?")
        if escolha_ataque == "1":
            escolha_atacar()

    elif opção == "2":
        print(f"Seu Inventario é {Jogador["mochila"]}")
    
    elif opção == "3":
        procurar_itens()

    elif opção == "4": 
        arquivo = input("Digite o nome do arquivo que vai querer salvar, com extensão .json no final")
        with open(arquivo,"w") as f:
            json.dump(Jogador,f,indent=4)
        print("Tchau, até a proxíma")
        break

    elif opção == "5":
        print("Tchau,ate a proxíma")
        break

    elif opção == "6":
        exibir_status_jogador()
    
    elif opção == "7":
        usar_consumivel()
    elif opção == "8":
        descartar()



    
            
