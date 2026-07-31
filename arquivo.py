import json
import cliente

def salvar_config(dados):                                   # Salva em Json
      with open('config.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def exibir_json(arqui):                                                  # Mostra o que está salvo no dict
    try:
        with open('arqui', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print()

        print("-------------------------------------")
        print(f'EXIBINDO ARQUIVO: {'arqui'}')
        print("-------------------------------------")

        if not dados:                   # Se o arquivo estiver vazio
            print('O arquivo está vazio.')
            return dados
                                        
        for chave, info in dados.items():                 #loop para ler cada item principal
            print(f'\n🔹 {chave}:'.upper())

            if isinstance(info, dict):                  #se as informações internas forem outro dict
                for sub_chave, valor in info.items():
                    print(f'  - {sub_chave}: {valor}'.capitalize())

        print('\n' + '-'*40)
        return dados
            
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        return None
    except json.JSONDecodeError:
        print('[ERRO]: O arquivo não é um JSON válido ou está corrompido.')
        return None
    