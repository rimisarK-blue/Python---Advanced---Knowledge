
data = input().split(', ')

result = [f"{name} -> {len(name)}"for name in data]

print(', '.join(result))