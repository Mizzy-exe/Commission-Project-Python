import json
import os

def add_cliente():
    if os.path.exists('clientes.json'):
        with open('clientes.json', 'r', encoding='utf-8') as arquivo:
            clientes = json.load(arquivo)
        print(f'--- Arquivo encontrado! {len(clientes)} clientes carregados. ---')
    else:
        clientes = {}
        print('--- Nenhum arquivo encontrado. Criando nova lista. ---')

    while True:
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

        with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

        print('\nArquivo atualizado com sucesso!')
