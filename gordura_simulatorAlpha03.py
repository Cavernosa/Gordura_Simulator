# coding=utf-8
erroValor = 'Entrada inválida! Coloque apenas números.'
nome = input('Olá, eu sou seu personal trainer virtual, qual o seu nome?\n')

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
# soma dos valores inteiros

"""soma_imc = pso / altura_dec ** 2
print('Seu IMC:', soma_imc)
if soma_imc < 17:
    print('Você está muito abaixo do peso, engorde!')
elif soma_imc < 1849 / 100:
    print('Você está abaixo do peso, coma mais.')
elif soma_imc < 2499 / 100:
    print('Peso normal, muito bem, continue assim!')
elif soma_imc < 2999 / 100:
    print('Acima do Peso, eu estou vendo esse bolo de banana que você está fazendo.')
elif soma_imc < 3499 / 100:
    print('Obesidade, vá praticar alguns exercícios!')
elif soma_imc < 3999 / 100:
    print('Obesidade severa, muito gordo, pare de comer bolo de banana e vá praticar exercício.')
else:
    print('Obesidade mórbida, procure ajuda!!!')"""
import time

time.sleep(2)

def personal():
    soma_imc = peso / altura_dec ** 2
    print('\nSeu IMC:', soma_imc)
    if soma_imc < 17:
        print('Você está muito abaixo do peso, engorde!\n')
    elif soma_imc < 1849 / 100:
        print('Você está abaixo do peso, coma mais\n')
    elif soma_imc < 2499 / 100:
        print('Peso normal, muito bem, continue assim!\n')
    elif soma_imc < 2999 / 100:
        print('Acima do Peso, eu estou vendo esse bolo de banana que você está fazendo\n')
    elif soma_imc < 3499 / 100:
        print('Obesidade, vá praticar alguns exercicios!\n')
    elif soma_imc < 3999 / 100:
        print('Obesidade severa, muito gordo, pare de comer bolo de banana e vá praticar exercicio\n')
    else:
        print('Obesidade mórbida, procure ajuda!!!\n')
    time.sleep(2)

personal()

# INICIO DO GAME GORDURA SIMULATOR
time.sleep(2)

# banco de dados
dinheiro = 5
cansaco = 0
stress = 0
ovo = 0
leite = 0
banana = 0
trigo = 0
margarina = 0 # <- Uma colher = 0.08
acucar = 0
fermento = 0
oleo = 0
sal = 0
bolo = 0
pao = 0

# MERCADO
def mercado():
    while True:
        try:
            acao_mercado = int(input('\nVocê foi ao mercado com {0} reais no bolso'
                                    '\n1: Comprar algo'
                                    '\n2: Voltar pra casa'
                                    '\n'.format(str(dinheiro))))

            if acao_mercado == 1:
                compras()
            elif acao_mercado == 2:
                return
            else:
                print('Comando desconhecido!')
        except ValueError:
                print(erroValor)
        time.sleep(1)

def compras():
    while True:
        global dinheiro, leite, ovo, banana, trigo, margarina,acucar, fermento, oleo, sal
        try:
            acao_compra = int(input('\nVocê foi ver oque tem para comprar'
                                    '\nVai comprar oque?'
                                    '\n1: Ovo R$2 (Tem {0})'
                                    '\n2: Leite R$3 (Tem {1})'
                                    '\n3: Banana R$1 (Tem {2})'
                                    '\n4: Trigo 1kg R$3 (Tem {3})'
                                    '\n5: Margarina R$5 (Tem {4})'
                                    '\n6: Açucar 1kg R$3 (Tem {5})'
                                    '\n7: Sal 500g R$2 (Tem {6})'
                                    '\n8: Fermento R$3 (Tem {7})'
                                    '\n9: Óleo R$3 (Tem {8})'
                                    '\n10: Sair do mercado\n'.format(ovo, leite, banana, trigo, margarina, acucar, sal, fermento, oleo)))
            if acao_compra == 1 and dinheiro >= 2:
                dinheiro = dinheiro - 2
                print('Você comprou um ovo por 2 reais')
                ovo = ovo + 1

            elif acao_compra == 2 and dinheiro >= 3:
                dinheiro = dinheiro - 3
                print('Você comprou um leite por 3 reais')
                leite = leite + 1

            elif acao_compra == 3 and dinheiro >= 1:
                dinheiro = dinheiro - 1
                print('Você comprou uma banana por 1 real')
                banana = banana + 1

            elif acao_compra == 4 and dinheiro >= 3:
                dinheiro = dinheiro - 3
                print('Você comprou um pacote de trigo por 3 reais')
                trigo = trigo + 1

            elif acao_compra == 5 and dinheiro >= 5:
                dinheiro = dinheiro - 5
                print('Você comprou uma margarina por 5 reais')
                margarina = margarina + 1

            elif acao_compra == 6 and dinheiro >= 3:
                dinheiro = dinheiro - 3
                print('Você comprou um pacote de açucar por 3 reais')
                acucar = acucar + 1

            elif acao_compra == 7 and dinheiro >= 2:
                dinheiro = dinheiro - 2
                print('Você comprou um sal 500g por 2 reais')
                sal = sal + 1

            elif acao_compra == 8 and dinheiro >= 3:
                dinheiro = dinheiro - 3
                print ('Você comprou um potinho de fermento por 3 reais')
                fermento = fermento + 1

            elif acao_compra == 9 and dinheiro >= 3:
                dinheiro = dinheiro - 3
                print('Você comprou um óleo por 3 reais')
                oleo = oleo + 1

            elif acao_compra == 10:
                return
            else:
                print('Você não tem dinheiro para comprar isso ou o comando é desconhecido!')

        except ValueError:
            print(erroValor)
        time.sleep(1)
        # FIM DAS COMPRAS NO MERCADO


