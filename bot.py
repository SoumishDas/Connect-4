import copy
import random
from game import *

class Connect4Bot:
    def __init__(self, game:Connect4Game):
        self.game = game
        self.player = game.players[1]  # Assuming player 'O' is the bot
        self.opponent = game.players[0]

    

    def get_best_move(self):
        #_, col = self.minimax(self.game, 3, float('-inf'), float('inf'), True)
        col = 0
        while True:
            col = random.randrange(0,self.game.cols)
            if self.game.is_valid_move(col):
                break
        return col
    def is_terminal_node(self):
        # Check if either player has won
        if self.game.check_self.game.winning_move(0) or self.game.check_self.game.winning_move(1):
            return True

        # Check if the board is full
        if self.game.is_board_full():
            return True

        return False

    def minimax(self,board, depth, alpha, beta, maximizingPlayer):
        valid_locations = [i for i in range(0,self.game.cols) if self.game.is_valid_move(i)]
        is_terminal = self.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.game.winning_move(AI_PIECE):
                    return (None, 100000000000000)
                elif self.game.winning_move(board, PLAYER_PIECE):
                    return (None, -10000000000000)
                else: # Game is over, no more valid moves
                    return (None, 0)
            else: # Depth is zero
                return (None, score_position(board, AI_PIECE))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
                new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else: # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def evaluate_board(self, game):
        score = 0
        # Evaluate horizontal
        for row in range(game.rows):
            for col in range(game.cols - 3):
                score += self.evaluate_window(game, row, col, row, col + 1, row, col + 2, row, col + 3)

        # Evaluate vertical
        for row in range(game.rows - 3):
            for col in range(game.cols):
                score += self.evaluate_window(game, row, col, row + 1, col, row + 2, col, row + 3, col)

        # Evaluate positive diagonal
        for row in range(game.rows - 3):
            for col in range(game.cols - 3):
                score += self.evaluate_window(game, row, col, row + 1, col + 1, row + 2, col + 2, row + 3, col + 3)

        # Evaluate negative diagonal
        for row in range(3, game.rows):
            for col in range(game.cols - 3):
                score += self.evaluate_window(game, row, col, row - 1, col + 1, row - 2, col + 2, row - 3, col + 3)

        return score

    def evaluate_window(self, game, *positions):
        bot_count = positions.count(self.player)
        opponent_count = positions.count(self.opponent)
        empty_count = positions.count(' ')
        if bot_count == 4:
            return 100
        elif bot_count == 3 and empty_count == 1:
            return 5
        elif bot_count == 2 and empty_count == 2:
            return 2
        elif opponent_count == 3 and empty_count == 1:
            return -5
        elif opponent_count == 2 and empty_count == 2:
            return -2
        else:
            return 0

    def get_empty_row(self, game, col):
        for row in range(game.rows - 1, -1, -1):
            if game.board[row][col] == ' ':
                return row
