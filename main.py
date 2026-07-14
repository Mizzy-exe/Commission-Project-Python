import config

print('*' * 40)
print('BEM-VINDO AO SISTEMA DE COMISSÕES')
print('*' * 40)

dados = config.config_artista()
config.salvar_config(dados)
config.carregar_config()
