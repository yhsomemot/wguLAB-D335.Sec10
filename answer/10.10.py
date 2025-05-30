# TASK 1 Complete the function to print the first X number of characters in the given string

def printFirst(mystring, x):
    print(mystring[:x])
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)

# TASK 2 Complete the function to return the last X number of characters in the given string

def getLast(mystring, x):
  return mystring[-x:]
 
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))

# TASK 3 Complete the function to return True if the word WGU exists in the given string otherwise return False

def containsWGU(mystring):
    if 'WGU' in mystring:
        return True
    else:
        return False
    
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))

# TASK 4 Complete the function to print all of the words in the given string

def printWords(mystring):
    print(mystring.split())
    
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')

# TASK 5 Complete the function to combine the words into a sentence and return a string

def combineWords(words):
    return ' '.join(words)
    
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))

# TASK 6 Complete the function to replace the word WGU with Western Governors University and print the new string

def replaceWGU(mystring):
    print(mystring.replace('WGU', 'Western Governors University'))
    
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

# TASK 7 Complete the function to remove the word WGU from the given string ONLY if it's not the first word and return the new string

def removeWGU(mystring):
    phrase = mystring.split()
    if phrase[0] == "WGU":
        return mystring
    else:
        return mystring.replace("WGU","")
    
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))

# TASK 8 Complete the function to remove trailing spaces from the first string and leading spaces from the second string and return the combined strings

def removeSpaces(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()
    
    return string1 + string2
    
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))

# TASK 9 Complete the function to print the specified hourly rate with two decimals

def displayHourlyRate(rate):
    print(f'${rate:.2f}')
 
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)

# TASK 10 Complete the function to return the number of uppercase letters in the given string

def countUpper(mystring):
    count = 0
    for i in mystring:
        if i.isupper():
            count += 1
    return count
 
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))
