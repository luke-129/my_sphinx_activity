import src.tic_tac_toe as toe


def main():
    current_player = 'X'
    moves = 0
    results = 0

    while moves < 9:
        toe.print_board()

        # Note that list comprehensions are more Pythonic, easier to read, and in recent versions of Python, faster.
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
        if toe.board[row][col] == ' ':
            toe.board[row][col] = current_player
            win = toe.is_win(current_player)

            if win:
                results += 1
                toe.print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'  # Switch player
            moves += 1
        else:
            print("Cell already occupied! Try again.")
    toe.print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {toe.tally_wins(results)}")


if __name__ == "__main__":
    main()
