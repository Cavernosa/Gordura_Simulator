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


def personal():
    try:
        imc = round(peso / altura_dec ** 2, 2)
    except ZeroDivisionError:
        frase = 'Você esætŋ< [object Object]]]]]'
        for i in range(len(frase)):
            print(frase[i], end='', flush=True)
            sleep(i ** 2 / 400)
        while True:
            print('00000000 Error', end=' ', flush=True)
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
    'stress': 0, #     0        1 x       2 0      2 1
    'comida': {  # [unidades, [custo], (consumo, gordura)]
        'ovo': [500, 2],
        'leite': [500, 3, (.25, .10)],
        'banana': [500, 1, (1, .20)],
        'trigo': [500, 3],
        'margarina': [500, 5], # <- Uma colher = 0.08
        'açúcar': [500, 3],
        'fermento': [500, 3],
        'óleo': [500, 3],
        'sal': [500, 2],
        'bolo': [0, [('banana', 3), ('ovo', 3), ('trigo', .2), ('leite', .2), ('margarina', .24), ('açúcar', .15), ('fermento', .10)], (.1, .50)],
        'pão': [0, [('trigo', 1), ('açúcar', .05), ('óleo', .1), ('sal', .01), ('fermento', .15)], (.05, .10)],
        'ovo frito': [0, [('ovo', 1), ('óleo', .15), ('sal', .1)], (1, .10)],
        'panqueca': [0, [('ovo', 3), ('leite', .25), ('trigo', .2)], (1, .20)]
    }
}

# MERCADO
def mercado():
    while True:
        try:
            acao = int(input('\nVocê foi ao mercado com {dinheiro} reais no bolso'
                                    '\n1: Comprar algo'
                                    '\n2: Voltar pra casa'
                                    '\n'.format_map(dt)))

            if acao == 1:
                compras()
            elif acao == 2:
                return
            else:
                print('Comando desconhecido!')
        except ValueError:
                print(erroValor)
        sleep(1)

def compras():
    while True:
        try:
            acao = input('\nVocê foi ver o que tem para comprar'
                         '\nVai comprar o quê?'
                         '\n1: Ovo R$2 (Tem {ovo[0]})'
                         '\n2: Leite R$3 (Tem {leite[0]})'
                         '\n3: Banana R$1 (Tem {banana[0]})'
                         '\n4: Trigo 1kg R$3 (Tem {trigo[0]})'
                         '\n5: Margarina R$5 (Tem {margarina[0]})'
                         '\n6: Açúcar 1kg R$3 (Tem {açúcar[0]})'
                         '\n7: Sal 500g R$2 (Tem {sal[0]})'
                         '\n8: Fermento R$3 (Tem {fermento[0]})'
                         '\n9: Óleo R$3 (Tem {óleo[0]})'
                         '\n10: Sair do mercado\n'.format_map(dt['comida']))
            if int(acao) == 10:
                return
            else:
                comida = tuple(dt['comida'].keys())
                for y in acao.split(','): #Cada indice de acao
                    for x in comida:      #Cada item de comida
                        if comida[int(y)-1] in x and dt['dinheiro'] >= dt['comida'][x][1]: 
                            print('Comprou', x, 'por', dt['comida'][x][1], 'reais.')
                            dt['dinheiro'] -= dt['comida'][x][1]
                            dt['comida'][x][0] += 1
                            break #Pula para o próximo indice de acao
                        elif dt['dinheiro'] < dt['comida'][x][1]:
                            print('Você não tem dinheiro!')

        except (ValueError, IndexError, TypeError):
            print('Comando desconhecido!')
        sleep(1)
        # FIM DAS COMPRAS NO MERCADO

# PRATICAR EXERCICIOS:
def exercicios():
    global peso
    loadprint('Você foi praticar exercícios', 5)
    print('Você perdeu 0.5kg, mas ficou cansado. Descanse um pouco!\n')
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
    print('')
    for i in range(4):
        print('\rTrabalhando', end=i*'.', flush=True)
        sleep(1)
    print('\nVocê terminou seu trabalho e ganhou 10 reais\n')
    dt['dinheiro'] += 10
    if dt['cansaço']:
        dt['cansaço'] -= 1
    dt['stress'] += 1
    sleep(3)

