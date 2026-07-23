import json

def salvar_config(dados):                                   # Salva em Json
      with open('config.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


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