class Pessoa(object):
	def __init__(self, nome=None, peso=None, altura=None):
		self.nome = nome
		self.peso = peso
		self.altura = altura
		self.dinheiro = 5
		self.cansaco = 0
		self.stress = 0

	def ganhar_peso(self, quantidade):
		self.peso += quantidade

	def perder_peso(self, quantidade):
		self.peso -= quantidade

	def ganhar_stress(self, quantidade):
		self.stress += quantidade

	def perder_stress(self, quantidade):
		self.stress -= quantidade
		if self.stress < 0:
			self.stress = 0

	def ganhar_cansaco(self, quantidade):
		self.cansaco += quantidade

	def perder_cansaco(self, quantidade):
		self.cansaco -= quantidade
		if self.cansaco < 0:
			self.cansaco = 0

	def ganhar_dinheiro(self, quantidade=1):
		self.dinheiro += quantidade

	def perder_dinheiro(self, quantidade=1):
		if self.dinheiro - quantidade < 0:
			return 'erroSemDinheiro'
		else:
			self.dinheiro -= quantidade


	def imc(self):
		return round(self.peso / ( self.altura / 100 ) ** 2, 2)


class Item(object):
	def __init__(self):
		self.data = {
				'ovo' : 0,
				'leite' : 0,
				'banana' : 0,
				'trigo' : 0,
				'margarina' : 0,  # <- Uma colher = 0.08
				'acucar' : 0,
				'fermento' : 0,
				'oleo' : 0,
				'sal' : 0,
				'bolo' : 0,
				'pao' : 0,
				'ovo_frito' : 0,  # unidade
				'panqueca' : 0,  # unidade
				}

	def ganhar_item(self, **kwargs):
		for kw in kwargs:
			self.data[kw] += kwargs[kw]


	def perder_item(self, **kwargs):
		for kw in kwargs:
			self.data[kw] -= kwargs[kw]
			if self.data[kw] < 0:
				self.data[kw] = 0

	def debug(self):
		for i in self.data:
			self.data[i] = 500

