from time import sleep
import config

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
        sleep(2)

    print()
    final = input('Essa comissão foi finalizada? [S/N]: ').upper().strip()
    print()

    if final =='S':
        registro = config.data_hora()
        return registro
    else:
        print('ainda em desenvolvimento a partir daqui!')
        return None
        