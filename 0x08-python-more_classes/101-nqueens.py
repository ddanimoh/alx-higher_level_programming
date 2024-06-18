#!/usr/bin/python3
import sys


def print_usage_and_exit(message, status):
    print(message)
    sys.exit(status)


def is_valid_board(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    def place_queens(row, board):
        if row == N:
            solutions.append(board[:])
        else:
            for col in range(N):
                if is_valid_board(board, row, col):
                    board[row] = col
                    place_queens(row + 1, board)

    solutions = []
    place_queens(0, [-1] * N)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)

    if N < 4:
        print_usage_and_exit("N must be at least 4", 1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
