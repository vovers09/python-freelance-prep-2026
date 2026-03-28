# Task: Game Health Simulation
# Topic: while loop, lists, break
# Source: Stepik Python course
# Note: Hero starts with 100 HP, enemies deal damage each turn
#       Track total hits survived and which hit was critical (highest damage)

health = 100
hits_survived = 0
damage_log = []

print(f"Health level: {health}")

while health > 0:
    damage = int(input())
    damage_log.append(damage)
    health -= damage

    if health <= 0:
        break

    print(f"Health level: {health}")
    hits_survived += 1

print("Game over.")
print(f"Total hits your character heroically survived = {hits_survived}")
print(f"Hit #{damage_log.index(max(damage_log)) + 1} was critical")