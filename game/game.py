
class TicTacToe:
    def __init__(self):
        self._board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]
        self.running = True
        self.turn = 0
        self.winner = ""

    def set_winner(self, value: str):
        self.winner = value

    def change_turn(self):
        """
        Change the actual Turn. There are two turns. Turn 0 -> Player 1 and Turn 1 -> Player 2
        :return:
        """
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0

    def is_board_full(self):
        """
        Check if it is still possible to make a move
        :return: True if all spaces are complete, False otherwise.
        """
        return any("_" in row for row in self._board)

    def check_line(self, line):
        """
        Check if all elements in a line are the same and not equal to "_".
        :param line: list
        :return: True if all elements in the line are the same and not equal to "_", False otherwise.
        """
        return all(elem == line[0] and elem != "_" for elem in line)

    def check_win(self):
        """
        Check if any of the players has won.
        :return: Tuple (Boolean, String) representing if there's a win and the winning player's symbol.
        """
        # Check rows and columns
        for i in range(3):
            if self.check_line(self._board[i]) or self.check_line([self._board[j][i] for j in range(3)]):
                return True, self._board[i][i]

        # Check diagonals
        if (self.check_line([self._board[i][i] for i in range(3)]) or
                self.check_line([self._board[i][2 - i] for i in range(3)])):
            return True, self._board[1][1]

        return False, None

    def announce_winner(self):
        """
        Check if there is a winner and announce the result
        :return: Winner or Draw
        """
        if self.winner == "Draw":
            return "It is a draw"
        else:
            return f"{self.winner} Win"

    def moviment(self, position: list):
        """
        Places X or O, depending on what the player chose previously, at the given position.
        :param position: List with two values, row and column, respectively.
        :return:
        """
        mark = "X" if self.turn == 0 else "O"
        if self._board[position[0]][position[1]] != "_":
            return "Position already occupied! You have lost your turn."
        else:
            self._board[position[0]][position[1]] = mark

    def run_game(self):
        """
        Run the game
        :return:
        """
        while self.running:
            if self.check_win()[0]:
                self.running = False
                self.set_winner(self.check_win()[1])
                break
            if self.is_board_full():
                self.running = False
                self.set_winner("Draw")
                break
            if self.turn == 0:
                self.moviment(list())  # preciso tirar daqui e passar como parametro um valor que vou pegar do flet
                self.change_turn()
            elif self.turn == 1:
                self.moviment(list())
                self.change_turn()


