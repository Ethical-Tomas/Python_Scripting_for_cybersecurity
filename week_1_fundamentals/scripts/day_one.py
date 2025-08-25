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


