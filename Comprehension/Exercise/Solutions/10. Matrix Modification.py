
num = int(input())

rows = num
cals = num
matrix = [(list(map(int, input().split())))for _ in range(rows)]

line = input()
while not line == 'END':
    command, row, cal, value = line.split()
    row = int(row)
    cal = int(cal)
    value = int(value)
    if 0 <= row <= rows -1 and 0 <= cal <= cals - 1:
        if command == 'Add':
            matrix[row][cal] += value
        elif command == 'Subtract':
            matrix[row][cal] -= value
    else:
        print("Invalid coordinates")
    line = input()

[print(*row, sep=' ')for row in matrix]