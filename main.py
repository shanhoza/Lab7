import heapq


def kbig(k, nums):
    return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(f'Вход: nums = {nums}, k = {k}')
print(kbig(k, nums))
