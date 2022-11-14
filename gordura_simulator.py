# coding: utf8

from time import sleep
import classes.pessoa

erroValor = 'Entrada inválida! Coloque apenas números.'

pessoa = classes.pessoa.Pessoa()
item = classes.pessoa.Item()

pessoa.nome = str(input('Olá, eu sou seu personal trainer virtual, qual o seu nome?\n'))

print(f'Ok {pessoa.nome}, agora preciso saber seu peso e altura para saber se você está fora de forma')
# valores string:
while True:
	try:
		pessoa.peso = int(input('Peso (em kg, apenas números):'))
		pessoa.altura = int(input('Altura (em centímetros, apenas números):'))
		break
	except ValueError:
		print(erroValor)

def personal():
	soma_imc = pessoa.imc()
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
		print('Obesidade, vá praticar alguns exercícios!\n')
	elif soma_imc < 3999 / 100:
		print('Obesidade severa, muito gordo, pare de comer bolo de banana e vá praticar exercício\n')
	else:
		print('Obesidade mórbida, procure ajuda!!!\n')
	#sleep(5)


personal()

print('GORDURA SIMULATOR')
# INICIO DO GAME GORDURA SIMULATOR

def gerar_sufixo(var, singular='l', plural='is'):
	"""Retorna um sufixo plural ou singular dependendo do valor de var"""
	if var == 1:
		return singular
	else:
		return plural


# MERCADO
def mercado():
	while True:
		try:
			acao_mercado = int(input(
				f'\nVocê foi ao mercado com {pessoa.dinheiro} rea{gerar_sufixo(pessoa.dinheiro)} no bolso'
				'\n1: Comprar algo'
				'\n2: Voltar pra casa\n'))

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
			acao_compra = int(input(
				f'\nVocê foi ver o que tem para comprar com {pessoa.dinheiro} rea{gerar_sufixo(pessoa.dinheiro)}'
				f'\nVai comprar o quê?'
				f'\n1: Ovo R$2 .........(Tem {item.data["ovo"]})'
				f'\n2: Leite R$3 .......(Tem {item.data["leite"]})'
				f'\n3: Banana R$1 ......(Tem {item.data["banana"]})'
				f'\n4: Trigo 1kg R$3 ...(Tem {item.data["trigo"]})'
				f'\n5: Margarina R$5 ...(Tem {item.data["margarina"]})'
				f'\n6: Açúcar 1kg R$3 ..(Tem {item.data["acucar"]})'
				f'\n7: Sal 500g R$2 ....(Tem {item.data["sal"]})'
				f'\n8: Fermento R$3 ....(Tem {item.data["fermento"]})'
				f'\n9: Óleo R$3 ........(Tem {item.data["oleo"]})'
				'\n10: Sair do mercado\n'))

			def comprar(custo, item_desc, **itens):
				if pessoa.perder_dinheiro(custo) == 'erroSemDinheiro':
					print('Você não tem dinheiro para comprar isto')
					return

				item.ganhar_item(**itens)
				print(f'Você comprou {item_desc} por {custo} rea{gerar_sufixo(custo)}')

			match acao_compra:
				case 1: comprar(2, 'um ovo', ovo=1)
				case 2: comprar(3, 'um leite', leite=1)
				case 3: comprar(1, 'uma banana', banana=1)
				case 4: comprar(3, 'um pacote de trigo', trigo=1)
				case 5: comprar(5, 'uma margarina', margarina=1)
				case 6: comprar(3, 'um pacote de açúcar', acucar=1)
				case 7: comprar(2, 'um sal 500g', sal=1)
				case 8: comprar(3, 'um potinho de fermento', fermento=1)
				case 9: comprar(3, 'um óleo', oleo=1)
				case 10: return
				case _: print('Comando desconhecido')

		except ValueError:
			print(erroValor)
		sleep(1)
		# FIM DAS COMPRAS NO MERCADO


# PRATICAR EXERCICIOS:
def exercicios():
	print('\nVocê foi praticar exercícios')
	sleep(5)

	pessoa.perder_peso(0.5)
	pessoa.ganhar_cansaco(2)
	pessoa.perder_stress(1)
	
	print('Você perdeu 0,5 kg, mas ficou cansado. Descanse um pouco\n')
	sleep(3)


# TRABALHAR:
def trabalho():
	print('\nVocê foi trabalhar\n...')
	sleep(3)
	print('Trabalhando...')
	sleep(3)

	pessoa.ganhar_dinheiro(10)
	pessoa.perder_cansaco(1)
	pessoa.ganhar_stress(1)

	print('Você terminou seu trabalho e ganhou 10 reais\n')
	sleep(3)


# COZINHA
def cozinha():
	while True:
		try:
			cozinha = int(input(
				'\nVocê está na cozinha'
				'\n1: Comer/beber algo'
				'\n2: Fazer alguma receita'
				'\n3: Sair da cozinha\n'))

			match cozinha:
				case 1: cozinha_comer()
				case 2: cozinha_receita()
				case 3: return
				case _: print('Comando desconhecido, não tem easter egg!!')

		except ValueError:
			print(erroValor)
		sleep(1)


