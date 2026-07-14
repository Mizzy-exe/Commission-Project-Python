import json

def opcao_commBR():
    comm = [{'tipo': 'Sketch', 'tamanho': 'Busto', 'brl': 15.00}, {'tipo': 'Sketch', 'tamanho': 'Half body', 'brl': 35.00}, 
    {'tipo': 'Sketch', 'tamanho': 'Full body', 'brl': 60.00}, {'tipo': 'Flat color', 'tamanho': 'Busto', 'brl': 30.00},
    {'tipo': 'Flat color', 'tamanho': 'Half body', 'brl': 50.00}, {'tipo': 'Flat color', 'tamanho': 'Full body', 'brl': 75.00},
    {'tipo': 'Full render', 'tamanho': 'Busto', 'brl': 50.00}, {'tipo': 'Full render', 'tamanho': 'Half body', 'brl': 80.00},
    {'tipo': 'Full render', 'tamanho': 'Full body', 'brl': 120.00}]


def config_artista():
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

    dados_artista['nome'] = nome
    dados_artista['nome_artistico'] = nome_artistico

    return dados_artista


def salvar_config(dados_artista):
      with open('config.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_artista, arquivo, indent=4, ensure_ascii=False)

def carregar_config():
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