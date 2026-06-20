#IMPORTS
import random
import time
import json
from itens import itens_jogo, Itens_achaveis
from database import Goblin, Orc, Golem

print("Olá jogador, nesse maravilhoso mundo você, é o dono da historia, mas antes me diga algumas informações")
Peso_Max = 50     # VERIFICAR SE PASSOU DOS 50KG,
pode_colocar_item = True
idade = int(input("Me informe sua Idade por favor:\n"))
nome = input("Qual o seu nome?\n")
carregar = input("Se você tiver um save e quiser carrega-lo digite 0, se não aperte enter.").strip()

print("Você ganhou uma espada de cobre, uma mochila é uma armadura")
print("Mas infelizmente você so aguenta carregar 50Kg no total e sua vida é 100, sua defesa inicial e 5, para aumenta-la presica de uma armadura")
print("A defesa diminui o Dano tomado em número, por exemplo com 5 de defesa em vez de levar 10 de ataque, levaria 5")
#Função de Inventário: Adicionar item checando peso (< 50Kg) e usar item de cura.
#Loop de Combate: Criar um 'while' (enquanto vida de ambos > 0) com menu de ações.
#IA dos Monstros: Criar regras condicionais ( Orc cura, Grakos carrega ataque).
#Save/Load: Funções com o módulo 'json' para salvar e carregar o progresso num arquivo. FEITO SAVE
Inventario = []
Jogador = {
    "nome" : nome,
    "idade": idade,
    "vida" : 100,
    "defesa": 5,
    "Peso" : 20,
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
    if Jogador["Peso"] + item <= 50:
        print("O jogador Pode colocar item")
        pode_colocar_item = True
    if Jogador["Peso"] + item > 50:
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
    print(f"Se você digitar itens você pode achar algum item como esses {Itens_achaveis} no chão")
    lista_sorteada = random.choice(Itens_achaveis)
    item_final = random.choice(lista_sorteada)
    verificar_peso(item_final)
    if pode_colocar_item == True:
        Inventario.append(item_final)

def escolha_atacar():
    print("Para escolhar qual irá atacar, digite:\n1-) Atacar Goblin\n2-)Atacar Orc\n3-) Atacar Golem")
    escolhad_ataque = input("Eai, Vai escolher qual?")
    if escolhad_ataque == "1":
        Inimigo = Goblin["nome"]
        vida = Goblin["vida"]
        dano = Goblin["dano"]            
        defesa = Goblin["defesa"]


#LOOP WHILE DO JOGO
while Jogador["vida"] > 0:
    print("Para escolher você pode\n")
    print("1-)Atacar o Goblin Orc ou Golem\n")
    print("2-)Olhar seu Inventario\n")#PRONTO
    print("3-)Procurar Itens\n")
    print("4-)Salvar O jogo é sair\n") #PRONTO
    print("5-)Sair sem salvar\n")#PRONTO
    print("6-)Mostrar estatisticas\n")#PRONTO
    
    opção = input("Eai, qual opção vai ser a escolhida da vez?\nObs: digite só o número").strip()

    if opção == "1":
        print("Para escolhar qual irá atacar, digite:\n1-) Atacar Goblin\n2-)Atacar Orc\n3-) Atacar Golem")
        escolha_ataque = input("Eai, Vai escolher qual?")
        if escolha_ataque == "1":
            escolha_atacar()

    elif opção == "2":
        print(f"Seu Inventario é {Jogador["mochila"]}")

    if opção == "4": #PRONTRO
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



    
            
