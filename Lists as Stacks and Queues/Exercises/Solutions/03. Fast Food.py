from collections import deque

quantity_food = int(input())
food = deque(input().split())

biggest_order = 0

for _ in range(len(food)):

    current_order = int(food.popleft())

    if current_order > biggest_order:
        biggest_order = current_order
    if current_order > quantity_food:
        food.appendleft(str(current_order))
        break
    else:
        quantity_food -= current_order

print(biggest_order)
if len(food) == 0:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(food)}")




