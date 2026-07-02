from pathlib import Path

# p = Path('ReadWrite.txt')
# p.write_text('Hello, world!')

#print(p.read_text())

file = open('ReadWrite.txt')
print(file.read()) # reads content in one big string
file.seek(0)
print(file.readlines()) # list of strings

# write and append modes
file_write = open('ReadWrite.txt','w',encoding='UTF-8')
file_write.close()
file_append = open('ReadWrite.txt','a',encoding='UTF-8')
file_append.close()

with open('ReadWrite.txt','w',encoding='UTF-8') as file_with:
    file_with.write('Yellow World')

import shelve # store variables to binary shelf files
shelf_file = shelve.open('mydata')

shelf_file['cats'] = ['Zophie','Pooka','Simon']

# shelf values have keys and values like dicts
print(shelf_file['cats'])

shelf_file.close()

