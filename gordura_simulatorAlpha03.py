# coding: utf8

from time import sleep

erroValor = 'Entrada inválida! Coloque apenas números.'
nome = str(input('Olá, eu sou seu personal trainer virtual, qual o seu nome?\n'))

print('Ok', nome + ', agora preciso saber seu peso e altura para saber se você está fora de forma')
# valores string:
while True:
    try:
        peso = int(input('Peso (em kg, apenas números):'))
        altura = int(input('Altura (em centímetros, apenas números):'))
        break
    except ValueError:
        print(erroValor)
altura_dec = altura / 100

def loadprint(msg, tempo, vel=0.1):
    i = 0
    while i <= tempo:
        load = ['|', '/', '─','\\']
        for n in range(4):
            sleep(vel)
            print('\r{} [{}]'.format(msg, load[n]), end='', flush=True)
        i += vel * len(load)
    print('')


def receita(msg, msg2, receita, tempo):
    for i, ing in enumerate(dt[receita]['ing']):
        if dt[ing] - dt[receita]['ing'][ing] == True:
            print(dt) #Testa se tem o suficiente de um item...
            if i+1 == len(dt[receita]['ing']): # e depois se já é o ultimo item
                for _ in range(4):
                    print('\rVocê começou a', msg, end=_*'.', flush=True)
                    sleep(1)
                print('')
                for i in dt[receita]['ing']: #Subtrai os items
                    dt[i] -= dt[receita]['ing'][i]
                    sleep(tempo / len(dt[receita]['ing']))
                    print(i.capitalize()+'...')
                print('Você', msg2)
                dt[receita][receita] += 1
        else:
            print(f'Você não tem o suficiente de <{ing}>') #...Caso não tenha termina o processo
            break


def personal():
    imc = round(peso / altura_dec ** 2, 2)
    print('\nSeu IMC:', imc)
    if imc < 17:
        print('Você está muito abaixo do peso, engorde!\n')
    elif imc < 1849 / 100:
        print('Você está abaixo do peso, coma mais\n')
    elif imc < 2499 / 100:
        print('Peso normal, muito bem, continue assim!\n')
    elif imc < 2999 / 100:
        print('Acima do Peso, eu estou vendo esse bolo de banana que você está fazendo\n')
    elif imc < 3499 / 100:
        print('Obesidade, vá praticar alguns exercícios!\n')
    elif imc < 3999 / 100:
        print('Obesidade severa, muito gordo, pare de comer bolo de banana e vá praticar exercício\n')
    else:
        print('Obesidade mórbida, procure ajuda!!!\n')

personal()

# INICIO DO GAME GORDURA SIMULATOR

# BANCO DE DADOS
dt = {
    'dinheiro': 5,
    'cansaço': 0,
    'stress': 0,
    'ovo': 0,
    'leite': 500,
    'banana': 500,
    'trigo': 500,
    'margarina': 500, # <- Uma colher = 0.08
    'açúcar': 500,
    'fermento': 500,
    'óleo': 500,
    'sal': 0,
    'bolo': {
        'bolo': 0, #unidades
        'ing': {'banana': 3, 'ovo': 3, 'trigo': 0.2, 'leite': 0.2, 'margarina': 0.24, 'açúcar': 0.15, 'fermento': 0.10}
    },   #└> ingredientes
    'pão': {
        'pão': 0,
        'ing': {'trigo': 1, 'açúcar': 0.05, 'óleo': 0.1, 'sal': 0.01, 'fermento': 0.15}
    },
    'ovoFrito': {
        'ovoFrito': 0,
        'ing': {'ovo': 1, 'óleo': 0.15, 'sal': 0.1}
    },
    'panqueca': {
        'panqueca': 0,
        'ing': {'ovo': 3, 'leite': 0.25, 'trigo': 0.2}
    },
}

# MERCADO
def mercado():
    while True:
        try:
            acao_mercado = int(input('\nVocê foi ao mercado com {dinheiro} reais no bolso'
                                    '\n1: Comprar algo'
                                    '\n2: Voltar pra casa'
                                    '\n'.format_map(dt)))

            if acao_mercado == 1:
                compras()
            elif acao_mercado == 2:
                return
            else:
                print('Comando desconhecido!')
        except ValueError:
                print(erroValor)
        sleep(1)

