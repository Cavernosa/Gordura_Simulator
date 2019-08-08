# coding=utf-8
print('Olá, eu sou seu personal trainer virtual, qual o seu nome?')
nome = input()
print('Ok', nome, ',agora preciso saber seu peso e altura para saber se você está fora de forma')
# valores string:
peso_str = input('Peso (em kg, apenas números):')
altura_str = input('Altura (em centímetros, apenas números):')

# conversão dos valores string:
peso_int = int(peso_str)
altura_int = int(altura_str)
altura_dec = altura_int / 100

# soma dos valores inteiros

soma_imc = peso_int / altura_dec ** 2
print(soma_imc)
if soma_imc < 17:
    print('Você está muito abaixo do peso, engorde!')
elif soma_imc < 1849 / 100:
    print('Você está abaixo do peso, coma mais')
elif soma_imc < 2499 / 100:
    print('Peso normal, muito bem, continue assim!')
elif soma_imc < 2999 / 100:
    print('Acima do Peso, eu estou vendo esse bolo de banana que você está fazendo')
elif soma_imc < 3499 / 100:
    print('Obesidade, vá praticar alguns exercicios!')
elif soma_imc < 3999 / 100:
    print('Obesidade severa, muito gordo, pare de comer bolo de banana e vá praticar exercicio')
else:
    print('Obesidade mórbida, procure ajuda!!!')
import time

time.sleep(2)


def personal():
    soma_imc = peso_int / altura_dec ** 2
    print(soma_imc)
    if soma_imc < 17:
        print('Você está muito abaixo do peso, engorde!')
    elif soma_imc < 1849 / 100:
        print('Você está abaixo do peso, coma mais')
    elif soma_imc < 2499 / 100:
        print('Peso normal, muito bem, continue assim!')
    elif soma_imc < 2999 / 100:
        print('Acima do Peso, eu estou vendo esse bolo de banana que você está fazendo')
    elif soma_imc < 3499 / 100:
        print('Obesidade, vá praticar alguns exercicios!')
    elif soma_imc < 3999 / 100:
        print('Obesidade severa, muito gordo, pare de comer bolo de banana e vá praticar exercicio')
    else:
        print('Obesidade mórbida, procure ajuda!!!')
    time.sleep(2)


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
        acao_mercado = int(input('\nVocê foi ao mercado com {0} reais no bolso'
                                 '\n1: Comprar algo'
                                 '\n2: Voltar pra casa'
                                 '\n'.format(str(dinheiro))))
        if acao_mercado == 1:
            compras()
        if acao_mercado == 2:
            return


def compras():
    while True:
        global dinheiro, leite, ovo, banana, trigo, margarina,acucar, fermento, oleo, sal
        acao_compra = int(input('\nVocê foi ver oque tem para comprar'
                                '\nVai comprar oque?'
                                '\n1: Ovo R$2'
                                '\n2: Leite R$3'
                                '\n3: Banana R$1'
                                '\n4: Trigo 1kg R$3'
                                '\n5: Margarina R$5'
                                '\n6: Açucar 1kg R$3'
                                '\n7: Sal 500g R$2'
                                '\n8: Fermento R$3'
                                '\n9: Óleo R$3'
                                '\n10: Sair do mercado\n')) #Trocar o sair do mercado pro 10 #CORRIGIR#
        if acao_compra == 1 and dinheiro >= 2:
            dinheiro = dinheiro - 2
            print('Você comprou um ovo por 2 reais')
            time.sleep(1)
            ovo = ovo + 1

        elif acao_compra == 2 and dinheiro >= 3:
            dinheiro = dinheiro - 3
            print('Você comprou um leite por 3 reais')
            time.sleep(1)
            leite = leite + 1

        elif acao_compra == 3 and dinheiro >= 1:
            dinheiro = dinheiro - 1
            print('Você comprou uma banana por 1 real')
            time.sleep(1)
            banana = banana + 1

        elif acao_compra == 4 and dinheiro >= 3:
            dinheiro = dinheiro - 3
            print('Você comprou um pacote de trigo por 3 reais')
            time.sleep(1)
            trigo = trigo + 1

        elif acao_compra == 5 and dinheiro >= 5:
            dinheiro = dinheiro - 5
            print('Você comprou uma margarina por 5 reais')
            time.sleep(1)
            margarina = margarina + 1

        elif acao_compra == 6 and dinheiro >= 3:
            dinheiro = dinheiro - 3
            print('Você comprou um pacote de açucar por 3 reais')
            time.sleep(1)
            acucar = acucar + 1

        elif acao_compra == 10:
            return

        elif acao_compra == 8 and dinheiro >= 3:
            dinheiro = dinheiro - 3
            print ('Você comprou um potinho de fermento por 3 reais')
            fermento = fermento + 1
            time.sleep(1)

        elif acao_compra == 9 and dinheiro >= 3:
            dinheiro = dinheiro - 3
            print('Você comprou um óleo por 3 reais')
            oleo = oleo + 1
            time.sleep(1)

        elif acao_compra == 7 and dinheiro >= 2:
            dinheiro = dinheiro - 2
            print ('Você comprou um sal 500g por 2 reais')
            sal = sal + 1
            time.sleep(1)

        else:
            print('Você não tem dinheiro para comprar isso ou o comando é desconhecido!')
            time.sleep(1)

        # FIM DAS COMPRAS NO MERCADO


