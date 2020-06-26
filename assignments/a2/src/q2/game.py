import sys
from random_agent import *
from ai_agent import *

player1 = AIAgent('Player 1')
player2 = RandomAgent('Player 2')
MAX_PLAYS = 200

# Once minimax is confirmed to work as expected, come up with a better cost function that can play against retarded opponents


def run_game(debug=False):

    board = Board()
    if debug:
        print("Initial Board:")
        board.print()
        print()

    previous_player = None
    t = 0
    for _ in range(MAX_PLAYS):
        player = player1 if board.is_whites_turn() else player2

        prev_board = board
        board = player.make_a_move(board)

        # TODO: The serialize check is done due to a flaw in game ending logic - find it and FIX IT
        if board is None or board.serialize()[0] == prev_board.serialize()[0]:
            if debug:
                print(f'{previous_player.name} won!!!')
            break
        if debug:
            print(f'Play {t+1}:')
            board.print()
            print()

        previous_player = player
        t += 1
    if t == MAX_PLAYS and debug:
        print(f'Draw.')
    return t


num_plays = int(sys.argv[1]) if len(sys.argv) == 2 else 1

plays = [run_game(True) for i in range(num_plays)]

if num_plays > 1:
    print(f'Average Plays: {sum(plays)/len(plays)}')
    print(f'Average Rounds: {sum(plays)/len(plays)//2}')
