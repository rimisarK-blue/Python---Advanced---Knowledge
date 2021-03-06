rows, cols = [int(el) for el in input().split()]


def init_matrix(rows, cals):

    matrix = []

    for _ in range(rows):
        matrix.append(input().split())
    return matrix


def check_if_index_is_valid(index_row, index_col, rows, cols):
    if 0 <= index_row < rows and 0 <= index_col < cols:
        return True
    return False


def check_if_command_is_valid(command, cords, rows, cols):
    if len(cords) == 4 and command == 'swap':
        for index in range(0, len(cords), 2):
            if not check_if_index_is_valid(cords[index], cords[index +1], rows, cols):
                print("Invalid input!")
                return False
        return True
    else:
        print("Invalid input!")
    return False


def print_matrix(mat):
    for row_index in range(0 , len(mat)):
        for col_index in range(0, len(mat[row_index])):
            print(f"{mat[row_index][col_index]} ",end='')
        print()


matrix = init_matrix(rows, cols)

data = input()
while not data == 'END':
    splitted_data = data.split()
    try:
        command = splitted_data[0]
        coordinates = [int(el) for el in splitted_data[1:]]
    except:
        print("Invalid input!")

    if check_if_command_is_valid(command, coordinates, rows, cols):
        current_row = coordinates[0]
        current_col = coordinates[1]
        row_to_swap = coordinates[2]
        col_to_swap = coordinates[3]
        temp = matrix[current_row][current_col]
        matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
        matrix[row_to_swap][col_to_swap] = temp
        print_matrix(matrix)

    data = input()

