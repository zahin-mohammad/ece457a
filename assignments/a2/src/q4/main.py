from state import State
import parsed_input
from annealing_schedule import make_trigonometric_schedule
from simulated_annealing import simulated_annealing

make_annealing_schedule = make_trigonometric_schedule(1000)
# Best so far: 2500, 1, 300 (int(T) was capped at 500) -> Final cost 1191
annealing_schedule = make_annealing_schedule(2500, 1, 300)

initial_state = State(6, parsed_input.locations,
                      parsed_input.D, parsed_input.S)


def cost_function(state: State):
    return state.get_cost()


def neighbor(state: State, T):
    return state.get_neighbor(min(500, int(T)))


print('INITIAL')
print(initial_state)

final_state = simulated_annealing(
    initial_state,
    cost_function,
    neighbor,
    annealing_schedule
)

print('FINAL')
print(final_state)