# PRATICAR EXERCICIOS:
def exercicios():
    print('Você foi praticar exercícios')
    time.sleep(5)
    print('Você perdeu 0,5 kg mas ficou cansado, descanse um pouco')
    global peso_int
    global cansaco
    global stress
    peso_int = peso_int - 5 / 10
    cansaco = cansaco + 2
    if stress >= 1:
        stress = stress - 1
    print(cansaco, peso_int)
    time.sleep(3)


# TRABALHAR:
def trabalho():
    print('Você foi trabalhar')
    print('...')
    time.sleep(3)
    print('Trabalhando...')
    time.sleep(3)
    print('Você terminou seu trabalho e ganhou 10 reais')
    global dinheiro, cansaco, stress
    dinheiro = dinheiro + 10
    if cansaco >= 1:
        cansaco = cansaco - 1
    stress = stress + 1
    time.sleep(3)


# COZINHA
def cozinha():
    while True:
        print('\nVocê foi à cozinha')
        cozinha = int(input('1: Comer/beber algo'
                            '\n2: Fazer alguma receita'
                            '\n3: Sair da cozinha\n'))
        if cozinha == 1:
            cozinha_comer()
        elif cozinha == 2:
            cozinha_receita()
        elif cozinha == 3:
            return
def cozinha_comer():
    while True:
        print('\nVocê foi comer algo')
        acao_cozinha = int(input('Comer/beber oque?'
                                 '\n1: Ovo'
                                 '\n2: Leite'
                                 '\n3: Banana'
                                 '\n4: Trigo 1kg'
                                 '\n5: Margarina'
                                 '\n6: Açúcar'
                                 '\n7: Comer uma fatia de bolo'
                                 '\n8: Comer uma fatia de pão'
                                 '\n9: Voltar'))
        global peso_int, leite, banana, bolo, pao
        if acao_cozinha == 2 and leite >= 0.25:
            print('Você bebeu um pouco de leite e engordou 0.10kg')
            leite = leite - 0.25
            peso_int = peso_int + 0.10
            time.sleep(1)
        elif acao_cozinha == 3 and banana >= 1:
            print('Você comeu uma banana e engordou 0.20kg')
            banana = banana - 1
            peso_int = peso_int + 0.20
            time.sleep(1)
        elif acao_cozinha == 7 and bolo >= 0.1:
            print('Você comeu uma fatia de bolo')
            bolo = bolo - 0.1
            peso_int = peso_int + 0.50
            time.sleep(1)
        elif acao_cozinha == 8 and pao >= 0.05:
            print ('Você comeu uma fatia de pão')
            pao = pao - 0.05
            peso_int = peso_int + 0.10
        elif acao_cozinha == 9:
            return

        else:
            print('Você não pode comer isso ou não é de comer puro')
            time.sleep(1)

def cozinha_receita():
    while True:
        global banana, ovo, trigo, leite, margarina, acucar, fermento, oleo, sal, bolo, pao
        print('\nVocê pensou em fazer uma receita')
        cozinha_receita = int(input('Fazer oque?'
                                    '\n1: Bolo de banana (3 bananas, 3 ovos, 2 xícaras de trigo 200gr, 1 copo de leite 200ml, 3 colheres de margarina, 1.5 xícara de açúcar 150gr, 1 colher (chá) de fermento'
                                    '\n2: Pão (1 kg de trigo, 1/2 xícara de açúcar 50gr, 1/2 xícara de óleo 100ml, 1/2 colher de sopa de sal, 2 copos de água, 15gr de fermento'
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
            time.sleep(1)

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
            time.sleep(1)
        elif cozinha_receita == 3:
            return
        else:
            print('\nVocê não tem ingredientes ou o comando é desconhecido')
            time.sleep(2)


# CASA

def main():
    while True:
        acao = int(input('\nVocê está em casa. Escolha oque fazer:          |ESTATÍSTICAS '
                         '\n1: Ir ao mercado                                |PESO:' + str(peso_int) + 'kg'
                         '\n2: Dispensar o personal trainer e terminar      |CANSAÇO:' + str(cansaco) +
                         '\n3: Praticar exercícios                          |DINHEIRO:' + str(dinheiro) +
                         '\n4: Ir ao trabalho                               |STRESS:' + str(stress) +
                         '\n5: Consultar o personal trainer virtual'
                         '\n6: Ir à cozinha\n'))
        if acao == 1:
            mercado()
        elif acao == 2:
            break
        elif acao == 3:
            exercicios()
        elif acao == 4:
            trabalho()
        elif acao == 5:
            personal()
        elif acao == 6:
            cozinha()
        if stress >= 10:
            print('Você morreu de stress')
            break
        elif peso_int >= 250:
            print('Você ficou muito gordo e morreu')
            break
        elif cansaco >= 20:
            print('Ficou tão cansado que morreu')
            break
        elif peso_int <= 10:
            print('Morreu com fome')
            break
    print('Você dispensou o personal trainer e terminou o jogo')


main()
