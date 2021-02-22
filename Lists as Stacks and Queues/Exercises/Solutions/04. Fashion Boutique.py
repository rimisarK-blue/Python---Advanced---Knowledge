
box = list(map(int, input().split()))

capacity = int(input())

counter_rack = 1
current_capacity = capacity

while len(box) > 0:
    current_value = box.pop()

    if current_value <= current_capacity:
        current_capacity -= current_value

    else:
        counter_rack += 1
        current_capacity = capacity
        current_capacity -= current_value

print(counter_rack)