from random import randint

class Board:
    def __init__(self, dim, nSub):
        self.dim = dim
        self.board = [[0 for _ in range(dim)] for _ in range(dim)]

        for _ in range(nSub):
            x = randint(0, dim - 1)
            y = randint(0, dim - 1)
            self.board[x][y] = 1

    def __str__(self):
        size = self.dim
        board_str = ""

        for i in range(size):
            board_str += "+---" * size + "+\n"  # Top border of each cell row
            board_str += "| "
            for j in range(size):
                if self.board[i][j] == 0:
                    board_str += "  | "
                else:
                    board_str += "X | "  # Assuming X for cells with value 1

            board_str += "\n"
        board_str += "+---" * size + "+\n"  # Bottom border of the last row

        return board_str

# Example usage:
if __name__ == "__main__":
    dim = 5
    nSub = 10
    game_board = Board(dim, nSub)
    print(game_board)

            