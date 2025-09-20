#Working with Lists
#Storing multiple cat names using a list
'''
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
print('The cat names are:')
for name in catNames:
    print('-' + name)
'''

# Practice
# Adding new cat names to a list
'''
catNames = ['Zoey', 'Frikky', 'Weker', 'Boon']
while True:
    print(f'Enter the name of new cat {(len(catNames)+1)} (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames.append(name)
print('Your cats names are:')
for names in catNames:
    print('-' + names)
'''

# Using for loops with lists
'''
supplies = ['pens', 'staples', 'gum', 'erasers']
for i in range(len(supplies)):
    print('The index ' + str(i) + ' is the item ' + supplies[i])
'''

# The in and not in Operators
'''
myPets = ['Bella', 'Entertainment', 'Tatey']
print('Enter my pets name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
'''

#Example Program: Magic 8 Ball with a list
'''
import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
'''

# List-like Types: strings and tuples
'''
name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print(name[:2])
for i in name:
   print('***' + i + '***')
'''

#Mutable and Immutable Data Types 
#Strings are Immutable 
'''
name = 'Zophie a cat'
try:
    name[7] = 'the'
except TypeError:
    print('Strings are immutable cannot assign item')
'''
#Mutating a string with slicing and concatenation
'''
name = 'Zophie a cat'
print(name[0:7] + 'the' + name[8:12])
'''

#The tuple data type
'''
spam = ('hello', 42, 0.5) #This is a tuple
print(spam[0])
print(spam[1:3])
try:
    spam[1] = 40 #you cannot assign items to a tuple it is immutable
except TypeError: 
    print('Tuple is an immutable data type cannot assign item')
'''

#Converting types with the list() and tuple() functions
'''
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))
'''

#List reference in variables
'''
eggs = [0, 1, 2, 3, 4, 5, 6] #the list of numbers is a reference to eggs
cheese = eggs #now we are assigning the referenced variable to another
cheese[1] = 'Hello'
print(eggs)
print(cheese)
'''

#Passing Reference
'''
def eggs(someParameter):
   someParameter.append('Hello')
   
spam = [1, 2, 3]
eggs(spam)
print(spam)
'''
#The copy module's copy() and deepcopy() functions
'''
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 50
print(spam)
print(cheese)
'''

#Practice Projects
#Comma Code
'''
def convert(list_value):
    if not list_value:
        return ''
    elif len(list_value) == 1:
        return list_value[0]
    elif len(list_value) == 2:
        return f'{list_value[0]} and {list_value[1]}'
    else:
        return ', '.join(list_value[:-1]) + f', and {list_value[-1]}'
spam = ['apples', 'bananas', 'tofu', 'cat']
cheese = convert(spam)
print(cheese)
'''

#Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', '1'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for i in range(0, 9):
    return grid[0:9][0:6]


         
