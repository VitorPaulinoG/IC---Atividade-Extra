import random
import math
from typing import List
from codigo_base import ProblemaMVP, penalizacao


def simulated_annealing(problema: ProblemaMVP, escalonamento):
    atual = problema.estado_inicial 
    melhor_solucao = atual
    t = 1
    while True:
        T = escalonamento(t)
        if T == 0: 
            return melhor_solucao
        proximo = sucessor_aleatorio(atual)
        
        valor_proximo = penalizacao(proximo, problema)
        valor_atual = penalizacao(atual, problema)

        diff = valor_proximo - valor_atual
        if diff > 0:
            atual = proximo
        else:
            if random.random() < math.exp(diff / T):
                atual = proximo
        
        if penalizacao(atual, problema) > penalizacao(melhor_solucao, problema):
            melhor_solucao = atual
        t += 1


def sucessor_aleatorio(atual: List[int]):
    sucessor = atual.copy()
    index = random.randrange(len(atual))
    sucessor[index] = 1 - sucessor[index]
    return sucessor
        