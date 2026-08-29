def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


def main():
    print("===== N-Queens Problem =====")

    try:
        n = int(input("Enter the number of queens: "))

        if n < 1:
            print("Please enter a positive number.")
            return

        board = [[0 for _ in range(n)] for _ in range(n)]

        if solve_n_queens(board, 0, n):
            print(f"\nSolution for {n}-Queens:\n")
            print_board(board)
        else:
            print(f"No solution exists for {n} queens.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()