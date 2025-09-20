#Manipulating Strings

#Escape characters
'''
spam = 'That is ALice\'s cat '
print(spam)
print('Hello there!\nHow are you\nI\'m doing fine.')
'''

#Raw Strings
# print(r'This is an escape character \'')

#Multiline string
# print('''Dear Alice,
# Eve's cat as been arrested for cat buglary and extortion.
# Sincerely,
# Bob.''')

#Indexing and slicing strings
'''
spam = 'Hello World!'
print(spam[0])
fizz = spam[0:5]
print(fizz)
'''

#upper(), lower(), isupper() and islower() string methods
'''
spam = 'Hello World'
spamm = spam.upper()
print(spamm)
fuzz = spam.lower()
print(fuzz)'''
'''
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too')
elif feeling.upper() == 'GOOD':
    print('I\'m feeling good too')
else:
    print('I hope you have a good rest of your day')
'''
'''
spam = 'HELLO'
fuzz = 'hello'
print(spam.isupper())
print(spam.islower())
print(spam.islower())
'''

#The isX Strings Method
'''
print('hello'.isalpha())
print('Hello135'.isalnum())
print('Hello'.isalnum())
print('     '.isspace())
print('Hello World'.isspace())
print('122346'.isdecimal())
print('Tomiwa Oladejo'.istitle())
'''

#Validating Input
'''
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Enter your age as a number.')

while True:
    print('Enter your username (Only letters and numbers):')
    username = input()
    if username.isalnum():
        break
    print('No special characters allowed for useername.')
'''

#The startswith() and endswith() methods
'''
spam = 'Hello world'
print(spam.startswith('Hello'))
print(spam.endswith('world'))
'''

#The join() and split() string method
'''
spam = ', '.join(['cats', 'bats', 'rats'])
print(spam)
fuzz = ' '.join(['cats', 'bats', 'rats'])
print(fuzz)
egg = "My name is Alex".split()
print(egg)
fizz = "My name is and might be morty".split('m')
print(fizz)'''
# message = '''Dear Alex,
# How are you doing today? I am fine,
# Just wanted to check up on you,
# Sincerely,
# Bob. '''
'''print(message.split('\n'))'''

#Justifying text with rjust(), ljust() and center()
'''
spam = 'Hello'
print(spam.rjust(10))
print(spam.ljust(12))
print(spam.center(20))
print(spam.rjust(10, '*'))
print(spam.ljust(12, '-'))
print(spam.center(20, "="))
'''

#Picnic List
'''
def printPicnic(itemsDict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))
picnic = {"drink": 4, "apples": 12, "cups": 7, "cookies": 300}
printPicnic(picnic, 20, 6)
'''

#Removing whitespace with strip(), rstrip(), and lstrip()