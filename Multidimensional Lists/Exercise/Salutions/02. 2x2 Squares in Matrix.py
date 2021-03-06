
rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())

    return matrix


def check_element_equal(row, cal, mat):
    current_element = mat[row][cal]
    next_element = mat[row][cal+1]
    element_bottom = mat[row+1][cal]
    element_bottom_right = mat[row+1][cal+1]
    if current_element == next_element and next_element == element_bottom and element_bottom == element_bottom_right:
        return True


matrix = init_matrix()

counter = 0
for raw_index in range(rows-1):
    for col_index in range(cols-1):
        if check_element_equal(raw_index, col_index, matrix):
            counter += 1


print(counter)