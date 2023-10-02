# This program is used to create a simple Tic Tac Toe game

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if player == "X":
            row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
        else:
            print("Computer's turn:")
            row, col = computer_move(board)

        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = player
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)

        if is_winner(board, player):
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player, computer = computer, player

if __name__ == "__main__":
    play_game()
