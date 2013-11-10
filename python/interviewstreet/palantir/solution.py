import sys

def main():
    size = int(sys.stdin.readline())
    matrix = []
    for _ in xrange(size):
        row = [int(x) for x in sys.stdin.readline().split()]
        matrix.append(row)
    basins = find_basins(size, matrix)
    print " ".join([str(x) for x in basins])

def find_basins(s, matrix):
    adjacent = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    lowest_neighbour_matrix = [[None]*s for _ in xrange(s)]
    # Find lowest neigbour of each cell
    for row in xrange(s):
        for col in xrange(s):
            lowest_neighbour = (row, col)
            lowest_neighbour_value = matrix[row][col]
            for dr, dc in adjacent:
                if row+dr >= s or row+dr < 0 or col+dc >=s or col+dc < 0:
                    continue
                # Strict < because unique (from problem)
                if matrix[row+dr][col+dc] < lowest_neighbour_value:
                    lowest_neighbour = (row+dr, col+dc)
                    lowest_neighbour_value = matrix[row+dr][col+dc]
            lowest_neighbour_matrix[row][col] = lowest_neighbour

    sink_map = {}
    basin_matrix = [[None]*s for _ in xrange(s)]

    def sink_of_cell(row, col):
        if not basin_matrix[row][col]:
            flow = (row, col)
            next_flow = lowest_neighbour_matrix[flow[0]][flow[1]]
            if flow == next_flow:
                # Found a new sink
                sink_map[flow] = 1
                basin_matrix[row][col] = flow
            else:
                # Follow until sink
                basin_matrix[row][col] = sink_of_cell(next_flow[0],next_flow[1])
                if basin_matrix[row][col] not in sink_map:
                    sink_map[basin_matrix[row][col]] = 1
                else:
                    sink_map[basin_matrix[row][col]] += 1

        return basin_matrix[row][col]

    for row in xrange(s):
        for col in xrange(s):
            sink_of_cell(row, col)

    return sorted(sink_map.values(), reverse=True)

main()
