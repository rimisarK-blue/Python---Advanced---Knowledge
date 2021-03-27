
start = int(input())
stop = int(input())

print([x for x in range(start, stop+1) if any(x % i == 0 for i in range(2, 11))])