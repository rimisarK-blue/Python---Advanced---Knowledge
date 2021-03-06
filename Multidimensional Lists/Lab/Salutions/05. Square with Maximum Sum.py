
def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for rows_index in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def get_sum_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix_sum(matrix, submatrix_size):

    best_row_index = 0
    best_column_sum = 0
    best_sum = get_sum_submatrix(matrix, best_row_index, best_column_sum, sub_matrix_size)

    for row_index in range(len(matrix) - sub_matrix_size + 1):
        for col_index in range(len(matrix[row_index]) - sub_matrix_size + 1):
            current_sum = get_sum_submatrix(matrix, row_index, col_index, sub_matrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_sum = col_index
    return(best_row_index, best_column_sum)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_submatrix(matrix, row_index, col_index, size))


matrix = read_matrix()
sub_matrix_size = 2

coordinates = get_best_submatrix_sum(matrix, sub_matrix_size)
print_result(coordinates, sub_matrix_size)



