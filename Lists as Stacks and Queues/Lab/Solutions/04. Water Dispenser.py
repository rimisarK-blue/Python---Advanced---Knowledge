from collections import deque

total_amount = int(input())

people = deque()

while True:
    command = input()
    if command == 'Start':
        break
    people.append(command)

while True:
    command = input()
    if command == 'End':
        print(f'{total_amount} liters left')
        break
    if command.startswith('refill'):
        data = command.split()
        liters = int(data[1])
        total_amount += liters
    else:
        person = people.popleft()
        person_liters = int(command)
        if person_liters <= total_amount:
            total_amount -= person_liters
            print(f'{person} got water')
        else:
            print(f"{person} must wait")





