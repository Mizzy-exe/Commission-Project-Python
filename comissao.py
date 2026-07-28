from time import sleep
import config

def extra(opc):                                                  # Pergunta se o cliente quer mais alguma coisa na ilustração
    print('INFORMAÇÕES EXTRAS DA COMISSÃO')
    print('-' * 40)

    lista = ['Personagem', 'Fundo detalhado', 'Armas', 'Animal']
    extras ={}

    for c in lista:
        item = input(f'Deseja adicionar {c}? [S/N]: ').strip().upper()
        if item == 'S':
           q = int(input('Quantos: '))
           porcento = float(input('Qual porcentagem adicional? '))

           extras[c] = {
               'quant': q,
               'porcentagem': porcento
           }
        else:
            print(f'Tudo bem, sem {c}')

    calculo_extra(opc, extras)
    final = input('Essa comissão foi finalizada? [S/N]: ').upper().strip()
    print()

    if final =='S':
        registro = config.data_hora()
        return registro
    else:
        print('ainda em desenvolvimento a partir daqui!')
        return None


def calculo_extra(escolha, itm):                       #itm é item, eu so fiquei sem ideia para nome do parametro
    
    print()
    print('O cliente quis adicionar: ')
    soma = 0

    for nome_item, c in itm.items():                # Aqui uso o for para listar apenas o que foi escolhido com Sim
        print(f'{c['quant']} {nome_item}')

        calculo = escolha['brl'] * (c['porcentagem'] / 100)
        calculo *= c['quant']
        soma += calculo

    print()
    total = escolha['brl'] + soma
    print(f'O valor total da comissão é: R${total:.2f}')
