# Task: RGB Color Encoder
# Topic: Strings, hex conversion, formatting
# Source: Stepik Python course

# Input: three integers (R, G, B) from 0 to 255
# Output: color code in #RRGGBB format (uppercase hex)

r, g, b = int(input()), int(input()), int(input())

r_hex = hex(r)[2:].upper().rjust(2, '0')
g_hex = hex(g)[2:].upper().rjust(2, '0')
b_hex = hex(b)[2:].upper().rjust(2, '0')

print(f"#{r_hex}{g_hex}{b_hex}")