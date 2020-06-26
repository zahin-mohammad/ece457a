from collections import deque
import numpy as np

# Use a deque if required


def configure_tabu_search(
    stopping_condition,
    get_neighbors,
    evaluate,
    max_tabu_size=10
):
    def tabu_search(s_0):
        s_best = s_0
        best_score = evaluate(s_0)
        current_solution = s_0
        s_freq = {}
        # TODO: Combine with set for O(1) pop, add, lookup
        tabu_list = deque([s_0])

        def choose_random_top_candidate(candidates):
            if len(candidates) == 0:
                return None

            top_val = max(map(lambda n: evaluate(
                n, s_freq.setdefault(n, 0)), candidates))

            top_candidates = [n for n in candidates if evaluate(
                n, s_freq.setdefault(n, 0)) == top_val]

            return np.random.choice(np.array(top_candidates))

        while not stopping_condition():
            # Increase freq penalty
            s_freq[current_solution] = s_freq.setdefault(
                current_solution, -1) + 1

            s_neighborhood = list(get_neighbors(current_solution))

            if len(s_neighborhood) == 0:
                break

            possibly_tabu_top_candidate = choose_random_top_candidate(
                s_neighborhood)

            s_neighborhood_minus_tabu_list = list(
                filter(lambda n: n not in tabu_list, s_neighborhood))
            non_tabu_top_candidate = choose_random_top_candidate(
                s_neighborhood_minus_tabu_list)

            possibly_tabu_top_score = evaluate(possibly_tabu_top_candidate)
            non_tabu_top_score = evaluate(non_tabu_top_candidate)

            # Aspiration Criterion: Promote to non-tabu if the score sufficiently high
            if possibly_tabu_top_score > max(best_score, non_tabu_top_score):
                non_tabu_top_score = possibly_tabu_top_score
                non_tabu_top_candidate = possibly_tabu_top_candidate

            elif non_tabu_top_candidate is None:
                # If all neighbors are tabu and NONE of them are better states than best_state, then end the search
                break

            if non_tabu_top_score >= best_score:
                s_best = non_tabu_top_candidate
                best_score = non_tabu_top_score

            tabu_list.append(non_tabu_top_candidate)

            if len(tabu_list) > max_tabu_size:
                tabu_list.popleft()

            current_solution = non_tabu_top_candidate
        return s_best

    return tabu_search