def compras():
    while True:
        try:
            acao_compra = int(input('\nVocê foi ver o que tem para comprar'
                                    '\nVai comprar o quê?'
                                    '\n1: Ovo R$2 (Tem {ovo})'
                                    '\n2: Leite R$3 (Tem {leite})'
                                    '\n3: Banana R$1 (Tem {banana})'
                                    '\n4: Trigo 1kg R$3 (Tem {trigo})'
                                    '\n5: Margarina R$5 (Tem {margarina})'
                                    '\n6: Açúcar 1kg R$3 (Tem {açúcar})'
                                    '\n7: Sal 500g R$2 (Tem {sal})'
                                    '\n8: Fermento R$3 (Tem {fermento})'
                                    '\n9: Óleo R$3 (Tem {óleo})'
                                    '\n10: Sair do mercado\n'.format_map(dt)))
            if acao_compra == 1 and dt['dinheiro'] >= 2:
                dt['dinheiro'] -= 2
                print('Você comprou um ovo por 2 reais')
                dt['ovo'] += 1

            elif acao_compra == 2 and dt['dinheiro'] >= 3:
                dt['dinheiro'] -= 3
                print('Você comprou um leite por 3 reais')
                dt['leite'] += 1

            elif acao_compra == 3 and dt['dinheiro'] >= 1:
                dt['dinheiro'] -= 1
                print('Você comprou uma banana por 1 real')
                dt['banana'] += 1

            elif acao_compra == 4 and dt['dinheiro'] >= 3:
                dt['dinheiro'] -= 3
                print('Você comprou um pacote de trigo por 3 reais')
                dt['trigo'] += 1

            elif acao_compra == 5 and dt['dinheiro'] >= 5:
                dt['dinheiro'] -= 5
                print('Você comprou uma margarina por 5 reais')
                dt['margarina'] += 1

            elif acao_compra == 6 and dt['dinheiro'] >= 3:
                dt['dinheiro'] -= 3
                print('Você comprou um pacote de açúcar por 3 reais')
                dt['açúcar'] += 1

            elif acao_compra == 7 and dt['dinheiro'] >= 2:
                dt['dinheiro'] -= 2
                print('Você comprou um sal 500g por 2 reais')
                dt['sal'] += 1

            elif acao_compra == 8 and dt['dinheiro'] >= 3:
                dt['dinheiro'] -= 3
                print ('Você comprou um potinho de fermento por 3 reais')
                dt['fermento'] += 1

            elif acao_compra == 9 and dt['dinheiro'] >= 3:
                dt['dinheiro'] -= 3
                print('Você comprou um óleo por 3 reais')
                dt['óleo'] += 1
            
            elif acao_compra == 10:
                return
            else:
                print('Você não tem dinheiro para comprar isso ou o comando é desconhecido!')
        except ValueError:
            print(erroValor)
        sleep(1)
        # FIM DAS COMPRAS NO MERCADO


# PRATICAR EXERCICIOS:
def exercicios():
    global peso
    loadprint('Você foi praticar exercícios', 5)
    print('Você perdeu 0,5 kg, mas ficou cansado. Descanse um pouco\n')
    dt['cansaço'] += 2
    if dt['stress']:
        dt['stress'] -= 1
    peso -= 0.5
    sleep(3)

# TRABALHAR:
def trabalho():
    for i in range(4):
        print('\rVocê foi trabalhar', end=i*'.', flush=True)
        sleep(1)
    for i in range(4):
        print('Trabalhando', end=i*'.', flush=True)
        sleep(1)
    print('Você terminou seu trabalho e ganhou 10 reais\n')
    dt['dinheiro'] += 10
    if dt['cansaço']:
        dt['cansaço'] -= 1
    dt['stress'] += 1
    sleep(3)

# COZINHA
def cozinha():
    while True:
        try:
            cozinha = int(input('\nVocê está na cozinha'
                                '\n1: Comer/beber algo'
                                '\n2: Fazer alguma receita'
                                '\n3: Sair da cozinha\n'))
            if cozinha == 1:
                cozinha_comer()
            elif cozinha == 2:
                cozinha_receita()
            elif cozinha == 3:
                return
            else:
                print('Comando desconhecido, não tem easter egg!!')
        except ValueError:
            print(erroValor)
        sleep(1)

