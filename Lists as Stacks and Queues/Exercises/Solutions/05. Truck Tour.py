from collections import deque
num = int(input())
station = deque([])


for _ in range(num):
    station.append(input().split())

for big_circle in range(num):
    gas_tank = 0
    is_valid = True
    for small_circle in range(num):
        gas_tank += int(station[small_circle][0]) - int(station[small_circle][1])

        if gas_tank < 0:
            is_valid = False
            station.append(station.popleft())
            break

    if is_valid:
        print(big_circle)
        break


