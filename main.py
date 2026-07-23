import config
import arquivo
import comissao

print('*' * 40)
print('BEM-VINDO AO SISTEMA DE COMISSÕES')
print('*' * 40)

dados = config.config_artista()
arquivo.salvar_config(dados)
arquivo.carregar_config()

while True:
    opcao = config.tabela_esc()
    registro = comissao.extra_comm(opcao)
    print(f'Comissão registrada em {registro}')
    print()
    
    continuar = input('Deseja registrar outra comissão? [S/N]: ').strip().capitalize()

    if continuar != 'S':
        print('Encerrando o sistema de comissões... Até logo!')
        break
