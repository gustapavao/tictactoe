"""Jogo da velha"""
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]


def create_board():
    """Função para criar o tabuleiro"""
    for line in board:
        print("\n")
        for column in line:
            print(column, end='')
    print("\n")


def is_board_full() -> bool:
    """Função que checa se o tabuleiro está completamente preenchido"""
    if "_" not in board[0] and "_" not in board[1] and "_" not in board[2]:
        print("Board is Full. Game Over.")
        return True
    return False


def put_x(player1) -> None:
    """Função que coloca a peça x em um espaço escolhido pelo usuário"""
    position = input(f"{player1}(X) - Choose a position (Line,Column): ")
    if "," not in position or len(position) > 3:
        print("This position is invalid! You have lost your turn.")
        return
    try:
        line: int = int(position[0])
        column: int = int(position[-1])
    except (IndexError, ValueError):
        print("This position is invalid! You have lost your turn.")
        return
    try:
        if board[line - 1][column - 1] != "_":
            print("\nPosition already occupied! You have lost your turn.")
        else:
            board[line - 1][column - 1] = "X"
    except (IndexError, ValueError):
        print("This position is invalid! You have lost your turn.")


def put_o(player2) -> None:
    """Função que coloca a peça x em um espaço escolhido pelo usuário"""
    position = input(f"{player2}(O) - Choose a position (Line,Column): ")
    if "," not in position or len(position) > 3:
        print("This position is invalid! You have lost your turn.")
        return
    try:
        line: int = int(position[0])
        column: int = int(position[-1])
    except (IndexError, ValueError):
        print("This position is invalid! You have lost your turn.")
        return
    try:
        if board[line - 1][column - 1] != "_":
            print("\nPosition already occupied! You have lost your turn.")
        else:
            board[line - 1][column - 1] = "O"
    except (IndexError, ValueError):
        print("This position is invalid! You have lost your turn.")


def check_win():
    """Função que percorre o tabuleiro e verifica se já tem um vencedor"""
    # Check lines
    for line in board:
        if all(cell == "X" for cell in line):
            return "X"
        if all(cell == "O" for cell in line):
            return "O"
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return board[0][col]
    # Check diagonals
    if ((board[0][0] == board[1][1] == board[2][2] != "_") or
            (board[0][2] == board[1][1] == board[2][0] != "_")):
        return board[1][1]
    return None


def game():
    """Função que inicia o jogo da velha"""
    is_over: bool = False
    count = 0
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    while not is_over:
        create_board()
        if check_win() == "X":
            print(f"{player1} won!")
            is_over = True
            continue
        if check_win() == "O":
            print(f"{player2} won!")
            is_over = True
            continue
        if is_board_full():
            is_over = True
            continue
        if count % 2 == 0:
            put_x(player1)
        else:
            put_o(player2)
        count += 1


if __name__ == '__main__':
    game()
