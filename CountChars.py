print('Enter text that should be counted.')
text = input()
count = {} # dict

for character in text:
    count.setdefault(character,0) # initializes character in dict
    count[character] = count[character] + 1 # adds count to character

print(dict(sorted(count.items())))