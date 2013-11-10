
import sys
import pprint


def main():
    for iterations, matrix in read_gol_data():
        m = solve_gol(iterations, matrix)
        pprint.pprint(m)


def read_gol_data():
    games = int(sys.stdin.readline().rstrip())
    instances = []
    for i in xrange(games):
        (rows, columns) = [int(x) for x in sys.stdin.readline().split()]
        iterations = int(sys.stdin.readline().rstrip())
        matrix = []
        for row in xrange(rows):
            matrix.append(sys.stdin.readline().split())
        instances.append((iterations, matrix))
    return instances


def solve_gol(iterations, matrix):
    adjacent = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    for i in xrange(iterations):
        next_matrix = [x[:] for x in matrix]
        for r in xrange(1, len(matrix)-1):
            for c in xrange(1, len(matrix[0])-1):
                bs = 0
                ws = 0
                for dr, dc in adjacent:
                    if matrix[r+dr][c+dc] == 'w':
                        ws += 1
                    else:
                        bs += 1
                # counting with self = don't change if equal surrounding
                next_matrix[r][c] = 'w' if ws > bs else 'b'
        matrix = next_matrix
    return matrix


if __name__ == '__main__':
    main()
