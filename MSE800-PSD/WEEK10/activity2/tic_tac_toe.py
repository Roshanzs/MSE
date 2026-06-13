
"""Tic Tac Toe Game
This is a simple implementation of the classic Tic Tac Toe game for two players."""
def print_board(board):
    """print the current state of the board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """check if the current player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

def is_board_full(board):
    """check if the board is full"""
    return all(cell in ['X', 'O'] for cell in board)

def play_game():
    """main function to play the game"""
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    print("--- Welcome to Tic Tac Toe! ---")
    print("Enter a number 1-9 to select the position where you want to place your mark:")
    while True:
        print_board(board)
        # Get player input and validate
        try:
            move = int(input(f"Player {current_player}, please enter a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] in ['X', 'O']:
                print("❌ Invalid position, please try again!")
                continue
        except ValueError:
            print("❌ Please enter a number between 1 and 9!")
            continue
        # Place the mark
        board[move] = current_player
        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Congratulations! Player {current_player} has won!")
            break
        # Check if the board is full (tie game)
        if is_board_full(board):
            print_board(board)
            print("🤝 It's a tie! You are both equally skilled!")
            break
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
    