def cozinha_comer():
	while True:
		try:
			acao_cozinha = int(input(
				'\nVocê foi comer algo'
				'\nComer/beber o que?'
				f'\n 1: Ovo .....................(Tem {item.data["ovo"]})'
				f'\n 2: Leite ...................(Tem {item.data["leite"]})'
				f'\n 3: Banana ..................(Tem {item.data["banana"]})'
				f'\n 4: Trigo 1kg ...............(Tem {item.data["trigo"]})'
				f'\n 5: Margarina ...............(Tem {item.data["margarina"]})'
				f'\n 6: Açúcar ..................(Tem {item.data["acucar"]})'
				f'\n 7: Comer uma fatia de bolo .(Tem {item.data["bolo"]})'
				f'\n 8: Comer uma fatia de pão ..(Tem {item.data["pao"]})'
				f'\n 9: Comer um ovo frito ......(Tem {item.data["ovo_frito"]})'
				f'\n10: Comer uma panqueca ......(Tem {item.data["panqueca"]})'
				'\n11: Voltar\n'))

			def comer(item_desc, peso_ganho, **itens):
				pessoa.ganhar_peso(peso_ganho)
				item.perder_item(**itens)
				peso_pt = peso_ganho.replace('.', ',')
				print(f'Você {item_desc} e engordou {peso_pt}kg')

			match acao_cozinha:
				case 2: comer('bebeu um pouco de leite', 0.10, leite=0.25)
				case 3: comer('comeu uma banana', 0.20, banana=1)
				case 7: comer('comeu uma fatia de bolo', 0.50, bolo=0.1)
				case 8: comer('comeu uma fatia de pão', 0.10, pao=0.05)
				case 9: comer('comeu um ovo frito', 0.10, ovo_frito=1)
				case 10: comer('comeu uma panqueca', 0.20, panqueca=1)
				case 11: return
				case _: print('Você não pode comer isso. Você não tem essa comida ou o comando é desconhecido')

		except ValueError:
			print(erroValor)
		sleep(1)


def cozinha_receita():
	while True:
		global banana, ovo, trigo, leite, margarina, acucar, fermento, oleo, sal, bolo, pao, ovo_frito, panqueca
		try:
			cozinha_receita = int(input(
				'\nVocê pensou em fazer uma receita...'
				'\nFazer o quê?'
				'\n1: Bolo de banana (3 bananas, 3 ovos, 2 xícaras de trigo 200g, 1 copo de leite 200ml, 3 colheres de margarina, 1,5 xícara de açúcar 150g, 1 colher (chá) de fermento)'
				'\n2: Pão (1 kg de trigo, 1/2 xícara de açúcar 50g, 1/2 xícara de óleo 100ml, 1/2 colher de sopa de sal, 2 copos de água, 15g de fermento)'
				'\n3: Ovo frito (1 ovo, 1 colher de sopa de óleo 15ml,  1/2 colher de sopa de sal)'
				'\n4: Panqueca (2 xícaras de trigo 200g, 2 copos de leite 250ml, 3 ovos)\n'
				'\n5: Voltar\n'))

			def receita(item_comecou, item_terminou, resultado, **ingredientes):
				print('Preparando os ingredientes...')
				for i in ingredientes:
					if item.data[i] - ingredientes[i] >= 0:
						print(i.capitalize(), end='.. ', flush=True)
						sleep(0.5)
					else:
						print(f'Você não tem {i}')
						break
				else:
					print(f'Você tem todos os ingredientes e começou a {item_comecou}!')

				item.perder_item(**ingredientes)
				item.ganhar_item(**resultado)

				print(f'Você terminou de {item_terminou}')


			match cozinha_receita:
				case 1: receita('preparar seu bolo', 'fazer o bolo', {'bolo':1}, banana=3, ovo=3, trigo=0.2, leite=0.2, margarina=0.24, acucar=0.15, fermento=0.10) 
				case 2: receita('fazer um pão', 'fazer o pão', {'pao':1}, trigo=1, acucar=0.05, oleo=0.1, sal=0.01, fermento=0.15)
				case 3: receita('fritar um ovo', 'fritar o ovo', {'ovo_frito':1}, ovo=1, oleo=0.15, sal=0.01)
				case 4: receita('fazer uma panqueca', 'fazer a panqueca', {'panqueca':1}, trigo=0.2, leite=0.25, ovo=3)
				case 5: return
				case _: print('Comando desconhecido')

		except ValueError:
			print(erroValor)
		sleep(1)


# CASA

def main():
	while True:
		try:
			acao = int(input(
				'\nVocê está em casa. Escolha o que fazer:         |ESTATÍSTICAS '
				f'\n1: Ir ao mercado                                |ALTURA: {pessoa.altura} cm'
				f'\n2: Dispensar o personal trainer e terminar      |PESO: {pessoa.peso} kg'
				f'\n3: Praticar exercícios                          |DINHEIRO: {pessoa.dinheiro}'
				f'\n4: Ir ao trabalho                               |CANSAÇO: {pessoa.cansaco}'
				f'\n5: Consultar o personal trainer virtual         |STRESS: {pessoa.stress}'
				'\n6: Ir à cozinha\n'))

			match acao:
				case 1: mercado()
				case 2:
					print('Você dispensou o personal trainer e terminou o jogo')
					break
				case 3: exercicios()
				case 4: trabalho()
				case 5: personal()
				case 6: cozinha()
				case _: print('Comando desconhecido')
		except ValueError:
			print(erroValor)

		# FIM DE JOGO
		if pessoa.stress >= 10:
			print('\nVocê morreu de stress')
			break
		elif pessoa.peso >= 250:
			print('\nVocê ficou muito gordo e morreu')
			break
		elif pessoa.cansaco >= 20:
			print('\nEm sua compulsividade por ficar magro, se exercitou tanto que morreu de cansaço!')
			break
		elif pessoa.peso <= 10:
			print('\nMorreu com fome. Será que estava fingindo ser uma criança africana?\nFaça uma doação e contribua com o fim da fome na África!')
			break
		sleep(1)
	sleep(10)

main()
