# Pegando as bibliotecas
import os
import requests

######################################################
# Corpo das funções a serem utilizadas 

os.system('cls' if os.name == 'nt' else 'clear')

##################

def solicitacao_de_conselhos(qtde):
    contar = 0
    dicio = {}  # Para armazenar os conselhos com seu id
    traco = '  ----------------------------  '

    while contar < qtde:
        pedido_url = "https://api.adviceslip.com/advice"
        resposta = requests.get(pedido_url)
        id = resposta.json()['slip']

        print('\n     ' + id['advice'] + traco + 'Id do Conselho ' + str(id['id']) + '\n')
        dicio[str(id['id'])] = id['advice']

        print("\n--- Você quer guardar este conselho? --- \n")
        s = input()

        if s.upper() == 'SIM':
            guardar_conselho(dicio.popitem())
        
        contar += 1

###################################################
def guardar_conselho(tupla):
    with open("teste_1.txt", 'a') as arq:
        arq.write(tupla[0] + ' ' + '--- ' + tupla[1] + '\n')

########

########################################
def resgatar_conselho(id):
    with open("teste_1.txt", 'r') as arq:
        for leitura in arq:
            if leitura.startswith(id + ' '):
                print(f"O conselho requerido é: {leitura[len(id) + 1:]}")
                print("                     ----------------- Este é um bom conselho :) -------------")
                return
        print("Conselho não encontrado.")

###########

######################################
# Início do programa em si

print("----- Bom dia! Seja bem-vindo à Cachaçaria do Seu Zé! ! -------- \n")
print("----- Depois de uma boa nada melhor do que querer buscar orientação na vida não é mesmo -----!? :) :)\n")
print("----- Diga quantos conselhos deseja -------\n ")

conselhos = int(input())

####################

# O arquivo é aberto em modo 'w' para ser limpo antes de usar
with open("teste_1.txt", 'w'):
    pass

####################

solicitacao_de_conselhos(conselhos)

###################

print("---- Você deseja resgatar algum conselho ------ ?\n")
s = input('\n')

if s.upper() == 'SIM':
    print("\nDigite o id \n")
    id = input()
    resgatar_conselho(str(id))
