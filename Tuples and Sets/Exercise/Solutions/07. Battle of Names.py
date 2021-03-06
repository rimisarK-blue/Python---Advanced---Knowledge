
n = int(input())
even_numbers = set()
odd_numbers = set()

for current_iteration in range(1, n+1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // current_iteration

    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)

sum_even = sum(even_numbers)
sum_odds = sum(odd_numbers)

if sum_even == sum_odds:
    modified_set = [str(el) for el in even_numbers.union(odd_numbers)]
    print(f"{', '.join(modified_set)}")
elif sum_odds > sum_even:
    modified_set = [str(el) for el in odd_numbers.difference(even_numbers)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in odd_numbers.symmetric_difference(even_numbers)]
    print(f"{', '.join(modified_set)}")



