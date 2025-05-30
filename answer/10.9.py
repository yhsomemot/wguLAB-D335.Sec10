user_input = input()
result = ''
for char in user_input:
    if char.isalpha():
        result += char
print(result)
