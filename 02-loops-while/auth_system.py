# Task: Password Authentication System
# Topic: while/else, walrus operator
# Source: Stepik Python course
# Note: User has 3 attempts to enter the correct password
#       while/else — else block runs only if loop was NOT interrupted by break

attempts = 3
password = input()

while attempts > 0:
    entry = input()

    if entry == password:
        print("You entered the correct password! Welcome!")
        break

    attempts -= 1
    print("Wrong password entered!")
    print(f"Attempts limit = {attempts}")

else:
    print("You have used all your attempts! Come back tomorrow")