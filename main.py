import json
import os
import config
import arquivo
import comissao
import cliente
from time import sleep
import menu

print('-' * 40)
print(f'{"BEM-VINDO AO SISTEMA DE COMISSÕES":^40}')
print('-' * 40)

if os.path.exists('config.json'):
    with open('config.json', 'r', encoding='utf-8') as arquivo:
        artista = json.load(arquivo)
    print(f'Arquivo encontrado! Bem vindo(a) {artista['nome_artistico']}')
else:
    print('Nada foi encontrado. Criando um novo arquivo...')
    sleep(1)
    artista = config.config_artista()
    arquivo.salvar_config(artista)
    arquivo.exibir_json(artista)

print()
print(f'            ---{artista['nome_artistico']}---'.upper())

menu.menu_principal()




# while True:
#     opcao = config.tabela_esc()
#     registro = comissao.extra(opcao)

#     print(f'Comissão registrada em {registro}')
#     print()
    
#     continuar = input('Deseja registrar outra comissão? [S/N]: ').strip().capitalize()

#     if continuar != 'S':
#         print('Encerrando o sistema de comissões... Até logo!')
#         break
