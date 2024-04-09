# Print a List without the Commas and Brackets in Python

list_of_strings = ['bobby', 'hadz', '.com']

# ✅ Print a list of strings without commas, brackets and quotes
result = ''.join(list_of_strings)
print(result)  # 👉️ bobbyhadz.com

# ---------------------------------------------

# ✅ Print a list of integers without commas, brackets and quotes

list_of_integers = [7, 21, 44]

result = ''.join(str(item) for item in list_of_integers)
print(result)  # 👉️ 72144