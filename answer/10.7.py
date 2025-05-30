
new_val = input()

var = new_val[0]
var2 = new_val[1:].count(var)

if var2 != 1:
    print(f'{var2} {var}\'s')
else:
    print(f'{var2} {var}')
