import random
from typing import List
from codigo_base import ProblemaMVP, penalizacao

def selecao_roleta(populacao: List[list[int]], aptidoes: List[int]):
    total_aptidao = sum(aptidoes)

    if total_aptidao == 0:
        return random.choice(populacao)
    
    sorteado = random.uniform(0, total_aptidao)
    soma_parcial = 0
    for i in range(len(populacao)):
        atual = populacao[i]
        aptidao_atual = aptidoes[i]
        soma_parcial += aptidao_atual

        if soma_parcial >= sorteado:
            return atual
    return populacao[-1]

def reproduz(x: list[int], y: list[int]) -> list[int]:
    n = len(x)
    ponto_corte = random.randint(1, n - 1)
    filho = x[:ponto_corte] + y[ponto_corte:]
    return filho

def mutacao(filho: list[int]):
    mutado = filho[:]
    index = random.randrange(len(mutado))
    mutado[index] = 1 - mutado[index]
    return mutado

def algoritmo_genetico(problema: ProblemaMVP, populacao_inicial: List[list[int]], prob_mutacao: float, num_geracoes: int):
    populacao = populacao_inicial[:]

    for _ in range(num_geracoes):
        nova_populacao = []
        aptidoes_atuais = [penalizacao(individuo, problema) for individuo in populacao]

        for _ in range(len(populacao)):
            x = selecao_roleta(populacao, aptidoes_atuais)
            y = selecao_roleta(populacao, aptidoes_atuais)
            filho = reproduz(x, y)
            if random.random() < prob_mutacao:
                filho = mutacao(filho)
            
            nova_populacao.append(filho)
        
        populacao = nova_populacao

    aptidoes_finais = [penalizacao(ind, problema) for ind in populacao]
    indice_melhor = aptidoes_finais.index(max(aptidoes_finais))
    melhor_individuo = populacao[indice_melhor]

    return melhor_individuo