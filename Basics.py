# using modules by importing, can be done in 1 line
# round() and abs() are standard
import math, random, os, sys, copy
# can also use from math import *

print(math.sqrt(16))

print(2 ** 3) # exponentiation
print(22%8) # modulus
print(22//8) # integer division
print(22/8) # division (always floating point)
print(3*5) # division
print(5-2) # subtraction
print(2+2) # addition

# int++ and int-- are not supported :(

# naming convention : variable_name snake_case

# variables are automatically assigned a type
number = 3
text = 'word' # use '' instead of ""
floating_point_number = 3.5

# python uses + to concat, like most langs

print(text+str(number))
print(text*5) # string replication

# comparisons are like most langs
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 3)

# doesn't use || && ! literally uses
# and or not
age = 20
print(age > 18 and age < 30)

# uses : instead of {}
if age > 18:
    print('Adult')
else:
    print('child')

# loops are special
for i in range(5):
    print(i)

for i in range(0,10,2): # start stop step
    print(i)

# while loops are like most langs
while True: # booleans are capitalized
    break
    continue # unreachable


# lists, like arrays, mutable, tuples are immutable
# but can contain multiple types
numbers = [1,2,3]

numbers.append(4) # adding push_back
print(numbers[0]) # accessing
print(len(numbers)) # size of list

# dictionaries, very important
person = {
    "name": "Alex",
    "age": 20
}

print(person['name']) # accessing

# functions are called def
def check_age(): # automatically assigns type
    if age > 18:
        print('Adult')
    elif age < 0:
        print('Impossible') # elif instead of else if
    else:
        print('child')

# type conversion : int(), float(), str()

# to determine type use type()
print(type(42))

# input() to get input and () for the text
text = input('name: ')

# when used in conditions, 0, 0.0 and '' are false
if not 0:
    print('weird')

# to know if smth returns True or False
print(bool(0))
print(bool(67))

# random module
for i in range(3):
    print(random.randint(1,4)) # 1-4

# sys module
print('Type exit to exit.')
response = input('TYPE exit: ')
if response == 'exit':
    sys.exit()

# nil, null, undefined is called None in python
print(None == 2)

# print automatically separates multiple values using a space
print('cats','mice','dogs')
# the seperator can be replced
print('cats','mice','dogs',sep=';')

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])  # Last index
# 'elephant'

print(spam[0:4])
# ['cat', 'bat', 'rat', 'elephant']
# includes 0 excludes 4

print(spam[:2])
# ['cat', 'bat']
print(spam[1:])
# ['bat', 'rat', 'elephant']


# one can also add and replicate lists
spam = spam + ['A','B','C']
print(spam)
print(spam*2)

# del to delete list item
del spam[0]
print(spam)

# enumeration splits index and item

for index,item in enumerate(spam):
    print('Index: '+str(index)+" Item: "+item)

# random module has a choice functions and a shuffle
for i in range(3):
    print(random.choice(spam))

random.shuffle(spam)
print(spam)

# index to find the reverse from values
print(spam.index('A'))

# to add an item, either use append() or insert(index, value)
spam.append('appended')
spam.insert(1,'inserted')
print(spam)

# remove to remove a value
spam.remove('B')
print(spam)

# sort a list a-z-A-Z
spam.sort()
print(spam)
# sort a list a/A-z/Z
spam.sort(key=str.lower)
print(spam)
# reverse a list
spam.reverse()
print(spam)

# python strings are immutable !!!

#tuples are in () and they're immutable and can contain multiple types

eggs = ('hello',3,0.5)

# python variables can point to the same value

spam_same = spam
spam_same.append('appendicitis')
print(spam)

spam_copy = copy.copy(spam) # deepcopy() if the lists contains lists
spam_copy.append('appendicitis2')
print(spam_copy)
print(spam)

# dictionaries are unordered, lists are

cake = {'name':'Zophie','species':'cat','age':'8'}
muffin = {'species':'cat','age':'8','name':'Zophie'}
print(cake == muffin)
