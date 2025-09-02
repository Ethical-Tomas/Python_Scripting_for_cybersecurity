#Dictionaries and structuring data
#The dictionary data type
"""
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('My cat is ' + myCat['size'] + ' and has a ' + myCat['color'] + ' fur.')
"""

#Dictionaries vs. Lists
#Lists are ordered 
'''
spam = ['Zophie', 'cat', 8]
pet = ['cat', 8, 'Zophie']
print(spam == pet) #ANswer is false
'''
#Dictionaries are unordered
'''
spam = {'name': 'Zophie', 'type': 'cat', 'age': 8}
pet = {'type': 'cat', 'age': 8, 'name': 'Zophie'}
print(spam == pet) #Answer is True
'''

#Organizing data with dictionaries
'''
birthdays = {'Alice': 'Apr 1', 'John': 'Jun 12', 'Alex': 'Feb 15'}

while True:
    print('Enter the name of your friend (Blank to exit):')
    name = input()
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have information on ' + name + ' birthday')
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
'''
#The keys(), Values(), and Items() methods
'''
spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)
# for k in spam.keys():
#     print(k)
# for i in spam.items():
#     print(i)

for k, v in spam.items():
    print('Key: ' + k + ', Value: ' + str(v), sep=',')
'''

#Checking whether a key or value exists in a dictionary
'''
pet = {'name': 'Zophie', 'age': 8}
print('name' in pet.keys())
'''

#The get() Method
'''
picnicItems = {'apples': 4, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' apples', end='')
print(' and ' + str(picnicItems.get('drinks', 0)) + ' drinks')
'''

#The setdefault() method
'''
pet = {'name': 'Pooka', 'age': 6}
pet.setdefault('color', 'black')
for k, v in pet.items():
    print("Key: " + k + ', Value: ' + str(v))
'''

#Example SOlution using setdefault() method
#COunting the amount of letters in a sentence
'''
message = 'It was a cold day in April, the clocks were striking thirteen'
count = {}

for character in message:
     count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
'''

#Pretty Printing
'''
import pprint

message = 'It was a cold day in APril, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
'''
#A Tic-Tac-Toe Board
'''
theBoard = {
     'top-L': '', 'top-M': '', 'top-R': '',
     'mid-L': '', 'mid-M': '', 'mid-R': '',
     'low-L': '', 'low-M': '', 'low-R': ''
 }
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
'''

#fantasy game inventory
'''
inventory = {
    'gold': 93,
    'rope': 1,
    'dagger': 2,
    'food': 5,
    'shield': 1
}
def getInventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(" - " + k + ": " + str(v))
    print("Total number of items: " + str(sum(inventory.values())))
getInventory(inventory)
'''

def displayInventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(" - " + k + ": " + str(v))
    print("Total number of items: " + str(sum(inventory.values())))

def addInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addInventory(inv, dragonLoot)
displayInventory(inv)
