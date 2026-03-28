# Task: Years Until Limak Outweighs Bob
# Topic: while loop, simulation
# Source: Stepik Python course
# Note: Limak's weight triples each year, Bob's weight doubles
#       Find the first year when Limak strictly outweighs Bob

limak, bob = map(int, input().split())
years = 0

while limak <= bob:
    limak *= 3
    bob *= 2
    years += 1

print(years)