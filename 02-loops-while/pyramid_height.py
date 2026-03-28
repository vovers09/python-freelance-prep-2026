# Task: Maximum Pyramid Height
# Topic: while loop, accumulative sum
# Source: Stepik Python course
# Note: Level i requires 1+2+...+i cubes (triangular number)
#       Total cubes used grows as sum of triangular numbers
#
# Algorithm:
# 1. Track cubes used per level and total cubes used
# 2. Each iteration add one more level
# 3. Stop when there are not enough cubes for the next level

n = int(input())
height = 0
cubes_per_level = 0
total_used = 0

while True:
    cubes_per_level += height + 1
    if total_used + cubes_per_level > n:
        break
    total_used += cubes_per_level
    height += 1

print(height)