# PRATICAR EXERCICIOS:
def exercicios():
    global peso, cansaco, stress
    print('\nVocê foi praticar exercícios')
    time.sleep(5)
    print('Você perdeu 0,5 kg mas ficou cansado, descanse um pouco\n')
    peso = peso - 1 / 2
    cansaco = cansaco + 2
    if stress:
        stress = stress - 1
    time.sleep(3)


# TRABALHAR:
def trabalho():
    global dinheiro, cansaco, stress
    print('\nVocê foi trabalhar\n...')
    time.sleep(3)
    print('Trabalhando...')
    time.sleep(3)
    print('Você terminou seu trabalho e ganhou 10 reais\n')
    dinheiro = dinheiro + 10
    if cansaco:
        cansaco = cansaco - 1
    stress = stress + 1
    time.sleep(3)


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
        time.sleep(1)

def cozinha_comer():
    while True:
        global peso, leite, banana, bolo, pao
        try:
            acao_cozinha = int(input('\nVocê foi comer algo'
                                     '\nComer/beber oque?'
                                     '\n1: Ovo (Tem {0})'
                                     '\n2: Leite (Tem {1})'
                                     '\n3: Banana (Tem {2})'
                                     '\n4: Trigo 1kg (Tem {3})'
                                     '\n5: Margarina (Tem {4})'
                                     '\n6: Açúcar (Tem {5})'
                                     '\n7: Comer uma fatia de bolo (Tem {6})'
                                     '\n8: Comer uma fatia de pão (Tem {7})'
                                     '\n9: Voltar\n'.format(ovo, leite, banana, trigo, margarina, acucar, bolo, pao)))

            if acao_cozinha == 2 and leite >= 0.25:
                print('Você bebeu um pouco de leite e engordou 0.10kg')
                leite = leite - 0.25
                peso = peso + 0.10

            elif acao_cozinha == 3 and banana >= 1:
                print('Você comeu uma banana e engordou 0.20kg')
                banana = banana - 1
                peso = peso + 0.20

            elif acao_cozinha == 7 and bolo >= 0.1:
                print('Você comeu uma fatia de bolo')
                bolo = bolo - 0.1
                peso = peso + 0.50

            elif acao_cozinha == 8 and pao >= 0.05:
                print ('Você comeu uma fatia de pão')
                pao = pao - 0.05
                peso = peso + 0.10
            elif acao_cozinha == 9:
                return
            else:
                print('Você não pode comer isso ou você não tem ele ou o comando é desconhecido')
        except ValueError:
            print(erroValor)
        time.sleep(1)

def cozinha_receita():
    while True:
        global banana, ovo, trigo, leite, margarina, acucar, fermento, oleo, sal, bolo, pao
        try:
            cozinha_receita = int(input('\nVocê pensou em fazer uma receita...'
                                        '\nFazer o quê?'
                                        '\n1: Bolo de banana (3 bananas, 3 ovos, 2 xícaras de trigo 200gr, 1 copo de leite 200ml, 3 colheres de margarina, 1.5 xícara de açúcar 150gr, 1 colher (chá) de fermento)'
                                        '\n2: Pão (1 kg de trigo, 1/2 xícara de açúcar 50gr, 1/2 xícara de óleo 100ml, 1/2 colher de sopa de sal, 2 copos de água, 15gr de fermento)'
                                        '\n3: Voltar\n'))
            if cozinha_receita == 1 and banana >= 3 and ovo >= 3 and trigo >= 0.2 and leite >= 0.2 and margarina >= 0.24 and acucar >= 0.15 and fermento >= 0.10:
                print('\nVocê começou a preparar seu bolo')
                banana = banana - 3
                ovo = ovo - 3
                trigo = trigo - 0.2
                leite = leite - 0.2
                margarina = margarina - 0.24
                acucar = acucar - 0.15
                fermento = fermento - 0.10
                time.sleep(6)
                bolo = bolo + 1
                print ('Você terminou de fazer o bolo')

            elif cozinha_receita == 2 and trigo >= 1 and acucar >= 0.05 and oleo >= 0.1 and sal >= 0.01 and fermento >= 0.15:
                print('\nVocê começou a fazer um pão')
                trigo = trigo - 1
                acucar = acucar - 0.05
                oleo = oleo - 0.1
                sal = sal - 0.01
                fermento = fermento - 0.15
                time.sleep(6)
                pao = pao + 1
                print ('Você terminou de fazer o pão')

            elif cozinha_receita == 3:
                return
            else:
                print('Você não tem ingredientes ou o comando é desconhecido')
        except ValueError:
            print(erroValor)
        time.sleep(1)

# CASA

def main():
    while True:
        try:
            acao = int(input('\nVocê está em casa. Escolha oque fazer:          |ESTATÍSTICAS '
                             '\n1: Ir ao mercado                                |PESO:' + str(peso) + 'kg'
                             '\n2: Dispensar o personal trainer e terminar      |CANSAÇO:' + str(cansaco) +
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
        elif cansaco >= 20:
            print('\nEm sua compulsividade por ficar magro, se exercitou tanto que morreu de cansaço!')
            break
        elif peso <= 10:
            print('\nMorreu com fome. Será que estava fingindo ser uma criança africana?')
            break
        time.sleep(1)
    time.sleep(10)

main()
