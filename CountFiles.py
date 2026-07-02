from pathlib import Path
from collections import defaultdict

count = defaultdict(int) # dict

while True:
    path = Path(input('Enter a directory path: '))

    if not path.exists():
        print('That path does not exist.')
    elif not path.is_dir():
        print('That path is not a directory')
    else:
        break
file_count = 0
folder_count = 0
for item in path.iterdir():
    if item.is_file():
        file_count+=1
        count[item.suffix.lower() or 'NONE'] += 1
    elif item.is_dir():
        folder_count+=1
print('Total Items: '+str(file_count+folder_count))   
print('Total Files: '+str(file_count)+'\n'+'Total Folders: '+str(folder_count))

sorted_dict = dict(sorted(count.items()))

for k,v in sorted_dict.items():
    print('Extension: '+k+' Amount: '+str(v))