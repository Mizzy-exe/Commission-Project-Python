import config

print('*' * 40)
print('BEM-VINDO AO SISTEMA DE COMISSÕES')
print('*' * 40)

dados = config.config_artista()
config.salvar_config(dados)
config.carregar_config()

while True:
    opcao = config.tabela_esc()
    config.extra_comm(opcao)
    
    continuar = input('Deseja registrar outra comissão? [S/N]: ').strip().capitalize()

    if continuar != 'S':
        print('Encerrando o sistema de comissões... Até logo!')
        break
