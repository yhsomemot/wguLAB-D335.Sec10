#using multiple variables as one (and indexs)
names = input().split()

if len(names) == 3:
    first_name, middle_name, last_name = names
    print(f'{last_name}, {first_name[0]}.{middle_name[0]}.')
elif len(names) == 2:
    first_name, last_name = names
    print(f'{last_name}, {first_name[0]}.')
else:
    print("Invalid input")

#using indexs
user_input = input() # read name
name = user_input.split() # split name into separate words

if len(name) == 3: # if number of words in name is 3
    print(name[2] + ", " + name[0][0] + "." + name[1][0] + ".")

elif len(name) == 2: # if number of words in name is 2
    print(name[1] + ", " + name[0][0] + ".")
