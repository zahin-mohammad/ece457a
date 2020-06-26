from board import *

board = Board()

print(board)

serialized_version = board.serialize()

print(serialized_version)

deserialized_board = Board(*serialized_version)

print(deserialized_board)
