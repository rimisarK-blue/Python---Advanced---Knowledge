
num = int(input())

unique = []
for _ in range(num):
    elements = input()
    if len(elements) > 2:
        separated = elements.split()
        for el in separated:
            if el not in unique:
                unique.append(el)
    else:
        if elements not in unique:
            unique.append(elements)

for el in unique:
    print(el)


