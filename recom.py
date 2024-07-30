import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return "Tie"
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "O"
    ai = "X"
    current_player = human

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        if current_player == human:
            while True:
                row, col = map(int, input("Enter your move (row and column): ").split())
                if board[row][col] == " ":
                    board[row][col] = human
                    current_player = ai
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            row, col = best_move(board)
            board[row][col] = ai
            current_player = human

play_game()
