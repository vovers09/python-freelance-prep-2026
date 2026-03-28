# Task: Maximum Tasks in a Programming Competition
# Topic: while loop, greedy logic
# Source: Stepik Python course
# Note: Competition lasts 240 minutes (20:00 to 00:00)
#       Task i takes 5*i minutes, travel to party takes k minutes
#
# Algorithm:
# 1. Try to solve tasks one by one in order
# 2. After each task check if there is still time to travel to the party
# 3. Stop when adding the next task would make Limak late

n, k = map(int, input().split())
tasks_done = 0
time_spent = 0

while tasks_done < n:
    next_task_time = (tasks_done + 1) * 5

    if time_spent + next_task_time + k > 240:
        break

    time_spent += next_task_time
    tasks_done += 1

print(tasks_done)