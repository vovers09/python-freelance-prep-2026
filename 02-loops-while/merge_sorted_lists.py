# Task: Merge Two Sorted Lists
# Topic: Two-pointer algorithm
# Source: Stepik Python course
# Note: Built-in sorting is not allowed — algorithm must merge manually
#
# Algorithm:
# 1. Start two pointers at the beginning of each list
# 2. Compare current elements, append the smaller one to result
# 3. Move the pointer of the list we just took from
# 4. When one list is exhausted, append the rest of the other

n, m = map(int, input().split())
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
result = []

left_1, left_2 = 0, 0

while left_1 < n and left_2 < m:
    if list_1[left_1] < list_2[left_2]:
        result.append(list_1[left_1])
        left_1 += 1
    else:
        result.append(list_2[left_2])
        left_2 += 1

while left_1 < n:
    result.append(list_1[left_1])
    left_1 += 1

while left_2 < m:
    result.append(list_2[left_2])
    left_2 += 1

print(result)