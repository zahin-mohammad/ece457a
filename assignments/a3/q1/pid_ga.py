import numpy as np
import heapq
from perffcn import q1_perfFNC
import random


k_p_lower = 2.00
k_p_upper = 18.00

T_I_lower = 1.05
T_I_upper = 9.42

T_D_lower = 0.25
T_D_upper = 2.37


class ProportionalIntegralDifferentialGAS():
    def __init__(self,
                 population_size=50,
                 generation_count=150,
                 prob_crossover=0.6,
                 prob_mutation=0.25,
                 survival_count=2):
        super().__init__()
        self.population_size = population_size
        self.generation_count = generation_count
        self.p_c = prob_crossover
        self.p_m = prob_mutation
        self.survival_count = survival_count
        self.cache = {}

    def reset(self, population_size=50, generation_count=150,
              prob_crossover=0.6,
              prob_mutation=0.25,
              survival_count=2):
        self.population_size = population_size
        self.generation_count = generation_count
        self.p_c = prob_crossover
        self.p_m = prob_mutation
        self.survival_count = survival_count
        self.cache = {}

    def init_population(self):

        return [tuple(np.round(np.array([
                np.random.uniform(low=k_p_lower, high=k_p_upper),
                np.random.uniform(low=T_I_lower, high=T_I_upper),
                np.random.uniform(low=T_D_lower, high=T_D_upper)
                ]), 2)) for i in range(self.population_size)]

    def fitness(self, individual):
        try:
            return self.cache.setdefault(individual, 1.0 / sum(q1_perfFNC(*individual)))
        except:
            return self.cache.setdefault(individual, 0)

    def mutation(self, individuals):
        for i, _ in enumerate(individuals):
            genes = []
            for k, gene in enumerate(individuals[i]):
                if np.random.uniform() <= (self.p_m):
                    genes.append(np.random.uniform(
                        low=k_p_lower, high=k_p_upper))
                else:
                    genes.append(gene)
            individuals[i] = tuple(np.round(np.array(genes), 2))
        return individuals

    def crossover(self, parents):

        children = []
        random.shuffle(parents)

        # Uniform Crossover
        for i in range(1, len(parents), 2):
            child_a, child_b = list(parents[i-1]), list(parents[i])

            for k, gene in enumerate(child_a):
                if np.random.uniform() <= (self.p_c):
                    child_a[k], child_b[k] = child_b[k], child_a[k]
            child_a, child_b = tuple(child_a), tuple(child_b)
            children.extend([child_a, child_b])
        return children

    def survivor_selection(self, next_generation, current_generation):

        worst_x = set(heapq.nsmallest(
            self.survival_count, next_generation, key=self.fitness))

        to_remove = []
        for i, individual in enumerate(next_generation):
            if individual in worst_x:
                to_remove.append(i)
                worst_x.remove(individual)

        for i in reversed(to_remove):
            del next_generation[i]

        next_generation.extend(heapq.nlargest(
            self.survival_count, current_generation, key=self.fitness))
        return next_generation

    def parent_selection(self, individuals):
        fitnesses = np.array([self.fitness(individual)
                              for individual in individuals])
        selection_prob = fitnesses / fitnesses.sum()
        # Roulette wheel
        new_gen = [individuals[i] for i in np.random.choice(
            len(individuals), len(individuals), p=selection_prob)]
        return new_gen[:self.population_size]

    def best_of_population(self, population):
        best_individual = max(population, key=self.fitness)
        return self.fitness(best_individual), best_individual
