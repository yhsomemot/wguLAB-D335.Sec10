# wguLAB-D335.Sec10

**10.5 LAB: Checker for integer string**

Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input, and outputs Yes if every character is a digit 0-9 or No otherwise.

Ex: If the input is:
1995

the output is:
Yes

Ex: If the input is:
42,000

or any string with a non-integer character, the output is:
No

[answer](https://github.com/yhsomemot/wguLAB-D335.Sec10/blob/main/answer/10.5.py)

---

**10.6 LAB: Name format**

Many documents use a specific format for a person's name. Write a program whose input is:
firstName middleName lastName

and whose output is:
lastName, firstInitial.middleInitial.

Ex: If the input is:
Pat Silly Doe

the output is:
Doe, P.S.

If the input has the form:
firstName lastName

the output is:
lastName, firstInitial.

Ex: If the input is:
Julia Clark

the output is:
Clark, J.

[answer](https://github.com/yhsomemot/wguLAB-D335.Sec10/blob/main/answer/10.6.py)

---

**10.7 LAB: Count characters**

Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase. The output should include the input character and use the plural form, n's, if the number of times the characters appears is not exactly 1.

Ex: If the input is:
n Monday

the output is:
1 n

Ex: If the input is:
z Today is Monday

the output is:
0 z's

Ex: If the input is:
n It's a sunny day

the output is:
2 n's

Case matters. n is different than N.

Ex: If the input is:
n Nobody

the output is:
0 n's

[answer](https://github.com/yhsomemot/wguLAB-D335.Sec10/blob/main/answer/10.7.py)

---

**10.8 LAB: Mad Lib - loops**

Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.

Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in the example below. The program repeats until the input string is quit and disregards the integer input that follows.

Ex: If the input is:

apples 5

shoes 2

quit 0

the output is:

Eating 5 apples a day keeps the doctor away.

Eating 2 shoes a day keeps the doctor away.

[answer](https://github.com/yhsomemot/wguLAB-D335.Sec10/blob/main/answer/10.8.py)

---

**10.9 LAB: Remove all non-alpha characters**

Write a program that removes all non-alpha characters from the given input.

Ex: If the input is:
-Hello, 1 world$!

the output is:
Helloworld

[answer](https://github.com/yhsomemot/wguLAB-D335.Sec10/blob/main/answer/10.9.py)

---

**extra practice**

Task 1

Complete the function to print the first X number of characters in the given string

```python
# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
# Student code goes here
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)
```

Task 2

Complete the function to return the last X number of characters in the given string

```python
# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
# Student code goes here
 
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))
```

Task 3

Complete the function to return True if the word WGU exists in the given string otherwise return False

```python
# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
# Student code goes here
    
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
```

Task 4

Complete the function to print all of the words in the given string

```python
# Complete the function to print all of the words in the given string
def printWords(mystring):
# Student code goes here
    
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')
print(containsWGU('Night Owls Rock'))
```

Task 5

Complete the function to combine the words into a sentence and return a string

```python
# Complete the function to combine the words into a sentence and return a string 
def combineWords(words):
# Student code goes here
    
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))
```

Task 6

Complete the function to replace the word WGU with Western Governors University and print the new string

```python
# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
# Student code goes here
    
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')
```

Task 7

Complete the function to remove the word WGU from the given string ONLY if it's not the first word and return the new string

```python
# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
# Student code goes here
    
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))
```

Task 8

Complete the function to remove trailing spaces from the first string and leading spaces from the second string and return the combined strings

```python
# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
# Student code goes here
    
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))
```

Task 9

Complete the function to print the specified hourly rate with two decimals

```python
# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
# Student code goes here
 
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)
```

Task 10

Complete the function to return the number of uppercase letters in the given string

```python
# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
# Student code goes here
 
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))
```

[answers](https://github.com/yhsomemot/wguLAB-D335.Sec10/blob/main/answer/10.10.py)

---
