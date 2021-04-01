
size = int(input())
matrix = [[int(x) for x in input().split(', ')]for i in range(size)]

first_diagonal = [str(matrix[i][i])for i in range(len(matrix))]
second_diagonal = [str(matrix[i][len(matrix)-1-i])for i in range(len(matrix))]

first_diagonal_sum = sum([int(num)for num in first_diagonal])
second_diagonal_sum = sum([int(num)for num in second_diagonal])

print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {first_diagonal_sum}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {second_diagonal_sum}")





