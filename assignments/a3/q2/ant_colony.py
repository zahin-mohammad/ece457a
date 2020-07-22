
import pprint
from typing import Callable, Tuple
from ant import Ant
import numpy as np
import sys
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)

coordinates = [
    [1150, 1760],
    [630, 1660],
    [40, 2090],
    [750, 1100],
    [750, 2030],
    [1030, 2070],
    [1650, 650],
    [1490, 1630],
    [790, 2260],
    [710, 1310],
    [840, 550],
    [1170, 2300],
    [970, 1340],
    [510, 700],
    [750, 900],
    [1280, 1200],
    [230, 590],
    [460, 860],
    [1040, 950],
    [590, 1390],
    [830, 1770],
    [490, 500],
    [1840, 1240],
    [1260, 1500],
    [1280, 790],
    [490, 2130],
    [1460, 1420],
    [1260, 1910],
    [360, 1980]
]


def online_simulation(
    init_pheromone,              # f() -> {(Int,Int)->Int}
    init_ants,                   # f() -> [Ant]
    termination_condition,       # generator
    state_transition,       # f(Ant)
    online_pheromone_update,     # f(Ant, {(Int,Int)->Int}) -> {(Int,Int)->Int}
    offline_pheromone_update,
    get_best_solution,           # f([Ant], [])
    # f([Ant], {(Int,Int)->Int}) -> {(Int,Int)->Int}

    is_online,                   # boolean,
):
    pheromones = init_pheromone()

    best_solutions = []
    for x in termination_condition():
        best_solution = None
        ants = init_ants()
        all_ants_have_solution = False

        while not all_ants_have_solution:
            all_ants_have_solution = True

            for i in range(len(ants)):
                if not ants[i].ant_has_solution():
                    all_ants_have_solution = False

                    ants[i] = state_transition(ants[i], pheromones)

                    if is_online:
                        pheromones = online_pheromone_update(
                            ants[i], pheromones)

        for i in range(len(ants)):
            ants[i].loop_back()
        best_solution = get_best_solution(ants, best_solution)
        best_solutions.append(best_solution)

        pheromones = offline_pheromone_update(ants, pheromones)
    return best_solutions


def init_pheromone() -> dict:  # return: map of coord -> pheromone
    pheromones = dict()
    # i < k for all keys
    for i in range(len(coordinates)):
        for k in range(i+1, len(coordinates)):
            pheromones[(i, k)] = 1
    return pheromones


def init_ants(m: int) -> Callable[[], list]:
    def f():
        return [Ant() for i in range(m)]
    return f


def termination_condition(iteration_count: int) -> Callable[[], int]:
    def f():
        for i in range(iteration_count):
            yield i
    return f


def get_best_solution(ants: list, global_best_ant: Ant) -> Ant:
    local_best_ant = min(ants, key=lambda x: x.solution_length)
    return local_best_ant if global_best_ant is None or local_best_ant.solution_length < global_best_ant.solution_length else global_best_ant

######################################################################################


def state_transition(alpha: float, beta: float, q0: float):
    def f(ant: Ant, pheromones: dict) -> Ant:
        neighbors = ant.get_neighbors()
        transition_arr = [(ant.solution_path[-1], i) for i in neighbors]

        for index in range(len(transition_arr)):
            i, j = transition_arr[index]
            if i > j:
                transition_arr[index] = (j, i)

        next_neighbor = None
        distances = np.array(list(map(ant.get_distance, transition_arr)))
        heuristic = distances ** -beta
        if np.random.uniform() < q0:
            max_pheromone = 0
            next_neighbor = np.argmax(
                np.array([pheromones[coord] for coord in transition_arr]) * heuristic)
        else:
            taos = np.array([pheromones[coord] for coord in transition_arr])
            probabilities = ((taos ** alpha)*heuristic) / \
                ((taos ** alpha)*heuristic).sum()
            next_neighbor = np.random.choice(
                len(transition_arr), p=probabilities)

        ant.add_node(transition_arr[next_neighbor])
        return ant
    return f


######################################################################################

