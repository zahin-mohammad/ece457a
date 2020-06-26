from typing import Any


MAX_DEPTH = 2


# TODO: Implement alpha/beta pruning

# cost, alpha[depth!=1], beta[depth!=1], node[depth=1]

def configure_minimax(evaluate, get_children):
    def minimax(root):
        def minimax_dfs(node, is_max, depth, alpha, beta):
            ''' Pseudo Code:
            get parent_alpha
            get parent_beta

            if is leaf node or max_depth:
                evaluate my cost
                evaluate alpha to return if i am max
                evaluate beta to return If i am min

                return cost, alpha, beta


            initialize my_cost to None
            initialize my_alpha to parent_alpha
            initialize my_beta to parent_beta

            get children

            for child in children:
                get child_cost 
                get child_alpha and child_beta

                if i am max node:
                    if child_alpha >= parent_beta:
                        my_cost = child_alpha
                        prune

                    my_cost = max of my_cost and child_cost
                    my_alpha = max of my_alpha or child_alpha

                else if i am min node:
                    if child_beta <= parent_alpha:
                        my_cost = child_beta
                        prune

                    my_cost = min of my_cost and child_cost
                    my_beta = min of my_beta or child_beta

            return my_cost, my_alpha, my_beta
            '''
            def is_leaf_node(n):
                return next(get_children(n), None) is None

            if depth == MAX_DEPTH or is_leaf_node(node):
                return evaluate(node)

            if is_max:
                value = float('-inf')
                for child in get_children(node):
                    value = max(value, minimax_dfs(
                        child, False, depth + 1, alpha, beta))
                    alpha = max(alpha, value)

                    if alpha >= beta:
                        break

                return value

            else:
                value = float('inf')
                for child in get_children(node):
                    value = min(value, minimax_dfs(
                        child, True, depth + 1, alpha, beta))
                    beta = min(beta, value)

                    if beta <= alpha:
                        break

                return value

        '''Pseudo Code for Root:

        initialize my_children to []
        initialize my_alpha to float('-inf')
        initialize my_beta to float('inf')

        get children

        for child in children:
            get child_cost, child_alpha, child_beta using minimax

            update my_alpha and my_beta

            append (child_cost, child)

        set max_child to max of children based on cost

        return max_child

        '''
        my_children_and_their_cost = []
        my_alpha = float('-inf')
        my_beta = float('inf')

        children = get_children(root)

        for child in children:
            child_cost = minimax_dfs(
                child, False, 1, my_alpha, my_beta)

            my_alpha = max(my_alpha, child_cost)

            my_children_and_their_cost.append((child_cost, child))

        return my_children_and_their_cost

    return minimax
