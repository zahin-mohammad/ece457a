# population_size = 50
# generation_count = 150
# p_c = 0.6
# mutation_probability = 0.25
import numpy as np
import heapq
from perffcn import q2_perfFNC

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
                 mutation_sigma=1.0,
                 survival_count=2):
        super().__init__()
        self.population_size = population_size
        self.generation_count = generation_count
        self.p_c = prob_crossover
        self.p_m = prob_mutation
        self.sigma = mutation_sigma
        self.survival_count = survival_count

    def init_population(self):
        pop = np.empty((0, 3), float)
        for i in range(self.population_size):
            genes = np.round(np.array([
                np.random.uniform(low=k_p_lower, high=k_p_upper),
                np.random.uniform(low=T_I_lower, high=T_I_upper),
                np.random.uniform(low=T_D_lower, high=T_D_upper)
            ]), 2)
            pop = np.append(pop, [genes], axis=0)
        return pop

    def fitness(self, individual):
        ISE, t_r, t_s, M_p = q2_perfFNC(*individual)
        return 1/ISE

    def mutation(self, individuals):
        for i, individual in enumerate(individuals):
            if np.random.uniform() <= (self.p_m):
                genes = np.round(np.array([
                    np.random.uniform(low=k_p_lower, high=k_p_upper),
                    np.random.uniform(low=T_I_lower, high=T_I_upper),
                    np.random.uniform(low=T_D_lower, high=T_D_upper)
                ]), 2)
                individuals[i] = genes
        return individuals

    def crossover(self, parents):
        children = np.empty((0, 3), float)
        np.random.shuffle(parents)

        # Uniform Crossover
        for i in range(1, parents.shape[0], 1):
            child_a, child_b = parents[i-1], parents[i]

            for i, gene in enumerate(child_a):
                if np.random.uniform() <= (1-self.p_c):
                    child_a[i], child_b[i] = child_b[i], child_a[i]

            children = np.append(children, [child_a], axis=0)
            children = np.append(children, [child_b], axis=0)
        return children

    def within_range(self, individual):
        if k_p_lower <= individual[0] <= k_p_upper and\
                T_I_lower <= individual[1] <= T_I_upper and\
                T_D_lower <= individual[2] <= T_D_upper:
            return True
        return False

    def survivor_selection(self, next_generation, best_of_current):
        for individual in best_of_current:
            next_generation = np.append(next_generation, [individual], axis=0)
        return next_generation

    def roulette_population(self, population, selection_prob):
        return population[np.random.choice(population.shape[0], p=selection_prob)]

    def parent_selection(self, individuals):
        scores = []
        to_remove = []
        max = 0
        for i, individual in enumerate(individuals):
            try:
                i_fitness = self.fitness(individual)
                scores.append((i, i_fitness))
                max += i_fitness
            except:
                to_remove.append(i)

        individuals = np.delete(individuals, to_remove, axis=0)
        scores.sort(reverse=True, key=lambda x: x[1])

        selection_prob = [score[1]/max for score in scores]
        new_population = np.empty((0, 3), float)

        # Spin roulette wheel until we get enough individuals
        while new_population.shape[0] < self.population_size and\
                new_population.shape[0] == individuals.shape[0]:
            parent = self.roulette_population(individuals, selection_prob)
            new_population = np.append(
                new_population, [parent], axis=0)

        best_survivors = [individuals[scores[i][0]]
                          for i in range(self.survival_count)]

        return new_population, best_survivors

    def best_of_population(self, population):

        heapq.nlargest(1, population, key=self.fitness)
