
def read_matrix():
    rows_count = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(rows_count)]


matrix = read_matrix()
print([[x for x in row if x % 2 == 0]for row in matrix])