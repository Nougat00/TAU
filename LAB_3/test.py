import unittest
from unittest.mock import patch
from main import initialize_game, move_player

class TestModifiedGame(unittest.TestCase):

    def test_game_initialization(self):
        game_board, player_start, target_position = initialize_game()
        self.assertEqual(len(game_board), 6)
        self.assertEqual(player_start, (0, 0))
        self.assertEqual(target_position, (5, 5))

    def test_player_movement(self):
        game_board, player_position, _ = initialize_game()
        game_board[1][0] =  '_'
        current_row, current_col = move_player(game_board, 's', player_position, player_position, (5, 5))
        self.assertNotEqual(player_position[0], current_row)
        self.assertEqual(player_position[1], current_col)

    def test_reaching_the_target(self):
        game_board, _, target_position = initialize_game()
        game_board[5][4] =  '_'
        current_row, current_col = move_player(game_board, 's', (4, 4), (4, 4), target_position)
        self.assertEqual(current_row, 5)
        self.assertEqual(current_col, 4)

    def test_avoiding_obstacle(self):
        game_board, player_position, _ = initialize_game()
        game_board[0][1] = 'X'
        current_row, current_col = move_player(game_board, 'd', player_position, player_position, (5, 5))
        self.assertEqual(current_row, player_position[0])
        self.assertEqual(current_col, player_position[1])

    def test_attempt_to_move_out_of_bounds(self):
        game_board, _, target_position = initialize_game()
        current_row, current_col = move_player(game_board, 's', (5, 5), (5, 5), target_position)
        self.assertEqual(current_row, 5)
        self.assertEqual(current_col, 5)

    def test_obstacle_count(self):
        game_board, _, _ = initialize_game()
        obstacle_count = sum(row.count('X') for row in game_board)
        self.assertEqual(obstacle_count, 5, "Liczba przeszkód na planszy powinna być równa 5")

    @patch('builtins.input', return_value='x')
    def test_invalid_input(self, mock_input):
        game_board, player_start, _ = initialize_game()
        new_row, new_col = move_player(game_board, 'x', player_start, player_start, (5, 5))
        self.assertEqual(player_start[0], new_row)
        self.assertEqual(player_start[1], new_col)

if __name__ == "__main__":
    unittest.main()