def cozinha_comer():
    global peso
    while True:
        try:
            acao_cozinha = int(input('\nVocê foi comer algo'
                                     '\nComer/beber o que?'
                                     '\n1: Ovo (Tem {ovo})'
                                     '\n2: Leite (Tem {leite})'
                                     '\n3: Banana (Tem {banana})'
                                     '\n4: Trigo 1kg (Tem {trigo})'
                                     '\n5: Margarina (Tem {margarina})'
                                     '\n6: Açúcar (Tem {açúcar})'
                                     '\n7: Comer uma fatia de bolo (Tem {bolo})'
                                     '\n8: Comer uma fatia de pão (Tem {pão})'
                                     '\n9: Comer um ovo frito (Tem {ovoFrito})'
                                     '\n10: Comer uma panqueca (Tem {panqueca})'
                                     '\n11: Voltar\n'.format_map(dt)))

            if acao_cozinha == 2 and dt['leite'] >= 0.25:
                print('Você bebeu um pouco de leite e engordou 0.10kg')
                dt['leite'] -= 0.25
                peso += 0.10

            elif acao_cozinha == 3 and dt['banana'] >= 1:
                print('Você comeu uma banana e engordou 0.20kg')
                dt['banana'] -= 1
                peso += 0.20

            elif acao_cozinha == 7 and dt['bolo'] >= 0.1:
                print('Você comeu uma fatia de bolo')
                dt['bolo'] -= 0.1
                peso += 0.50

            elif acao_cozinha == 8 and dt['pão'] >= 0.05:
                print ('Você comeu uma fatia de pão')
                dt['pão'] = round(dt['pão'] - 0.05, 2)
                peso = round(peso + 0.10, 2)

            elif acao_cozinha == 9 and dt['ovoFrito'] >= 1:
                print ('Você comeu um ovo frito')
                dt['ovoFrito'] -= 1
                peso = round(peso + 0.10, 2)

            elif acao_cozinha == 10 and dt['panqueca'] >= 1:
                print ('Você comeu uma panqueca')
                dt['panqueca'] -= 1
                peso = round(peso + 0.20, 2)

            elif acao_cozinha == 11:
                return
            else:
                print('Você não pode comer isso, você não tem essa comida ou o comando é desconhecido')
        except ValueError:
            print(erroValor)
        sleep(1)

def cozinha_receita():
    while True:
        #global banana, ovo, trigo, leite, margarina, açúcar, fermento, óleo, sal, bolo, pão, ovo_frito, panqueca
        try:
            cozinha_receita = int(input('\nVocê pensou em fazer uma receita...'
                                        '\nFazer o quê?'
                                        '\n1: Bolo de banana (3 bananas, 3 ovos, 2 xícaras de trigo 200g, 1 copo de leite 200ml, 3 colheres de margarina, 1.5 xícara de açúcar 150g, 1 colher (chá) de fermento)'
                                        '\n2: Pão (1 kg de trigo, 1/2 xícara de açúcar 50g, 1/2 xícara de óleo 100ml, 1/2 colher de sopa de sal, 2 copos de água, 15g de fermento)'
                                        '\n3: Ovo frito (1 ovo, 1 colher de sopa óleo 15ml,  1/2 colher de sopa de sal)'
                                        '\n4: Panqueca (2 xícaras de trigo 200g, 2 copos de leite 250ml, 3 ovos)\n'
                                        '\n5: Voltar\n'))
            
            if cozinha_receita == 1:
                receita('fazer um bolo de banana', 'fez um bolo de banana', 'bolo', 6)

            elif cozinha_receita == 2:
                receita('fazer um pão', 'fez um pão', 'pão', 6)

            elif cozinha_receita == 3:
                receita('fritar um ovo', 'fritou um ovo', 'ovoFrito', 2)

            elif cozinha_receita == 4:
                receita('fazer uma panqueca', 'fez uma panqueca', 'panqueca', 2)

            elif cozinha_receita == 5:
                return
            else:
                print('Você não tem ingredientes ou o comando é desconhecido')
            print(dt)
        except ValueError:
            print(erroValor)
        sleep(1)
cozinha_receita()
# CASA

def main():
    while True:
        try:
            acao = int(input('\nVocê está em casa. Escolha o que fazer:         |ESTATÍSTICAS '
                             '\n1: Ir ao mercado                                |PESO:' + str(peso) + 'kg'
                             '\n2: Dispensar o personal trainer e terminar      |CANSAÇO:' + str(cansaço) +
                             '\n3: Praticar exercícios                          |DINHEIRO:' + str(dinheiro) +
                             '\n4: Ir ao trabalho                               |STRESS:' + str(stress) +
                             '\n5: Consultar o personal trainer virtual'
                             '\n6: Ir à cozinha\n'))
            if acao == 1:
                mercado()
            elif acao == 2:
                print('Você dispensou o personal trainer e terminou o jogo')
                break
            elif acao == 3:
                exercicios()
            elif acao == 4:
                trabalho()
            elif acao == 5:
                personal()
            elif acao == 6:
                cozinha()
            else:
                print('')
        except ValueError:
            print(erroValor)
        if stress >= 10:
            print('\nVocê morreu de stress')
            break
        elif peso >= 250:
            print('\nVocê ficou muito gordo e morreu')
            break
        elif cansaço >= 20:
            print('\nEm sua compulsividade por ficar magro, se exercitou tanto que morreu de cansaço!')
            break
        elif peso <= 10:
            print('\nMorreu com fome. Será que estava fingindo ser uma criança africana? Faça uma doação e contribua com o fim da fome na África!')
            break
        sleep(1)
    sleep(10)

main()
