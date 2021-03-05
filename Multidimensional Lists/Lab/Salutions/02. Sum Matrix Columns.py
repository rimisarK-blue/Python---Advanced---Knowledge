
def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for rows_index in range(rows_count):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def get_column_sums():
    row_count = len(matrix)
    columns_count = len(matrix[0])
    sums = []
    for column_index in range(columns_count):
        column_sum = 0
        for row_index in range(row_count):
            column_sum += matrix[row_index][column_index]
        sums.append(column_sum)
    return sums


def print_result(values):
    [print(x) for x in values]


matrix = read_matrix()
result = get_column_sums()
print_result(result)