# While Loops — Practice Showcase
# Topic: while loop basics — iteration, counters, break, continue
# Source: Stepik Python course

# ── 1. Print all even numbers from 1000 to 2000 ──────────────────────────────
num = 1000
while num <= 2000:
    print(num)
    num += 2

# ── 2. Print multiples of 5 from 6785 down to 195 ────────────────────────────
num = 6785
while num >= 195:
    print(num)
    num -= 5

# ── 3. Countdown from N to 0 ─────────────────────────────────────────────────
n = int(input())
print("Countdown starts")
while n >= 0:
    print(n)
    n -= 1
print("Launch!")

# ── 4. Perfect squares up to N ───────────────────────────────────────────────
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1

# ── 5. Days until athlete runs at least Y km (15% increase per day) ──────────
x, y = map(int, input().split())
days = 1
while x < y:
    x *= 1.15
    days += 1
print(days)

# ── 6. Skip numbers divisible by 2 or 3, stop at multiples of 777 ────────────
a, b = int(input()), int(input())
while a <= b:
    if a % 777 == 0:
        break
    if a % 2 != 0 and a % 3 != 0:
        print(a)
    a += 1

# ── 7. Print each character with its index (forward) ─────────────────────────
word = input()
index = 0
while index < len(word):
    print(f"{word[index]} {index}")
    index += 1

# ── 8. Print each character with its index (reverse) ─────────────────────────
word = input()
index = len(word) - 1
while index >= 0:
    print(f"{word[index]} {index}")
    index -= 1