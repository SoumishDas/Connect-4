import copy
class Connect4Game:
    rows = 0
    cols = 0
    isdone = False
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.players = ['X', 'O']
        
    def copy(self):
        return copy.deepcopy(self)
    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == ' '

    def winning_move(self,player):
        for col in range(0,self.cols-1):
            if (self.is_valid_move(col) == False):
                continue
            row = self.get_empty_row(col)
            print(f"Row:{row} Col{col} win:{self.check_winning_move(row,col,player)}")
            if self.check_winning_move(row,col,player):
                
                return True
        return False

    def get_empty_row(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                return row
        return None  # Column is full

    

    def make_move(self, col,player):
        row = self.get_empty_row(col)
        if row is not None:
            self.board[row][col] = self.players[player]
            if self.check_winning_move(row, col,player):
                print("WIN")
            

        
    def check_winning_move(self,row, col,player):
        temp = self.board[row][col]
        self.board[row][col] = self.players[player]
        # Check horizontally
        count = 1
        for c in range(col - 1, -1, -1):
            if self.board[row][c] == self.board[row][col] == self.players[player]:
                count += 1
            else:
                break
        for c in range(col + 1, self.cols):
            if self.board[row][c] == self.board[row][col] == self.players[player]:
                count += 1
            else:
                break
        if count >= 4:
            self.board[row][col] = temp
            return True

        # Check vertically
        count = 1
        for r in range(row - 1, -1, -1):
            if self.board[r][col] == self.board[row][col] == self.players[player]:
                count += 1
            else:
                break
        for r in range(row + 1, self.rows):
            if self.board[r][col] == self.board[row][col] == self.players[player]:
                count += 1
            else:
                break
        if count >= 4:
            self.board[row][col] = temp
            return True

        # Check diagonally (bottom-left to top-right)
        count = 1
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0 and self.board[r][c] == self.board[row][col] == self.players[player]:
            count += 1
            r -= 1
            c -= 1
        r, c = row + 1, col + 1
        while r < self.rows and c < self.cols and self.board[r][c] == self.board[row][col] == self.players[player]:
            count += 1
            r += 1
            c += 1
        if count >= 4:
            self.board[row][col] = temp
            return True

        # Check diagonally (top-left to bottom-right)
        count = 1
        r, c = row + 1, col - 1
        while r < self.rows and c >= 0 and self.board[r][c] == self.board[row][col] == self.players[player]:
            count += 1
            r += 1
            
            c -= 1
        r, c = row - 1, col + 1
        while r >= 0 and c < self.cols and self.board[r][c] == self.board[row][col] == self.players[player]:
            count += 1
            r -= 1
            c += 1
        if count >= 4:
            self.board[row][col] = temp
            return True
        
        self.board[row][col] = temp
        return False

    

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)


