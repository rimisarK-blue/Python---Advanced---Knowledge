
num = int(input())
unique = []
for _ in range(num):
    name = input()
    if name in unique:
        continue
    else:
        unique.append(name)

for el in unique:
    print(el)
