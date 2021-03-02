
set1, set2 = map(int, input().split())

nums1 = []
num2 = []
for _ in range(set1):
    number = input()
    nums1.append(number)

for _ in range(set2):
    number = input()
    if number in nums1:
        num2.append(number)

unique = set(num2)
unique_nums = []
for num in unique:
    unique_nums.append(num)
for el in unique_nums:
    print(el)





