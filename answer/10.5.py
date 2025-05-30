# isnumeric()
user_string = input()

output = user_string.isnumeric()
if output == True:
    print("Yes")
else:
    print("No")

#isdigit() single line
user_string = input()

print("Yes") if user_string.isdigit() else print("No")

# isalnum()
user_string = input()

if user_string.isalnum() == True:
    print('Yes')
else:
    print('No')
    
