import json
from time import sleep

def opcao_commBR():                         # Opções de tamanho, pintura e tipo de arte
    comm = [{'tipo': 'Sketch', 'tamanho': 'Busto', 'brl': 15.00}, {'tipo': 'Sketch', 'tamanho': 'Half body', 'brl': 35.00}, 
    {'tipo': 'Sketch', 'tamanho': 'Full body', 'brl': 60.00}, {'tipo': 'Flat color', 'tamanho': 'Busto', 'brl': 30.00},
    {'tipo': 'Flat color', 'tamanho': 'Half body', 'brl': 50.00}, {'tipo': 'Flat color', 'tamanho': 'Full body', 'brl': 75.00},
    {'tipo': 'Full render', 'tamanho': 'Busto', 'brl': 50.00}, {'tipo': 'Full render', 'tamanho': 'Half body', 'brl': 80.00},
    {'tipo': 'Full render', 'tamanho': 'Full body', 'brl': 120.00}]
    return comm

def config_artista():                            # Pego nome real e artístico do usuario e coloco em um dicionário
    dados_artista = {}
    nome = input('>>>> Qual é seu nome? ').strip().capitalize()
    print(f'Olá, é um prazer te ter aqui {nome}.')
    print()

    resposta = input('>>>> Você tem nome artístico? [S/N] ').strip().capitalize()
    if resposta == 'S':
        print()
        nome_artistico = input('>>>> Qual é seu nome artístico? ').strip().capitalize()
        print(f'Perfeito. Vamos continuar com seu nome artístico: {nome_artistico}')
    else:
        print('Tudo bem. Então vamos continuar com seu nome real.')
        nome_artistico = nome

    dados_artista['nome'] = nome
    dados_artista['nome_artistico'] = nome_artistico

    return dados_artista


def salvar_config(dados_artista):                                   # Salva o dicionário com os dados do artista
      with open('config.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_artista, arquivo, indent=4, ensure_ascii=False)


def carregar_config():                                                  # Mostra o que está salvo no dicionário
    try:
        with open('config.json', 'r', encoding='utf-8') as arquivo:
            dados_artista = json.load(arquivo)
            print()

            print(f"Configuração carregada com sucesso!")
            print(f"Nome: {dados_artista['nome']}\nNome Artístico: {dados_artista['nome_artistico']}")
            return dados_artista
    except FileNotFoundError:
        print('Arquivo de configuração não encontrado. Por favor, configure o artista primeiro.')
        return None
    

def extra_comm(opc):                                                  # Pergunta se o cliente quer mais algum personagem
    print('INFORMAÇÕES EXTRAS DA COMISSÃO')
    print('-' * 40)
    personagem = input('Quer adicionar personagens? [S/N] ').strip().capitalize()

    if personagem =='S':
        quantidade = int(input('Quantos? '))
        preco_principal = opc['brl']
        total_extras = quantidade * (preco_principal * 0.60)
        preco_total = preco_principal + total_extras
        print(f'O valor total com +{quantidade} personagens é: R${preco_total:.2f}')
    else:
        print('Entendido. Sem personagens extras.')
        print('>>>> Fim do planejamento dessa comissão <<<<') 
        print('-' * 40)
        sleep(2)
        


def inicio_turno():                                                              # Começa o programa em loop
    escolha = input('Iniciar? [S/N] (N vai parar) ').strip().capitalize()
    print('-' * 40)
    while True:
        if escolha == 'N':
            print('Okay. Encerrando...')
            sleep(2)
            break
        else:
            if escolha == 'S':
                cliente = input('Nome do cliente: ').strip().capitalize()
                print(f'Veja qual opção o(a) {cliente} quer: ')
                print()
        return cliente


def tabela_esc(): 
    client = inicio_turno() 
    commission = opcao_commBR()  
    
    # Mostra a tabela de opções toda organizada
    while True:
        print(f'{'PINTURA':<24} {'TAMANHO':<23} {'VALOR'}')
        print()

        for i, c in enumerate(commission, start=1):                                          #tabela
            print(f'{i} - {c['tipo']:<20} {c['tamanho']:<23} {c['brl']:.2f}') 
        print() 

        esc_comm = int(input('Digite aqui: '))                           #decisao

        if 1 <= esc_comm <= len(commission):
            opcao_escolhida = commission[esc_comm - 1]
            print(f'O(a) {client} escolheu {opcao_escolhida['tamanho']}, {opcao_escolhida['tipo']} por R${opcao_escolhida['brl']:.2f}')

            confirm = input('Tem certeza: [S/N] ').strip().capitalize()

            if confirm == 'S':
                print('Confirmado.')
                print()
                return opcao_escolhida
            else:
                print('Então tente novamente.')
                print()
        else:
            print('Opção invalida! Tente novamente.')   
            print() 
