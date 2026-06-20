#IMPORTS
import random
import time
import json
from itens import itens_jogo
import database
print(itens_jogo)
print("Olá jogador, nesse maravilhoso mundo você, é o dono da historia, mas antes me diga algumas informações")
Peso_Max = 50    
idade = int(input("Me informe sua Idade por favor:\n"))
nome = input("Qual o seu nome?\n")
print("Você ganhou uma espada de cobre, uma mochila é uma armadura")
print("Mas infelizmente você so aguenta carregar 50Kg no total e sua vida é 100, sua defesa inicial e 5, para aumenta-la presica de uma armadura")
print("A defesa diminui o Dano tomado em número, por exemplo com 5 de defesa em vez de levar 10 de ataque, levaria 5")
Jogador = {
    "nome" : nome,
    "idade": idade,
    "vida" : 100,
    "defesa": 5,
    "Peso" : 20,
    "dano": 15,
}
Inventario = []


