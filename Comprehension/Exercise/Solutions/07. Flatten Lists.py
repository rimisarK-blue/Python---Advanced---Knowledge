
data = input().split('|')

data.reverse()

result = [el.strip() for i in range(len(data))for el in data[i].split()]

print(*result)