def round_iterables(nums):
    result = [round(el)for el in nums]
    return result


nums = map(lambda el: float(el), input().split())
print(round_iterables(nums))