def offline_pheromone_update(rho: float = 0.3) -> Callable[[list, dict], dict]:
    def fitness_ant(ant: Ant) -> float:
        return ant.solution_length

    def f(ants: Ant, pheromones: dict) -> dict:
        best_ant = min(ants, key=fitness_ant)
        for key, value in pheromones.items():
            new_pheromone = (1-rho)*value
            i, j = key
            if i in best_ant.tabu or j in best_ant.tabu:
                new_pheromone += rho*(1/best_ant.solution_length)
            pheromones[key] = new_pheromone
        return pheromones

    return f


def online_pheromone_update(rho: float = 0.3) -> Callable[[Ant, dict], dict]:
    def f(ant, pheromones):
        i, j = ant.solution_path[-2], ant.solution_path[-1]
        if i > j:
            i, j = j, i
        pheromones[(i, j)] = (1-rho)*pheromones[(i, j)] + \
            1.0/ant.get_distance((i, j))
        return pheromones
    return f


def graph(title, data):
    print(data)
    for series in data:
        x = range(1, len(series[1])+1)
        y = series[1]
        plt.plot(x, y, label=series[0])

    plt.xlabel('Iterations')
    plt.ylabel('Best Solution')
    plt.title(title)
    plt.legend()

    plt.savefig(title, dpi=500)


if __name__ == "__main__":
    m = [100]*10
    iteration_count = [100]*10
    alpha = [2]*10
    beta = [2]*10
    q0 = [0.7]*10
    rho1 = [0.3]*10
    rho2 = [0.3]*10
    is_online = True
    labels = []
    title = ""

    if sys.argv[1] == '0':
        title = "Solution with changes in Rho1 (Offline)"
        rho1 = [i * 0.3 for i in range(3)]
        labels = [f'rho1: {rho1[i]}' for i in range(3)]

    if sys.argv[1] == '1':
        title = "Solution with changes in Rho2 (Online)"
        rho2 = [i * 0.3 for i in range(3)]
        labels = [f'rho1: {rho2[i]}' for i in range(3)]

    if sys.argv[1] == '2':
        title = "Solution with changes in alpha"
        alpha = [i + 1 for i in range(3)]
        labels = [f'alpha: {alpha[i]}' for i in range(3)]

    if sys.argv[1] == '3':
        title = "Solution with changes in beta"
        beta = [i + 1 for i in range(3)]
        labels = [f'beta: {beta[i]}' for i in range(3)]

    if sys.argv[1] == '4':
        title = "Solution with changes in population size"
        m = [(i + 1)*50 for i in range(3)]
        labels = [f'beta: {m[i]}' for i in range(3)]

    if sys.argv[1] == '5':
        title = "Solution with changes in Rho1 (Offline) with no online update"
        is_online = False
        rho1 = [i * 0.3 for i in range(3)]
        labels = [f'rho1: {rho1[i]}' for i in range(3)]

    if sys.argv[1] == '6':
        title = "Solution with changes in alpha with no online update"
        is_online = False
        alpha = [i + 1 for i in range(3)]
        labels = [f'alpha: {alpha[i]}' for i in range(3)]

    if sys.argv[1] == '7':
        title = "Solution with changes in beta with no online update"
        is_online = False
        beta = [i + 1 for i in range(3)]
        labels = [f'beta: {beta[i]}' for i in range(3)]

    if sys.argv[1] == '8':
        title = "Solution with changes in population size  with no online update"
        is_online = False
        m = [(i + 1)*50 for i in range(3)]
        labels = [f'beta: {m[i]}' for i in range(3)]

    if sys.argv[1] == '9':
        title = "Solution with changes in Rho1 (Offline) with no online update"
        is_online = False
        rho1 = [i * 0.3 for i in range(3)]
        labels = [f'rho1: {rho1[i]}' for i in range(3)]

    data = []
    for i in range(3):
        print(f'Doing: {labels[i]}')
        best_solutions = online_simulation(
            init_pheromone,
            init_ants(
                m=m[i]),
            termination_condition(
                iteration_count=iteration_count[i]),
            state_transition(
                alpha=alpha[i],
                beta=beta[i],
                q0=q0[i]),
            online_pheromone_update(
                rho=rho2[i]),
            offline_pheromone_update(
                rho=rho1[i]),
            get_best_solution,
            is_online
        )
        data.append(
            (labels[i], [ant.solution_length for ant in best_solutions]))
    graph(title, data)
