N = int(input("enter the number of queens:"))
board = [[0] * N for _ in range(N)]


def is_attack(i, j):
    # Check for row and column attacks
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Check for diagonal attacks (main diagonal)
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def N_queen(n):
    # Base case: if all queens are placed, return True
    if n == 0:
        return True

    # Try to place a queen in each row of column n-1
    for i in range(0, N):
        for j in range(0, N):
            if board[i][j] == 0 and not is_attack(i, j):  # Check if the cell is safe
                board[i][j] = 1  # Place the queen

                # Recurse for the next queen (decrement n to place the next queen)
                if N_queen(n - 1):
                    return True

                # If placing the queen didn't lead to a solution, backtrack
                board[i][j] = 0

    return False  # Return False if no solution is found


# Solve the N-Queens problem
if N_queen(N):
    for row in board:
        print(row)
else:
    print("No solution exists")
