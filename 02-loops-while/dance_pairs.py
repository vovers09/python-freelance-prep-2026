# Task: Maximum Dance Pairs at a Ball
# Topic: Greedy algorithm + two pointers
# Source: Stepik Python course
# Note: A pair is valid if the difference in dance skill is at most 1
#
# Algorithm:
# 1. Sort both lists
# 2. Start two pointers at the end of each list (best dancers first)
# 3. If current pair is valid — count it, move both pointers
# 4. If not — move the pointer of the higher-skilled dancer

n = int(input())
list_men = list(map(int, input().split()))

m = int(input())
list_women = list(map(int, input().split()))

list_men.sort()
list_women.sort()

right_men = n - 1
right_women = m - 1
pairs = 0

while right_men >= 0 and right_women >= 0:
    if abs(list_men[right_men] - list_women[right_women]) <= 1:
        pairs += 1
        right_men -= 1
        right_women -= 1
    elif list_men[right_men] > list_women[right_women]:
        right_men -= 1
    else:
        right_women -= 1

print(pairs)