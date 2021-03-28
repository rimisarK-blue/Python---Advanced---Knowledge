
numbers = [int(num) for num in input().split(', ')]

positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 == 1]

result = {"Positive": positive, "Negative": negative, "Even": even, "Odd": odd}

for key, value in result.items():
    print(f"{key}: {', '.join([str(num)for num in value])}")
