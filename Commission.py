from time import sleep
comm = [{'tipo': 'Sketch', 'tamanho': 'Busto', 'brl': 15.00, 'usd': 5.00}, {'tipo': 'Sketch', 'tamanho': 'Half body', 'brl': 35.00, 'usd': 10.00}, 
{'tipo': 'Sketch', 'tamanho': 'Full body', 'brl': 60.00, 'usd': 15.00}, {'tipo': 'Flat color', 'tamanho': 'Busto', 'brl': 30.00, 'usd': 10.00},
{'tipo': 'Flat color', 'tamanho': 'Half body', 'brl': 50.00, 'usd': 15.00}, {'tipo': 'Flat color', 'tamanho': 'Full body', 'brl': 75.00, 'usd': 30.00},
{'tipo': 'Full render', 'tamanho': 'Busto', 'brl': 50.00, 'usd': 15}, {'tipo': 'Full render', 'tamanho': 'Half body', 'brl': 80.00, 'usd': 25.00},
 {'tipo': 'Full render', 'tamanho': 'Full body', 'brl': 120.00, 'usd': 45.00}]
print(f'{'ART COMMISSIONS':^40}')
print('*' *  40)
escolha = input('Iniciar turno? [S/N] (P para parar) ').strip().capitalize()
print('-' * 40)
while True:
    if escolha in 'NP':
        print('Okay. Encerrando...')
        sleep(2)
        break
    else:
        if escolha == 'S':
            cliente = input('Nome do cliente: ').strip().capitalize()
            nacionalidade = input(f'O {cliente} é do brasil ou não? [S/N] ').strip().capitalize()
            if nacionalidade == 'S':
                print('>>>> Okay. É brasileiro(a)')
                print(f'Veja qual opção o(a) {cliente} quer: ')
                print()
                while True:
                    print(f'{'PINTURA':<24} {'TAMANHO':<20} {'VALOR BRL'}')
                    print()
                    for i, c in enumerate(comm, start=1):                                          #tabela
                        print(f'{i} - {c['tipo']:<20} {c['tamanho']:<23} {c['brl']:.2f}') 
                    print() 
                    esc_comm = int(input('Digite aqui: '))                           #decisao
                    if 1 <= esc_comm <=9:
                        opcao_escolhida = comm[esc_comm - 1]
                        print(f'O(a) {cliente} escolheu {opcao_escolhida['tamanho']}, {opcao_escolhida['tipo']} por R${opcao_escolhida['brl']:.2f}')
                        confirm = input('Tem certeza: [S/N] ').strip().capitalize()
                        if confirm == 'S':
                            print('Confirmado.')
                            print()
                            break
                        else:
                            print('Então tente novamente.')
                            print()
                print('INFORMAÇÕES EXTRAS DA COMISSÃO')
                print('-' * 40)
                personagem = input('Quer adicionar personagens? [S/N] ').strip().capitalize()
                if personagem =='S':
                    quantidade = int(input('Quantos? '))
                    preco_principal = opcao_escolhida['brl']
                    total_extras = quantidade * (preco_principal * 0.60)
                    preco_total = preco_principal + total_extras
                    print(f'O valor total com +{quantidade} personagens é: R${preco_total:.2f}')
                else:
                    print('Entendido. Sem personagens extras.')
                    print('>>>> Fim do planejamento dessa comissão <<<<') 
                    print('-' * 40)
                sleep(2)
            else:
                if nacionalidade == 'N':
                    print('>>>> Okay. É gringo(a)')
                    print(f'Veja qual opção o(a) {cliente} quer: ')
                    print()
                    while True:
                        print(f'{'PINTURA':<24} {'TAMANHO':<20} {'VALOR USD'}')
                        print()
                        for i, c in enumerate(comm, start=1):                                          #tabela
                            print(f'{i} - {c['tipo']:<20} {c['tamanho']:<23} {c['usd']:.2f}') 
                        print() 
                        esc_comm = int(input('Digite aqui: '))                           #decisao
                        if 1 <= esc_comm <=9:
                            opcao_escolhida = comm[esc_comm - 1]
                            print(f'O(a) {cliente} escolheu {opcao_escolhida['tamanho']} {opcao_escolhida['tipo']} por ${opcao_escolhida['usd']:.2f}')
                            confirm = input('Tem certeza: [S/N] ').strip().capitalize()
                            if confirm == 'S':
                                print('Confirmado.')
                                print()
                                break
                            else:
                                print('Então tente novamente.')
                                print()
                    print('INFORMAÇÕES EXTRAS DA COMISSÃO')
                    print('-' * 40)
                    personagem = input('Quer adicionar personagens? [S/N] ').strip().capitalize()
                    if personagem =='S':
                        quantidade = int(input('Quantos? '))
                        preco_principal = opcao_escolhida['usd']
                        total_extras = quantidade * (preco_principal * 0.60)
                        preco_total = preco_principal + total_extras
                        print(f'O valor total com +{quantidade} personagens é: R${preco_total:.2f}')
                    else:
                        print('Entendido. Sem personagens extras.')
                        print('>>>> Fim do planejamento dessa comissão <<<<') 
                        print('-' * 40)
    sleep(2)
    if escolha not in 'SN':
        print('Erro. Tente novamente.')
        escolha = input('Iniciar turno? [S/N] (P para parar) ').strip().capitalize()
