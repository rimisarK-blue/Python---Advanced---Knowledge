from itertools import combinations
names = input().split(', ')
n = int(input())
print(*[f"{', '.join(el)}"for el in list(combinations(names, n))], sep='\n')
# def calculate_combinations(names, n, combinations=[]):
#     if len(combinations) == n:
#         print(", ".join(combinations))
#         return
#
#     for i in range(len(names)):
#         name = names[i]
#         combinations.append(name)
#         calculate_combinations(names[i+1:], n , combinations)
#         combinations.pop()
#
#
# names = input().split(', ')
# n = int(input())
#
# calculate_combinations(names, n)