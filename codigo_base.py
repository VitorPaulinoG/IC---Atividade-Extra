import random
from typing import List
class Funcionalidade:
    def __init__(self, nome: str, custo: int, valor: int):
        self.nome = nome
        self.custo = custo
        self.valor = valor

class ProblemaMVP:
    def __init__(self, funcionalidades: List[Funcionalidade], custo_maximo):
        self.funcionalidades = funcionalidades
        self.estado_inicial = [random.randint(0, 1) for _ in range(len(funcionalidades))]
        self.custo_maximo = custo_maximo

def valor_e_custo(solucao: List[int], problema: ProblemaMVP):
    custo_total = 0
    valor_total = 0
    for i in range(len(solucao)):
        if solucao[i] == 1:
            custo_total += problema.funcionalidades[i].custo
            valor_total += problema.funcionalidades[i].valor
    return valor_total, custo_total

def penalizacao(solucao: List[int], problema: ProblemaMVP):
    valor_real, custo_real = valor_e_custo(solucao, problema)
    if custo_real > problema.custo_maximo:
        return 0
    return valor_real
