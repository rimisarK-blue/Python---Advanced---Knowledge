
def read_matrix():
    size = int(input())
    matrix = []
    for rows_index in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def get_primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def det_sum_below_primary_diagonal(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if c <= r: # including main diagonal
          # if c < r: # excluding main diagonal
                the_sum += matrix[r][c]
    return the_sum


print(get_primary_diagonal_sum(read_matrix()))
#print(det_sum_below_primary_diagonal(read_matrix()))