# String Methods — Practice Showcase
# Topic: Built-in string methods in Python
# Source: Stepik Python course

# Count occurrences of a letter (case-insensitive)
text = "Everywhere"
print(text.lower().count("e"))  # 4

# Check prefix and suffix
s = "translate russian to english"
print(s.startswith("translate") and s.endswith("english"))  # True

# Pad number with leading zeros (10 digits total)
number = "99"
print(number.zfill(10))  # 0000000099

# Center text in a field of 15 chars
name = "Connor"
print(name.center(15, '_'))  # _____Connor____

# Strip specific characters from both sides
dirty = "!!!World?????????"
print(dirty.strip('-_!?'))  # World

# Strip only from the left
print(dirty.lstrip('-_!?'))  # World?????????