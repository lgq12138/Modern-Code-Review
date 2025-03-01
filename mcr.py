def is_win(game):
    win = False
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':  # Check Rows
            return True
        if game[0][i] == game[1][i] == game[2][i] != ' ':  # Check Columns
            return True
    if game[0][0] == game[1][1] == game[2][2] != ' ':  # Diagonal
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':  # Diagonal
        return True
    return False

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        valid_input = False
        while not valid_input:
            try:
                if  not turn:
                   print("Player 1: ", end="")
                else:
                   print("Player 2: ", end="")
                print("Which cell to mark? i:[1..3], j:[1..3]: ")
                i, j = map(int, input().split())
                if i < 1 or i > 3 or j < 1 or j > 3:  # Check if the input is within bounds
                    raise ValueError("Input out of bounds.")
                i -= 1
                j -= 1
                if game[i][j] != ' ':  # Check if the cell is already taken
                    raise ValueError("Cell already occupied.")
                if  not turn:
                    game[i][j] = player1
                else:
                    game[i][j] = player2
                valid_input = True
            except (ValueError, IndexError) as e:
                print(f"Invalid input: {e}. Please try again.")
        turn = not turn  # Switch turns
        # Show the game board
        for row in game:
            print(" ".join(row))
        if is_win(game) and game[i][j]==player2:
            print("Player 1 Win!")
            break  # Terminate the game
        if is_win(game) and game[i][j]==player2:
            print("Player 2 Win!")
            break  # Terminate the game
        if n == 8:  # All cells have been filled
            print("Tie!")

if __name__ == "__main__":
    main()
