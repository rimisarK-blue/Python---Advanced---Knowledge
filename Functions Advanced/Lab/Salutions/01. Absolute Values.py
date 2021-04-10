def convert_iterable_to_absolute(nums):
    result = [abs(el)for el in nums]
    return result


nums = [float(el) for el in input().split()]
print(convert_iterable_to_absolute(nums))