# COZINHA
def cozinha():
    while True:
        try:
            acao = int(input('\nVocê está na cozinha'
                                '\n1: Comer ou beber algo'
                                '\n2: Fazer alguma receita'
                                '\n3: Sair da cozinha\n'))
            if acao == 1:
                cozinha_comer()
            elif acao == 2:
                cozinha_receita()
            elif acao == 3:
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
            acao = int(input('\nVocê foi comer algo'
                             '\nComer/beber o que?'
                             '\n1: Ovo (Tem {ovo[0]})'
                             '\n2: Leite (Tem {leite[0]})'
                             '\n3: Banana (Tem {banana[0]})'
                             '\n4: Trigo 1kg (Tem {trigo[0]})'
                             '\n5: Margarina (Tem {margarina[0]})'
                             '\n6: Açúcar (Tem {açúcar[0]})'
                             '\n7: Comer uma fatia de bolo (Tem {bolo[0]})'
                             '\n8: Comer uma fatia de pão (Tem {pão[0]})'
                             '\n9: Comer um ovo frito (Tem {ovo frito[0]})'
                             '\n10: Comer uma panqueca (Tem {panqueca[0]})'
                             '\n11: Voltar\n'.format_map(dt['comida'])))
            if acao == 11:
                return
                             # 0=Não consumível 1=Consumível
            comida = [('ovo', 0), ('leite', 1), ('banana', 1), ('trigo', 0), ('margarina', 0),
                      ('açúcar', 0), ('bolo', 1), ('pão', 1), ('ovo frito', 1), ('panqueca', 1)]
            if comida[acao-1][1] and dt['comida'][comida[acao-1][0]][0] >= dt['comida'][comida[acao-1][0]][2][0]:
                print('Você comeu/bebeu', comida[acao-1][0], '!')
                dt['comida'][comida[acao-1][0]][0] = round(dt['comida'][comida[acao-1][0]][0] - dt['comida'][comida[acao-1][0]][2][0], 2)
                peso = round(peso + dt['comida'][comida[acao-1][0]][2][1], 2)
            elif comida[acao-1][1] == 0:
                print('Você não pode comer isso no momento')
            else:
                print('Você não tem essa comida')

        except (ValueError, IndexError):
            print('Comando desconhecido!')
        sleep(1)


def cozinha_receita():
    while True:
        try:
            acao = int(input('\nVocê pensou em fazer uma receita...'
                             '\nFazer o quê?'
                             '\n1: Bolo de banana (3 bananas, 3 ovos, 2 xícaras de trigo 200g, 1 copo de leite 200ml, 3 colheres de margarina, 1.5 xícara de açúcar 150g, 1 colher (chá) de fermento)'
                             '\n2: Pão (1 kg de trigo, 1/2 xícara de açúcar 50g, 1/2 xícara de óleo 100ml, 1/2 colher de sopa de sal, 2 copos de água, 15g de fermento)'
                             '\n3: Ovo frito (1 ovo, 1 colher de sopa óleo 15ml,  1/2 colher de sopa de sal)'
                             '\n4: Panqueca (2 xícaras de trigo 200g, 2 copos de leite 250ml, 3 ovos)\n'
                             '\n5: Voltar\n'))
            if acao == 5:
                return
            comida = ('bolo', 'pão', 'ovo frito', 'panqueca')
            deco = [('fazer um bolo de banana', 'fez um bolo de banana', 6),
                    ('fazer um pão', 'fez um pão', 6),
                    ('fritar um ovo', 'fritou um ovo', 2),
                    ('fazer uma panqueca', 'fez uma panqueca', 2)]
            for i, ing in enumerate(dt['comida'][comida[acao-1]][1]):
                if dt['comida'][ing[0]][0] >= dt['comida'][comida[acao-1]][1][i][1]: #Testa se tem o suficiente de um item...
                    if ing == dt['comida'][comida[acao-1]][1][-1]: #Testa se é o ultimo da lista
                        loadprint('Você comecou a ' + deco[acao-1][0], 5)
                        print('')
                        for i, ing in enumerate(dt['comida'][comida[acao-1]][1]): #Subtrai os items
                            dt['comida'][ing[0]][0] -= dt['comida'][comida[acao-1]][1][i][1]
                            sleep(deco[acao-1][2] / len(dt['comida'][comida[acao-1]][1]))
                            print(ing[0].capitalize()+'...', end='')

                        print('\r\033[K ......', end='\r')
                        sleep(1)
                        print('Você', deco[acao-1][1] +'!')
                        dt['comida'][comida[acao-1]][0] += 1
                else:
                    print('Você não tem os ingredientes necessários')
                    break
        except (ValueError, IndexError):
            print('Comando desconhecido!')
        sleep(1)
#TODO:
# CASA
def main():
    while True:
        try:
            acao = int(input('\nVocê está em casa. Escolha o que fazer:         |ESTATÍSTICAS '
                             '\n1: Ir ao mercado                                |PESO:'+ str(peso) +'kg'
                             '\n2: Dispensar o personal trainer e terminar      |CANSAÇO: {cansaço}' 
                             '\n3: Praticar exercícios                          |DINHEIRO: {dinheiro}' 
                             '\n4: Ir ao trabalho                               |STRESS: {stress}' 
                             '\n5: Consultar o personal trainer virtual'
                             '\n6: Ir à cozinha\n'.format_map(dt)))
            if acao == 1:
                mercado()
            elif acao == 2:
                print('Você dispensou o personal trainer e terminou o jogo.')
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
                print('Comando desconhecido!')
        except ValueError:
            print(erroValor)
        
        #FINAIS
        if dt['stress'] >= 10:
            print('\nVocê morreu de stress, infelizmente.')
            break
        elif peso >= 250:
            print('\nVocê ficou muito gordo(a) e morreu')
            break
        elif dt['cansaço'] >= 20:
            print('\nEm sua compulsividade por ficar magro(a), se exercitou tanto que morreu de cansaço!')
            break
        elif peso <= 10:
            print('\nDiagnosticado(a) com anorexia, mas agora já é tarde demais, porque você TÁ MORTO(a)!!')
            break
        sleep(1)
    print('Game Over')
    sleep(10)

main()

