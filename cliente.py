import json
import os
from time import sleep
import arquivo

def add_cliente():
    if os.path.exists('clientes.json'):                                 # checa se o arquivo clientes.json existe
        with open('clientes.json', 'r', encoding='utf-8') as arquivo:
            clientes = json.load(arquivo)
        print(f'--- Arquivo encontrado! {len(clientes)} clientes carregados. ---')
    else:
        clientes = {}
        print('--- Nenhum arquivo encontrado. Criando nova lista. ---')

    while True:                                                         #loop para adicionar clientes
        print()
        print('\n--- ADICIONAR NOVO CLIENTE ---')
        nome = input('Nome do cliente (ou "sair"): ').capitalize().strip()

        if nome.lower() == 'sair':
            break

        sexo = input('Sexo (F/M): ').capitalize().strip()
        if sexo not in 'FM':
            sexo = input('Tente novamente. Sexo (F/M): ').capitalize().strip()

        idade = int(input('idade: '))
        if idade < 18:
            print('Por favor, informe o número do seu responsável.')

        celular = input('Numero de celular: ')
        email = input('Email: ').capitalize().strip()
        cidade = input('Cidade: ').capitalize().strip()
        
        clientes[nome] = {
            'sexo': sexo,
            'idade': idade,
            'celular': celular,
            'email': email,
            'cidade': cidade,   
        }

        with open('clientes.json', 'w', encoding='utf-8') as arquivo:                  # faz a atualização do arquivo clientes.json com os novos dados
                json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

        print('\nArquivo atualizado com sucesso!')
        print()
        print('--- Cliente adicionado ---')
        print(f'Agora temos {len(clientes)} clientes cadastrados.')
        return clientes
        

def listar_clientes(clientes):                              # lista todos os clientes cadastrados no arquivo clientes.json
    print('\n--- LISTA DE CLIENTES ---')

    dicionario = arquivo.json_simples(clientes)

    for nome, info in dicionario.items():
        print(f'Nome: {nome}')
        print(f'Sexo: {info["sexo"]}')
        print(f'Idade: {info["idade"]}')
        print(f'Celular: {info["celular"]}')
        print(f'Email: {info["email"]}')
        print(f'Cidade: {info["cidade"]}')
        print('-' * 30)

