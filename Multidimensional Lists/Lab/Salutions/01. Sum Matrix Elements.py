def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for rows_count in range(rows_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()

matrix_sum = 0
for m in range(len(matrix)):
    row = matrix[m]

    for l in range(len(row)):
        matrix_sum += row[l]

print(matrix_sum)
print(matrix)