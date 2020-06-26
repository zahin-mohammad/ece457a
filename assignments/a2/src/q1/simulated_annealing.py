from random import random
from math import exp
from easom import f, INTERVAL


def simulated_annealing(
    start_state,
    cost_function,
    neighbor,
    annealing_schedule,
    prob_of_acceptance=lambda delta_cost, T: exp(-delta_cost/T)
):
    state = start_state

    states = []
    costs = []

    time_steps = 0
    initial_temp = None
    for T in annealing_schedule:
        initial_temp = T if initial_temp is None else initial_temp
        cost = cost_function(state)

        states.append(state)
        costs.append(cost)

        new_state = neighbor(state, T, initial_temp)
        new_cost = cost_function(new_state)

        cost_diff = new_cost - cost

        if cost_diff <= 0:
            state = new_state
        else:
            prob = prob_of_acceptance(cost_diff, T)

            if prob > random():
                state = new_state

        time_steps += 1

    return state, states, costs


def compute_error(final_cost):
    return f'{100*(-abs(final_cost - -1.0)/-1.0)}%'


def perform_annealing_and_print(start_state, make_schedule, T_i, T_f, iter_per_T, *args):
    final_state, states, costs = simulated_annealing(
        start_state,
        *args,
        make_schedule(T_i, T_f, iter_per_T)
    )

    print(f'Start State: {start_state}')
    print(f'Start Temp: {T_i}')
    print(f'Final State: {final_state}')
    print(f'Final Temp: {T_f}')
    print(f'Iterations per T: {iter_per_T}')
    print(f'f(final_state): {f(final_state)}')
    print(f'Error from ideal value: {compute_error(f(final_state))}')
    print()

    return states, costs
