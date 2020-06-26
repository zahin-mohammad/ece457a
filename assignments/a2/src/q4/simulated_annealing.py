from random import random
from math import exp


def simulated_annealing(
    start_state,
    cost_function,
    neighbor,
    annealing_schedule,
    prob_of_acceptance=lambda delta_cost, T: exp(-delta_cost/T)
):
    state = start_state

    initial_temp = None
    for T in annealing_schedule:
        initial_temp = T if initial_temp is None else initial_temp

        cost = cost_function(state)

        new_state = neighbor(state, T)
        new_cost = cost_function(new_state)

        cost_diff = new_cost - cost

        if cost_diff <= 0:
            state = new_state
        else:
            prob = prob_of_acceptance(cost_diff, T)

            if prob > random():
                state = new_state

    return state
