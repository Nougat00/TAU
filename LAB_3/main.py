import random

def initialize_game():
    game_board = [['_' for _ in range(6)] for _ in range(6)]

    player_start = (0, 0)
    game_board[player_start[0]][player_start[1]] = 'P'

    target_position = (5, 5)
    game_board[target_position[0]][target_position[1]] = 'T'

    for _ in range(5):
        while True:
            row, col = random.randint(0, 5), random.randint(0, 5)
            if game_board[row][col] == '_':
                game_board[row][col] = 'X'
                break

    return game_board, player_start, target_position


def display_board(board):
    for board_row in board:
        print(' '.join(board_row))


def move_player(board, action, position, start, target):
    row, col = position
    moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    delta_row, delta_col = moves.get(action, (0, 0))

    new_row, new_col = row + delta_row, col + delta_col
    if 0 <= new_row < 6 and 0 <= new_col < 6 and board[new_row][new_col] != 'X':
        board[row][col] = '_'
        board[new_row][new_col] = 'P'
        return new_row, new_col
    return row, col


def play_game():
    game_board, player_position, target_position = initialize_game()
    while True:
        print("\n")
        display_board(game_board)
        action = input("\nMove (W, S, A, D, q to quit): \n --> ").lower()

        if action == 'q':
            break
        else:
            player_position = move_player(game_board, action, player_position, player_position, target_position)

        if player_position == target_position:
            game_board[target_position[0]][target_position[1]] = '#'
            display_board(game_board)
            print("You reached the target!")
            break;

if __name__ == "__main__":
    play_game()
