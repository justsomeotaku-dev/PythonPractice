from pathlib import Path

# escape characters vs raw string
print('Hello \' \' world')
print(r'Hello \' \' world')

# multiline string
print('''Dear Alice,

Please feed the cat!
      
Sincerely,
Bob''')

"""multiline
comment"""

# indexes and slices work on strings

# fstrings are used for string interpolation
name = 'Alice'
print(f'My name is {name}')
print(name.upper())
print(name.lower())

# isX to use as filters
print('enter password (only letters and numbers)')
password = input()
if not password.isalnum():
    print('Only letters and numbers')
else:
    print('correct format')

# joining strings in a list
animals = ['cats','rats','bats']
joined = ';'.join(animals)
print(joined)
# splitting strings to a list
split = joined.split(';')
print(split)

# ljust and rjust add a num of chars, center
print(name.ljust(20,'-'))
print(name.rjust(20,'.'))
print(name.center(20,'#'))

# strip, also lstrip and rstrip same logic
ram = 'SpamSpamBaconSpamEggsSpamSpam'
print(ram.strip('ampS'))
fam = 'SpamSpamBaconSpamEggsSpamSpam'
print(fam.strip('Spam'))

# char to num and num to char
print(ord('B'))
print(chr(66))
print(chr(ord('A')+1))

# from pathlib import Path
my_files = ['accounts.txt','details.csv','invite.docx']
for filename in my_files:
    print(Path(r'C:\Users\John', filename))

# current working diectory
print(Path.cwd())
# home directory
print(Path.home())

# import os
import os
path = Path.cwd() / 'delicious' / 'walnut' / 'waffles'
# or path = Path.cwd() / Path('delicious/walnut/waffles')
# os.makedirs(path)

this_path = Path('./Basics.py')
print(this_path.stat())

# wildcards can be used and glob to list any content tha matches the pattern
print(list(Path('.').glob('*')))

for name in Path('.').glob('*'):
    print(name)