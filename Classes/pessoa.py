class Pessoa(object):
    ovo = 0
    leite = 0
    banana = 0
    trigo = 0
    margarina = 0  # <- Uma colher = 0.08
    acucar = 0
    fermento = 0
    oleo = 0
    sal = 0
    bolo = 0
    pao = 0
    ovo_frito = 0  # unidade
    panqueca = 0  # unidade

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.dinheiro = 5
        self.cansaço = 0
        self.stress = 0

    def ganha_Peso(self, peso_ganho = 0.1):
        self.peso+=peso_ganho

    def perde_Peso(self, peso_perdido = 0.1):
        self.peso-=peso_perdido

    def aumenta_stress(self):
        self.stress+=1

    def diminui_stress(self):
        self.stress-=1
        if self.stress < 0:
            self.stress = 0

    def aumenta_cansaço(self):
        self.cansaço += 1

    def diminui_cansaço(self):
        self.cansaço -= 1
        if self.cansaço < 0:
            self.cansaço = 0

    def ganha_dinheiro(self, valor=1):
        self.dinheiro+=valor

    def gasta_dinheiro(self, valor=1):
        self.dinheiro -= valor
        if self.dinheiro < 0:
            self.dinheiro = 0

    def retorna_Pessoa(self):
        if especifi == 0:
            return self.nome, self.peso, self.altura, self.dinheiro, self.stress, self.cansaço

    def imc(self):
        return round(self.peso/self.altura * 2,2)

    def retorna_dinheiro(self):
        return self.dinheiro



