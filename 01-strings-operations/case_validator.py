# Task: Check if a string consists entirely of uppercase letters
# Topic: String methods — isupper(), isalpha()
# Source: Stepik Python course
# Note: isupper() alone returns True for "ABC123" — isalpha() ensures letters only

text = input()

print(text.isupper() and text.isalpha())